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

## 🗂️ Project Structure

```text
pilotproject/
├── app.py                    # Flask web server
├── main.py                   # Pipeline runner
├── config/                   # YAML configuration files
│   └── config.yaml
├── params.yaml               # Model hyperparameters
├── schema.yaml               # Column definitions
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker build instructions
├── logs/                     # All application logs
├── datasets/                 # Source datasets (zip)
├── artifacts/                # Output from each pipeline stage
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   ├── model_trainer/
│   ├── model_evaluation/
│   └── model_prediction/
├── mlruns/                   # MLflow tracking directory
├── templates/                # Flask HTML templates
│   ├── index.html
│   └── results.html
└── src/pilotproject/         # Main package
    ├── components/           # Stage logic (ingest, validate, train, etc.)
    ├── pipeline/             # Pipeline orchestration
    ├── config/               # Configuration manager
    ├── entity/               # Dataclasses for configs
    ├── constants/            # Path constants
    └── utils/                # Common utilities

```
---

## ⚙️ Configuration

All configuration is handled through YAML and `.env` files for clean, flexible pipeline control.

- Edit dataset paths, output directories, and URLs in:  
  `config/config.yaml`

- Set model hyperparameters like `alpha`, `l1_ratio` in:  
  `params.yaml`

- Define schema (column names and data types) in:  
  `schema.yaml`

- Configure MLflow tracking URI and other secrets via `.env` file:

```dotenv
MLFLOW_TRACKING_URI=<your-mlflow-uri>

```
---
## 🧪 How to Run the Project

Follow these steps to set up, train, and run the ML pipeline with both CLI and Web UI support.

---

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
---

### 🔐 Step 2: Set Up Environment Variables

Create a `.env` file in the root directory and add the following:

```dotenv
MLFLOW_TRACKING_URI=<your-mlflow-uri>
MLFLOW_TRACKING_USERNAME=<your-username>
MLFLOW_TRACKING_PASSWORD=<your-password>
```

---
### 📦 Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

### 🛠️ Step 4: Run the Training Pipeline

This command runs the complete ML pipeline:

- Data ingestion  
- Data validation  
- Data transformation  
- Model training  
- Model evaluation (logged to MLflow)

```bash
python main.py
```

---

### 🌐 Step 5: Launch the Flask Web App

Start the prediction server:

```bash
python app.py
```

Then open your browser and go to:

```bash
http://localhost:8080
```

Use the UI to enter wine chemical attributes and receive quality predictions.
---

### 📊 Step 6: Launch MLflow UI (Optional)

To view tracked runs, metrics, and artifacts:

```bash
mlflow ui
```

Visit:

```bash
http://localhost:5000
```

You’ll be able to view:

- RMSE, MAE, R² metrics  
- Logged parameters (`alpha`, `l1_ratio`)  
- Saved models and input examples


