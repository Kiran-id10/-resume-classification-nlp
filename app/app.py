from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model/resume_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "Resume API running 🚀"}

@app.post("/predict")
def predict(data: dict):
    try:
        text = data["resume"]

        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]

        return {"prediction": pred}

    except Exception as e:
        return {"error": str(e)}
