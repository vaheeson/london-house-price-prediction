from flask import Flask
import joblib

app = Flask(__name__)

model = joblib.load(
"housing_price_model.pkl"
)

@app.route("/")
def home():
    return "Housing Prediction API Running"

app.run()