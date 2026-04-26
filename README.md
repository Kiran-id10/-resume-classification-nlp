# 📄 AI Resume Classification System (NLP | FastAPI | Streamlit | GCP Deployment)

🚀 Production-ready NLP system that classifies resumes into job roles using machine learning with real-time inference deployed on cloud.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![GCP](https://img.shields.io/badge/Cloud-GCP-orange)

---

🚀 **Live App:** http://34.131.252.227:8501

⚡ **API Docs:** http://34.131.252.227:8000/docs

🎯 End-to-end ML system:
**Data → NLP Processing → Model → API → Dashboard → Cloud Deployment**

---

## 🎥 Live Demo (Quick Preview)

![Demo](screenshots/demo.gif)

---

## 📸 Dashboard Preview

### 🖥️ Step 1: Upload Resume Files

![Dashboard](screenshots/Dashboard1.png)

### 📊 Step 2: View Predictions & Visualization

![Results](screenshots/Dashboard2.png)

---

## 🏆 Why This Project Stands Out

✔ Real-time deployed NLP system (not just notebook)

✔ Multi-format resume processing (PDF, DOCX, TXT)

✔ Cloud-hosted application with public access

✔ API + UI integration

✔ Production-style ML pipeline

---

## 🔥 Project Highlights

✔ Automated resume parsing and text extraction

✔ NLP preprocessing using spaCy (lemmatization + stopword removal)

✔ TF-IDF feature engineering

✔ Machine Learning classification using Multinomial Naive Bayes

✔ REST API using FastAPI

✔ Interactive dashboard using Streamlit

✔ Batch prediction support

✔ Visualization of prediction distribution

✔ Download results as CSV

✔ Deployed on GCP VM with static external IP

---

## 🧠 Problem Statement

Recruiters receive hundreds of resumes for each job role, making manual screening inefficient and time-consuming.

👉 Traditional manual filtering is slow and error-prone

👉 This system automates resume classification using NLP to enable faster and scalable hiring workflows

💼 **Impact:** Reduces manual resume screening time and improves hiring efficiency

📈 Enables scalable and automated candidate filtering for recruitment pipelines

---

## 📊 Dataset

* Source: Public dataset (Kaggle)
* Samples: 79+ resumes (demo dataset; scalable to large datasets)
* Classes: 4 job roles

  * Peoplesoft
  * React Developer
  * SQL Developer
  * Workday

### 🔧 Preprocessing

* Removed noise (URLs, symbols)
* Lemmatization using spaCy
* Stopword removal
* Text normalization

---

## 🏗️ System Architecture

```
User
 ↓
Streamlit UI
 ↓
FastAPI API
 ↓
NLP Processing
 ↓
ML Model
 ↓
Prediction
```

---

## 🏗️ Architecture Details

* FastAPI handles real-time prediction requests
* Streamlit provides interactive frontend interface
* NLP pipeline processes raw resume text
* TF-IDF converts text into numerical features
* Model performs classification
* Stateless API enables scalability

---

## 📈 Model Performance

### 📊 Evaluation Metrics

| Metric        | Value | Interpretation                     |
| ------------- | ----- | ---------------------------------- |
| **Accuracy**  | ~90%  | Overall classification performance |
| **Precision** | ~0.89 | Correct positive predictions       |
| **Recall**    | ~0.88 | Coverage of actual positives       |
| **F1 Score**  | ~0.88 | Balance between precision & recall |

---

📌 **Key Highlight:** Achieves strong performance with lightweight ML model suitable for real-time deployment

---

## 🌐 Live Cloud Deployment

🚀 Deployed on Google Cloud Platform (GCP)

### 📊 Streamlit Dashboard

👉 http://34.131.252.227:8501

### ⚡ FastAPI API Docs

👉 http://34.131.252.227:8000/docs

⚠️ Note: VM may be stopped to optimize cost

---

## 🔌 API Example

```bash
curl -X POST "http://34.131.252.227:8000/predict" \
-H "Content-Type: application/json" \
-d '{"resume": "Python developer with machine learning experience"}'
```

---

## 🧠 Model Selection Rationale

* TF-IDF efficiently represents textual data
* Multinomial Naive Bayes performs well on high-dimensional text
* Lightweight and fast → ideal for real-time APIs

### Compared Alternatives

* Logistic Regression → similar performance, higher compute
* Deep Learning (BERT) → better accuracy but higher latency

---

## ⚖️ Design Trade-offs

* Chose Naive Bayes for speed over deep learning accuracy
* Optimized for real-time prediction rather than heavy computation
* Balanced performance and deployment simplicity

---

## ⚠️ Limitations

* Limited dataset size (demo dataset)
* Model performance depends on resume quality
* PDF parsing may fail for scanned resumes
* Limited generalization for unseen job roles

---

## ☁️ Deployment Details

* Platform: Google Cloud Platform (GCP VM)
* OS: Linux (Debian)
* Backend: FastAPI (Uvicorn)
* Frontend: Streamlit
* Networking: Static External IP

---

## ▶️ Run on Cloud VM

```bash
source env/bin/activate

uvicorn app.app:app --host 0.0.0.0 --port 8000

streamlit run app/ui.py --server.port 8501 --server.address 0.0.0.0
```

---

## 🧰 Tech Stack

* Python
* Scikit-learn
* spaCy
* FastAPI
* Streamlit
* PyPDF2
* python-docx
* Matplotlib

---

## 📂 Project Structure

```
resume-classification-nlp/
│
├── app/
│   ├── app.py
│   └── ui.py
│
├── model/
│   ├── resume_model.pkl
│   └── vectorizer.pkl
│
├── data/
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/Kiran-id10/resume-classification-nlp.git
cd resume-classification-nlp

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
```

---

## ▶️ Run Locally

```bash
uvicorn app.app:app --reload
streamlit run app/ui.py
```

---

## 📊 Features

* Upload multiple resumes
* View predictions in table format
* Visualize distribution
* Download results as CSV

---

## 💡 Key Learnings

* Built production-ready NLP pipeline
* Applied real-world text preprocessing
* Integrated API + UI
* Deployed ML system on cloud
* Solved real deployment issues

---

## 🎯 Use Cases

* HR automation
* Resume screening
* Talent filtering
* Recruitment analytics

---

## 🔮 Future Improvements

* Add confidence scores
* Integrate deep learning (BERT)
* Dockerize application
* Improve UI/UX

---

## 👨‍💻 Author

**Kiran Kumar S R**

🎓 Data Science & AI Engineer
💼 Actively seeking Data Science / ML opportunities

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!

