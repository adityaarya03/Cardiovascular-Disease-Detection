from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load models
models = {
    "decision_tree": joblib.load("models/decision_tree_model.pkl"),
    "random_forest": joblib.load("models/random_forest_model.pkl"),
    "knn": joblib.load("models/knn_model.pkl"),
    "adaboost": joblib.load("models/adaboost_model.pkl"),
    "gradient_boosting": joblib.load("models/gradient_boosting_model.pkl")
}

# Load scaler
scaler = joblib.load("models/scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Ensure all expected keys are present in the received data
    required_keys = [
        'age', 'gender', 'chestpain', 'restingBP', 'serumcholestrol',
        'fastingbloodsugar', 'restingrelectro', 'maxheartrate',
        'exerciseangia', 'oldpeak', 'slope', 'noofmajorvessels'
    ]
    
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return jsonify({"error": f"Missing keys in request data: {missing_keys}"}), 400

    # Convert data into the required format for the model
    features = np.array([
        data['age'],
        data['gender'],
        data['chestpain'],
        data['restingBP'],
        data['serumcholestrol'],
        data['fastingbloodsugar'],
        data['restingrelectro'],
        data['maxheartrate'],
        data['exerciseangia'],
        data['oldpeak'],
        data['slope'],
        data['noofmajorvessels']
    ]).reshape(1, -1)

    # Scale features
    features_scaled = scaler.transform(features)

    # Get predictions from each model
    predictions = {model_name: model.predict(features_scaled)[0] for model_name, model in models.items()}

    return jsonify(predictions)


if __name__ == '__main__':
    app.run(debug=True)
