from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "✅ Network Analyzer API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Replace these with actual feature names used in training
        features = [
            data["duration"],
            data["protocol_type"],
            data["src_bytes"],
            data["dst_bytes"]
        ]

        prediction = model.predict([features])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})
