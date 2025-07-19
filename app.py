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

        # Ensure all 6 features are included
        features = [
            data["Source"],
            data["Destination"],
            data["Protocol"],
            data["Length"],
            data["Src_Dst_Interaction"],
            data["Length_Category"]
        ]

        # Convert to proper format for prediction
        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})
