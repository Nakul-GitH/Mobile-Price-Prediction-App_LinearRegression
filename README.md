# 📱 Mobile Price Prediction using Machine Learning & Streamlit

## 🚀 Live Demo

🔗 Streamlit Application: [*(https://mobile-price-prediction-app-linearregression.streamlit.app/)*]

---

# 📌 Project Overview

This project is an end-to-end Machine Learning regression application developed to predict the price of mobile phones based on their technical specifications.

The project covers the complete Machine Learning lifecycle including:

* Data Collection
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Skewness Treatment
* Feature Scaling
* Model Building
* Regularization Techniques
* Model Evaluation
* Streamlit Deployment
* GitHub Version Control
* Cloud Deployment

The application was deployed successfully using **Streamlit Cloud** and integrated with **GitHub** for version control and project hosting.

---

# 🎯 Problem Statement

The objective of this project is to build a Machine Learning model capable of predicting mobile phone prices based on features such as:

* RAM
* Internal Memory
* Battery Capacity
* CPU Specifications
* Camera Specifications
* Screen Resolution
* PPI
* Thickness
* Weight
* Sales Volume

This is a **Supervised Machine Learning Regression Problem**.

---

# 📂 Dataset Information

Dataset Source:

🔗 [https://www.kaggle.com/datasets/mohannapd/mobile-price-prediction/data](https://www.kaggle.com/datasets/mohannapd/mobile-price-prediction/data)

### Dataset Shape

* Rows: 161
* Columns: 14

### Features Used

| Feature      | Description             |
| ------------ | ----------------------- |
| Sale         | Sales count             |
| weight       | Mobile weight           |
| resolution   | Screen resolution       |
| ppi          | Pixels per inch         |
| cpu core     | Number of CPU cores     |
| cpu freq     | CPU frequency           |
| internal mem | Internal storage        |
| ram          | RAM capacity            |
| RearCam      | Rear camera megapixels  |
| Front_Cam    | Front camera megapixels |
| battery      | Battery capacity        |
| thickness    | Mobile thickness        |

### Target Variable

| Target | Description             |
| ------ | ----------------------- |
| Price  | Mobile price prediction |

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Libraries & Frameworks

* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit

## Deployment Platforms

* GitHub
* Streamlit Cloud

---

# 📊 Exploratory Data Analysis (EDA)

The following analysis was performed during EDA:

* Dataset inspection
* Missing value analysis
* Duplicate value analysis
* Data type validation
* Statistical summary
* Correlation analysis
* Heatmap visualization
* Distribution analysis
* Skewness detection
* Outlier analysis

### Key Findings

* Strong positive correlation between:

  * RAM and Price
  * Internal Memory and Price
  * PPI and Price
  * Battery and Price

* Thickness showed a negative relationship with Price.

* Some variables were highly skewed and required transformation.

---

# 🔄 Data Preprocessing

The following preprocessing techniques were applied:

## ✅ Log Transformation

Log transformation (`log1p`) was applied to highly skewed columns:

* Sale
* weight
* internal mem
* battery

This helped improve normality and model performance.

---

## ✅ Feature Scaling

`StandardScaler` was used to standardize numerical features.

Feature scaling was necessary because:

* Regression models are sensitive to feature magnitudes
* Regularization techniques require scaling
* Coefficients become directly comparable after scaling

---

# 🤖 Machine Learning Models Used

The following regression algorithms were implemented and compared:

| Model                 | Purpose                   |
| --------------------- | ------------------------- |
| Linear Regression     | Baseline regression model |
| Ridge Regression      | L2 Regularization         |
| Lasso Regression      | L1 Regularization         |
| ElasticNet Regression | Combination of L1 & L2    |

---

# 📈 Model Evaluation Metrics

The models were evaluated using:

* R² Score
* Adjusted R² Score
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* MAPE (Mean Absolute Percentage Error)

---

# 🏆 Final Model Performance

| Model                 | Train R² | Test R² | Train RMSE | Test RMSE |
| --------------------- | -------- | ------- | ---------- | --------- |
| Linear Regression     | 0.9446   | 0.9382  | 180.99     | 187.21    |
| Ridge Regression      | 0.9445   | 0.9368  | 181.14     | 189.32    |
| Lasso Regression      | 0.9445   | 0.9376  | 181.10     | 188.04    |
| ElasticNet Regression | 0.9213   | 0.8944  | 215.71     | 244.69    |

---

# ✅ Best Performing Model

## ⭐ Linear Regression

Linear Regression achieved the best overall performance with:

* Highest Test R² Score
* Lowest Test RMSE
* Strong Generalization Performance
* Minimal Overfitting

Final deployed model:

```python
LinearRegression()
```

---

# 🧠 Feature Importance

The following features had the strongest influence on mobile price prediction:

### Positive Impact Features

* RAM
* Battery
* PPI
* Internal Memory
* CPU Core

### Negative Impact Features

* Thickness
* Weight

---

# 🌐 Streamlit Application Features

The deployed application includes:

✅ Professional User Interface
✅ Sidebar Input Controls
✅ Dropdown Selection Inputs
✅ Interactive Sliders
✅ Input Preview Table
✅ Real-Time Price Prediction
✅ Feature Importance Visualization
✅ Responsive Layout

---

# 📁 Project Structure

```text
mobile-price-prediction-streamlit/
│
├── app.py
├── mobile_price_model.pkl
├── scaler.pkl
├── feature_importance.csv
├── requirements.txt
├── README.md
├── Mobile_Price_Prediction.ipynb
└── dataset.csv
```

---

# ▶️ How to Run the Project Locally

## Step 1 — Clone Repository

```bash
git clone <your-github-repository-link>
```

---

## Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# ☁️ Cloud Deployment

This application was deployed using:

* GitHub
* Streamlit Cloud

Deployment workflow:

```text
Jupyter Notebook
        ↓
Model Training
        ↓
Model Serialization (.pkl)
        ↓
GitHub Repository
        ↓
Streamlit Cloud Deployment
```

---

# 📚 Key Learning Outcomes

This project helped strengthen understanding of:

* End-to-End Machine Learning Workflow
* Regression Modeling
* Regularization Techniques
* Feature Engineering
* Data Preprocessing
* Streamlit Deployment
* GitHub Version Control
* Cloud Deployment
* Model Evaluation
* ML Application Development

---

# 📸 Application Preview

*(Add screenshots of your Streamlit application here)*

---

# 🔮 Future Improvements

Potential future enhancements:

* Hyperparameter Tuning
* Advanced Regression Algorithms
* XGBoost Regressor
* Random Forest Regressor
* Cross Validation
* Automated ML Pipelines
* Docker Deployment
* CI/CD Integration
* Advanced Visual Analytics

---

# 👨‍💻 Author

## Nakul

Data Science & Machine Learning Enthusiast

---

# ⭐ If You Like This Project

Please consider giving this repository a star ⭐ on GitHub.
