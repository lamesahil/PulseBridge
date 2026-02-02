# 🎀 PulseBridge – AI Breast Cancer Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pulsebridge.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Live-success)

**PulseBridge** is an AI-powered healthcare application designed to assist in the early detection of breast cancer. It predicts whether a tumor is **Benign (Safe) ✅** or **Malignant (Danger) ⚠️** using a Machine Learning model trained on clinical biopsy data.

🔗 **Live Demo:** [Click Here to View App](https://pulsebridge.streamlit.app/)

---

## 👥 The Team

| Name | Role | GitHub |
| :--- | :--- | :--- |
| **Sahil Tiwari** | **Lead Developer** (Frontend, Integration & Deployment) | [@lamesahil](https://github.com/lamesahil) |
| **Anuvesh Tiwari** | **ML Engineer** (Model Training & Evaluation) | [@aanuvesh24](https://github.com/aanuvesh24) |

> *Built with ❤️ using **Streamlit** for the UI and accelerated using **Generative AI** for code optimization and logic refinement.*

---

## 🛠 Tech Stack

* **Frontend & Deployment:** [Streamlit](https://streamlit.io/) (Interactive Web UI)
* **Machine Learning:** Scikit-learn (Logistic Regression)
* **Data Processing:** NumPy, Pandas
* **Visualization:** Matplotlib, Seaborn, Plotly
* **IDE/Tools:** VS Code, Jupyter Notebook

---

## 🧬 Project Overview & Features

The system uses the **10 most significant features** from the dataset to ensure fast, accurate, and interpretable predictions.

### Key Features:
* **🧹 Smart Data Handling:** Handles missing values automatically using mean imputation.
* **📊 Robust Preprocessing:** Standardizes patient data using `StandardScaler` for higher accuracy.
* **💻 Real-time Analysis:** Instant predictions through a user-friendly Streamlit interface.
* **📈 Data Visualization:** Interactive charts to understand risk factors (powered by Plotly).
* **🔗 Seamless Integration:** Designed to be easily integrated with external APIs.

---

## 🚀 How to Run Locally

If you want to run this project on your own machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/lamesahil/PulseBridge-AI.git](https://github.com/lamesahil/PulseBridge-AI.git)
    cd PulseBridge-AI
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

## 🔮 Future Enhancements

* **🧩 Explainable AI:** Add SHAP/LIME feature importance charts for better medical interpretability.
* **🌐 API Deployment:** Deploy the model via Flask/FastAPI for hospital system integration.
* **📋 Batch Processing:** Enable uploading CSV files for multiple patient predictions at once.

---

## ⚠️ Disclaimer
*This project is a prototype developed for educational and hackathon purposes. It is intended to assist medical professionals, not replace them. Always consult a certified oncologist for diagnosis.*
