"""
app.py
------
Flask backend for the Student Performance Predictor.

Serves:
  GET  /                -> the frontend (static/index.html)
  POST /predict          -> JSON API: {"attendance": <0-100>, "marks": <0-100>}
                            returns predicted performance category + confidence

Run with:
    python app.py

Then open http://127.0.0.1:5000 in any browser.
"""

import os
import joblib
import numpy as np
from flask import Flask, request, jsonify, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "performance_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="")

# Load the trained model and scaler once at startup.
if not (os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH)):
    raise FileNotFoundError(
        "Model files not found. Run 'python train_model.py' first to train "
        "and save the model before starting the server."
    )

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Short human-readable advice shown alongside each prediction.
ADVICE = {
    "Excellent": "Outstanding work — keep up both attendance and study habits.",
    "Good": "Solid performance. A little more consistency could push this to Excellent.",
    "Average": "At risk of falling behind. Improving attendance and revision time is recommended.",
    "Poor": "Needs immediate attention — consider extra classes, tutoring, or counseling support.",
}


@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400

    try:
        attendance = float(data.get("attendance"))
        marks = float(data.get("marks"))
    except (TypeError, ValueError):
        return jsonify({"error": "'attendance' and 'marks' must be numbers."}), 400

    if not (0 <= attendance <= 100) or not (0 <= marks <= 100):
        return jsonify({"error": "'attendance' and 'marks' must be between 0 and 100."}), 400

    features = np.array([[attendance, marks]])
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    classes = model.classes_
    confidence = float(max(probabilities))

    prob_breakdown = {
        cls: round(float(prob) * 100, 2) for cls, prob in zip(classes, probabilities)
    }

    return jsonify({
        "prediction": prediction,
        "confidence_percent": round(confidence * 100, 2),
        "advice": ADVICE.get(prediction, ""),
        "probability_breakdown": prob_breakdown,
    })


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
