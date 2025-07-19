from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return " Network Analyzer model is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    # Example input: {"features": [12, 34, 1, 400, 1234.5, 2]}
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
