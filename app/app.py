from fastapi import FastAPI
import joblib
import re
import spacy

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("model/resume_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Load NLP
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

# -----------------------------
# TEXT CLEANING
# -----------------------------
def clean_text(text):
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = " ".join(re.findall(r"\w+", text))
    doc = nlp(text)
    return " ".join([t.lemma_.lower() for t in doc if not t.is_stop])


# -----------------------------
# ROUTES
# -----------------------------
@app.get("/")
def home():
    return {"message": "Resume API Running 🚀"}


@app.post("/predict")
def predict(data: dict):
    try:
        text = data.get("resume", "")

        if not text.strip():
            return {"error": "Empty resume text"}

        cleaned = clean_text(text)

        if cleaned.strip() == "":
            return {"error": "Text cleaning removed all content"}

        vector = vectorizer.transform([cleaned])

        pred = model.predict(vector)[0]

        return {"prediction": str(pred)}

    except Exception as e:
        return {"error": str(e)}
