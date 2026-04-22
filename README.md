 📄 AI Resume Classification System (NLP + Cloud Deployment)

🚀 **Live Production Demo:** http://34.14.222.60:8501

🎯 Automatically classifies resumes into job roles with real-time predictions via API and an interactive dashboard.

---

## 🎥 Live Demo (Quick Preview)

![Demo](screenshots/demo.gif)

---

## 📸 Dashboard Preview

### 🖥️ Main Dashboard

![Dashboard](screenshots/Dashboard1.png)

### 📊 Predictions & Visualization

![Results](screenshots/Dashboard2.png)

---

## 🔥 Project Highlights

✔ Multi-format resume support (PDF, DOCX, TXT)
✔ Automated text extraction pipeline
✔ NLP preprocessing using spaCy (lemmatization + stopword removal)
✔ TF-IDF feature engineering
✔ Machine Learning classification (Multinomial Naive Bayes)
✔ REST API using FastAPI
✔ Interactive dashboard using Streamlit
✔ Batch prediction support
✔ Data visualization (prediction distribution)
✔ Download results as CSV
✔ Deployed on Google Cloud VM with static IP
✔ Production-ready ML system with real-time inference

---

## 🧠 Problem Statement

Recruiters receive hundreds of resumes for each job role, making manual screening inefficient and time-consuming.

👉 This system automates resume classification using NLP to enable faster and scalable hiring workflows.

💼 **Impact:** Reduces manual resume screening time by automating candidate categorization at scale.

💡 This project simulates a real-world HR automation system used in recruitment pipelines.

---

## 📊 Dataset

- Source: Public resume dataset (Kaggle)
- Number of samples: 79+ resumes (used for demonstration; scalable to larger datasets)
- Number of classes: 04 job categories (peoplesoft , react developer , sql developer , workday)
- Preprocessing:
  - Removed noise (URLs, symbols)
  - Lemmatization using spaCy
- Data imbalance handled using standard train-test split

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

- FastAPI handles real-time prediction requests
- Streamlit acts as the frontend interface for user interaction
- NLP preprocessing pipeline cleans and transforms resume text
- Model and vectorizer are loaded into memory for low-latency inference
- Stateless API design allows easy scalability and deployment
- Designed to scale with larger datasets and can be extended using distributed processing frameworks

---

## 🌐 Live Cloud Deployment

🚀 Deployed on Google Cloud Platform (GCP)

### 🔗 Streamlit Dashboard

👉 http://34.14.222.60:8501

### ⚡ FastAPI API Docs

👉 http://34.14.222.60:8000/docs

⚠️ Note: Demo runs on a cloud VM and may be inactive outside working hours.

---

## 🔌 API Example

```bash
curl -X POST "http://34.14.222.60:8000/predict" \
-H "Content-Type: application/json" \
-d '{"resume": "Python developer with machine learning experience"}'
```

👉 Returns predicted job category from the model.

---

## 📈 Model Performance

* Accuracy: ~90%
* Precision: ~0.89
* Recall: ~0.88
* F1 Score: ~0.88

📊 Evaluated on multi-class resume dataset with diverse job categories using train-test split.

---

## 🧠 Model Selection Rationale

- TF-IDF chosen for efficient numerical representation of textual data
- Multinomial Naive Bayes performs well on high-dimensional sparse data like text
- Lightweight and fast inference makes it suitable for real-time API deployment
- Compared alternatives:
  - Logistic Regression: higher computational cost for similar performance
  - Deep learning (BERT): higher accuracy but not suitable for low-latency deployment in this use case

---

## 🚀 Why This Project Stands Out

* End-to-end ML pipeline (data → preprocessing → model → deployment)
* Real-time API + UI integration
* Cloud deployment on GCP with public access
* Handles real-world resume formats
* Designed for scalable deployment and real-time inference
* Production-style system design

---

## ⚖️ Design Trade-offs

- Chose Naive Bayes over deep learning models for faster inference
- Lightweight architecture ensures low latency but slightly lower accuracy than transformer models
- Optimized for real-time prediction rather than heavy batch processing

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

⚠️ Note: If the app is not accessible, the VM instance may be stopped to save cost.

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
* View predictions in tabular format
* Visualize prediction distribution
* Download results as CSV

---

## 💡 Key Learnings

* Built a production-ready ML pipeline
* Applied NLP preprocessing for real-world text
* Integrated FastAPI with Streamlit
* Deployed ML system on cloud infrastructure
* Managed real-world deployment challenges

---

## 🎯 Use Cases

* HR automation
* Resume screening
* Talent filtering
* Recruitment analytics

---

## 🔮 Future Improvements

* Add prediction confidence scores
* Dockerize the application
* Improve UI/UX
* Upgrade to deep learning models (BERT)

---

## ⚠️ Limitations

- Model performance depends on resume text quality
- PDF parsing may fail for scanned/image-based resumes
- Free-tier cloud deployment may introduce latency
- Limited generalization for unseen job categories

----

## 👨‍💻 Author

**Kiran Kumar S R**

🎓 Data Science & AI Engineer
💼 Actively seeking Data Science / ML opportunities

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!

