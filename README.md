# 🏡 London House Price Prediction

## 📌 Project Overview
This project predicts London house prices using machine learning models. It applies data preprocessing, feature engineering, and regression algorithms to estimate property prices based on location and property attributes.

---

## 📊 Dataset Description
The dataset contains property listings with features such as:
- Property type
- Area (sq ft)
- Number of bedrooms, bathrooms, receptions
- Location (City/County, Postal Code)
- House price (target variable)

---

## ⚙️ Data Preprocessing
- Handled missing values using median/mode imputation
- Encoded categorical variables using One-Hot Encoding
- Feature engineering (Total Rooms, Price per Room)
- Train-test split (80/20)

---

## 🤖 Machine Learning Models Used
- Random Forest Regressor
- XGBoost Regressor

---

## 📈 Model Evaluation

| Model              | MAE (£) | RMSE (£) | R² Score |
|-------------------|--------|----------|----------|
| Random Forest     | 19343.504   | 51653.247     | 0.9967     |
| XGBoost          | 26347.520   | 49523.887    | 0.9970     |

👉 Best Model: **XGBoost**

---

## 🧠 Key Insights
- Location strongly impacts house price
- Area (sq ft) is the most important numerical feature
- Ensemble models outperform linear regression

---

## 🚀 Deployment
This project can be deployed using:
- Flask API
- Azure App Service
- Gunicorn web server

Startup command:
```bash
gunicorn app:app
```
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
XGBoost
Flask (deployment)
Azure (hosting)

📂 Project Structure
london-house-price-prediction/
│
├── app.py
├── model.pkl
├── notebook.ipynb
├── requirements.txt
├── README.md


📌 How to Run Locally
git clone https://github.com/vaheeson/london-house-price-prediction.git
cd london-house-price-prediction
pip install -r requirements.txt
python app.py

👨‍💻 Author
Vaheeson

Vaheeson Vasanthakumar
Data Science / Machine Learning Project
