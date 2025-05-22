# 🍷 PilotProject: Wine Quality Prediction ML Pipeline

**End-to-end Machine Learning pipeline for predicting wine quality**, built with production-ready engineering practices.

This project features modular ML components, experiment tracking with MLflow, and a Flask-based UI for real-time inference.

---

## 🧰 Tech Stack Used

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-lightgrey?logo=flask)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue?logo=mlflow)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Config-F4D03F?logo=yaml&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Data_Handling-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Math-blueviolet?logo=numpy)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/VS_Code-Editor-007ACC?logo=visual-studio-code)

---

## 🚀 Features

- ✅ Modular pipeline architecture with CLI and UI interfaces
- ✅ YAML-based configuration for easy customization
- ✅ Data validation with schema enforcement
- ✅ ElasticNet regression model with configurable parameters
- ✅ MLflow tracking for metrics, parameters, and models
- ✅ Flask web UI with `/train` and `/predict` endpoints
- ✅ Docker support for containerized deployment
- ✅ Logs, metrics, and predictions are persisted

---

## 📁 Project Structure

<details> <summary>📁 Project Structure (click to expand)</summary>
text
Copy
Edit
pilotproject/
├── app.py                  # Flask app with /train and /predict
├── main.py                 # Pipeline entry point
├── config/
│   └── config.yaml         # Path and pipeline configuration
├── params.yaml             # Model hyperparameters
├── schema.yaml             # Input data schema
├── src/
│   └── pilotproject/
│       ├── components/     # ML logic (ingestion, transform, train, etc.)
│       ├── pipeline/       # Orchestrators for each ML stage
│       ├── config/         # Configuration manager
│       ├── entity/         # Dataclass-based config entities
│       ├── utils/          # Helpers (YAML, JSON, file I/O)
│       └── constants/      # Constant paths to YAML files
├── templates/
│   ├── index.html          # Home page form
│   └── results.html        # Prediction output page
├── artifacts/              # All generated outputs (raw, processed, model)
├── mlruns/                 # MLflow experiment logs
├── logs/                   # Runtime logs (pipeline + Flask)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Containerization instructions
└── setup.py                # Project packaging script
</details>
