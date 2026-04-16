import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import PyPDF2
import docx

st.set_page_config(page_title="Resume Classifier", layout="wide")

st.title("📄 AI Resume Classification System")

# -----------------------------
# 📄 TEXT EXTRACTION
# -----------------------------
def extract_text(file):
    text = ""

    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + " "

    elif file.type == "text/plain":
        text = file.read().decode("utf-8")

    return text


# -----------------------------
# 📂 FILE UPLOAD
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload Resume Files (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:

    results = []

    for file in uploaded_files:
        text = extract_text(file)

        if text.strip():
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"resume": text}
            )

            prediction = response.json()["prediction"]

            results.append({
                "File Name": file.name,
                "Prediction": prediction
            })

    df = pd.DataFrame(results)

    st.write("### ✅ Prediction Results")
    st.dataframe(df)

    # -----------------------------
    # 📊 VISUALIZATION
    # -----------------------------
    st.write("### 📊 Prediction Distribution")

    counts = df["Prediction"].value_counts()

    fig, ax = plt.subplots()
    counts.plot(kind='bar', ax=ax)

    st.pyplot(fig)

    # -----------------------------
    # 📥 DOWNLOAD
    # -----------------------------
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Results",
        csv,
        "resume_predictions.csv",
        "text/csv"
    )
