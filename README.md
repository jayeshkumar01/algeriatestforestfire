# Algerian Forest Fire Prediction 🔥

An end-to-end machine learning project that predicts the **Fire Weather Index (FWI)** for regions in Algeria using weather and fire-related features, deployed as a Flask web application on AWS.

## 📌 Overview

This project walks through the complete ML lifecycle:
- Exploratory Data Analysis (EDA) on the Algerian Forest Fires dataset
- Data cleaning and preprocessing
- Training and comparing multiple regression models
- Feature scaling and final model selection (Ridge Regression)
- Model deployment via a Flask web app for real-time predictions
- Cloud deployment on AWS (Elastic Beanstalk)

## 🎯 Problem Statement

The goal is to predict the **Fire Weather Index (FWI)** — a numerical rating of fire intensity risk — based on weather conditions and fire-related indices recorded for regions in Algeria. This is a **regression problem**, since FWI is a continuous numeric value.

## 📊 Dataset Outline

The dataset contains **244 records** collected from two regions in Algeria — **Bejaia** (northeast) and **Sidi Bel-abbes** (northwest) — between **June and September 2012**.

**Input features:**
| Feature | Description |
|---|---|
| Temperature | Noon temperature (°C) |
| RH | Relative Humidity (%) |
| Ws | Wind speed (km/h) |
| Rain | Total rainfall (mm) |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| DC | Drought Code |
| ISI | Initial Spread Index |
| BUI | Buildup Index |
| Classes | Fire / not fire (categorical) |
| Region | Bejaia / Sidi Bel-abbes |

**Target variable:**
- **FWI (Fire Weather Index)** — the value being predicted

## 🧠 Models Trained & Compared

Multiple regression models were trained and evaluated to find the best performer:

- Linear Regression
- Lasso Regression
- Lasso Regression with Cross-Validation (LassoCV)
- Ridge Regression
- Ridge Regression with Cross-Validation (RidgeCV)
- ElasticNet Regression
- ElasticNet Regression with Cross-Validation (ElasticNetCV)

After comparison, **Ridge Regression** was selected as the final model based on performance, and saved as `ridge.pkl` along with the fitted `scaler.pkl` for feature scaling.

## 📂 Project Structure
ALGERIA_FOREST_FIRE_PREDICTION/
│
├── .ebextensions/                                # AWS Elastic Beanstalk configuration
├── templates/                                    # HTML templates for the Flask app
├── Algerian_forest_fires_dataset_UPDATE.csv      # Raw dataset
├── Algerian_forest_fires_cleaned_Dataset.csv     # Cleaned dataset after preprocessing
├── algeriafireforest.ipynb                       # Jupyter notebook (EDA, preprocessing, model training)
├── application.py                                # Flask application
├── ridge.pkl                                     # Trained Ridge Regression model
├── scaler.pkl                                    # Fitted StandardScaler for input features
├── requirements.txt                              # Project dependencies
└── .gitignore
## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy** – data manipulation
- **Matplotlib, Seaborn** – data visualization
- **Scikit-learn** – model training (Linear, Ridge, Lasso, ElasticNet + CV variants) and feature scaling
- **Flask** – web app for serving predictions
- **AWS Elastic Beanstalk** – cloud deployment

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jayeshkumar01/algeriatestforestfire.git
cd algeriatestforestfire
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\Activate.ps1     # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python application.py
```

Then open `http://127.0.0.1:5000` in your browser.

## 🖥️ How the App Works

1. Open the home page and navigate to the prediction form
2. Enter the weather/fire index values (Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, BUI)
3. The app scales your inputs using the saved `scaler.pkl` and feeds them into the trained `ridge.pkl` model
4. The predicted FWI value is displayed on the page

**Example output:**
The FWI prediction is 16.4079084392512
## 🧠 Model

Several regression models — Linear Regression, Ridge, Lasso, ElasticNet, and their cross-validated variants (RidgeCV, LassoCV, ElasticNetCV) — were trained and compared. **Ridge Regression** gave the best performance and was selected as the final model. It's saved as `ridge.pkl`, alongside the fitted `scaler.pkl` used to scale inputs before prediction. Both are loaded in `application.py` to serve real-time predictions through the Flask interface.

## ☁️ Deployment

This app is deployed on **AWS Elastic Beanstalk**, making the FWI prediction tool accessible online.

🔗 **Live app:** http://algeriatestforestfire.eba-aiftrm26.eu-north-1.elasticbeanstalk.com/

## 📈 Future Improvements

- Add model performance metrics and comparison visualizations
- Improve the front-end UI/UX

## 🙌 Acknowledgements

Dataset source: [UCI Machine Learning Repository – Algerian Forest Fires Dataset](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
