# 📄 AI Resume Classification System (NLP | FastAPI | Streamlit | Docker | GCP Deployment)

🚀 Production-ready NLP system that classifies resumes into job roles using machine learning with real-time inference deployed on cloud.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![GCP](https://img.shields.io/badge/Cloud-GCP-orange)

---

🎬 **Deployment Demo Available Below**

⚠️ **Note:** The original cloud deployment was hosted on Google Cloud Platform (GCP). The VM instance may currently be offline to optimize hosting costs.

🎥 The demo GIF below was recorded from the deployed cloud application and showcases the complete end-to-end workflow, including:

✔ Resume upload

✔ Real-time predictions

✔ Dashboard visualization

✔ API integration

✔ Production deployment workflow

🎯 End-to-end ML system:

**Data → NLP Processing → Model → API → Dashboard → Docker → Cloud Deployment**

---

## 🎥 Live Demo (Quick Preview)

> The following demo was recorded from the deployed cloud application and demonstrates the complete workflow.

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

✔ Dockerized production-ready deployment

✔ Containerized API serving architecture

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

✔ Dockerized deployment workflow

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

```text
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

## 🏗️ Dockerized Architecture

```text
Docker Container
│
├── FastAPI Backend
├── NLP Processing Pipeline
├── Trained ML Model
├── spaCy Language Model
└── REST API Service
```

---

## 🏗️ Architecture Details

* FastAPI handles real-time prediction requests
* Streamlit provides interactive frontend interface
* NLP pipeline processes raw resume text
* TF-IDF converts text into numerical features
* Model performs classification
* Stateless API enables scalability
* Docker ensures environment consistency and portability

---

## 📈 Model Performance

### 📊 Evaluation Metrics

| Metric | Value | Interpretation |
|----------|--------|--------|
| **Accuracy** | ~90% | Overall classification performance |
| **Precision** | ~0.89 | Correct positive predictions |
| **Recall** | ~0.88 | Coverage of actual positives |
| **F1 Score** | ~0.88 | Balance between precision & recall |

---

📌 **Key Highlight:** Achieves strong performance with lightweight ML model suitable for real-time deployment

---

## 🌐 Cloud Deployment

🚀 Originally deployed on Google Cloud Platform (GCP)

⚠️ **Deployment Status:** The cloud instance may currently be offline to optimize hosting costs.

🎬 **Deployment Walkthrough:** Please refer to the demo GIF above, which was recorded from the deployed application and demonstrates the complete end-to-end workflow.

---

## 🐳 Dockerized Deployment

This project has been fully containerized using Docker for reproducible and production-ready deployment.

---

## 🚀 Why Docker?

✔ Ensures consistent environment across systems

✔ Eliminates dependency conflicts

✔ Simplifies deployment workflow

✔ Supports scalable cloud-native deployment

✔ Enables isolated execution environment

✔ Improves portability across machines and servers

---

## 📦 Dockerfile Highlights

✔ Lightweight Python 3.11 slim image

✔ Optimized build context using `.dockerignore`

✔ Separate model and app copy strategy

✔ Reduced unnecessary file transfer

✔ Production-ready FastAPI startup command

✔ Optimized containerized deployment workflow

---

## 📂 Docker Files Added

```text
Dockerfile
.dockerignore
```

---

## ⚙️ Build Docker Image

```bash
docker build -t resume-api .
```

---

## ▶️ Run Docker Container

```bash
docker run -p 8000:8000 resume-api
```

---

## 🌐 Access Dockerized API

### FastAPI Swagger Docs

```text
http://localhost:8000/docs
```

---

## 🧠 Docker Optimization Techniques Used

✔ `.dockerignore` to exclude unnecessary files

✔ Avoided large notebook/data transfer

✔ Selective COPY commands instead of `COPY . .`

✔ Lightweight base image (`python:3.11-slim`)

✔ Cached dependency installation layers

✔ Reduced Docker build context size

---

## 📊 Docker Benefits for ML Systems

* Faster deployment
* Reproducible environments
* Easier scaling
* Simplified CI/CD integration
* Better portability across cloud platforms
* Production-grade deployment workflow

---

## 🔥 Production Engineering Concepts Demonstrated

✔ Containerization

✔ REST API Deployment

✔ Dependency Isolation

✔ Build Context Optimization

✔ FastAPI Production Serving

✔ Cloud-Ready Architecture

✔ Dockerized ML Deployment

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
* Containerization: Docker

---

## ▶️ Run on Cloud VM

```bash
source env/bin/activate

uvicorn app.app:app --host 0.0.0.0 --port 8000

streamlit run app/ui.py --server.port 8501 --server.address 0.0.0.0
```

---

## 🐳 Run Using Docker

```bash
git clone https://github.com/Kiran-id10/resume-classification-nlp.git

cd resume-classification-nlp

docker build -t resume-api .

docker run -p 8000:8000 resume-api
```

---

## 🧰 Tech Stack

* Python
* Scikit-learn
* spaCy
* FastAPI
* Streamlit
* Docker
* PyPDF2
* python-docx
* Matplotlib

---

## 📂 Project Structure

```text
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
├── Dockerfile
├── .dockerignore
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
* REST API support
* Dockerized deployment
* Production-ready architecture

---

## 💡 Key Learnings

* Built production-ready NLP pipeline
* Applied real-world text preprocessing
* Integrated API + UI
* Deployed ML system on cloud
* Solved real deployment issues
* Learned Docker containerization
* Optimized Docker build context
* Implemented production deployment workflow

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
* Add Docker Compose for multi-container deployment
* Kubernetes deployment
* CI/CD pipeline integration
* Improve UI/UX

---

## 👨‍💻 Author

**Kiran Kumar S R**

🎓 Data Science & AI Engineer

💼 Actively seeking Data Science / ML opportunities

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
