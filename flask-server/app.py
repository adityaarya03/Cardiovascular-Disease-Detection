from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load models and scaler
models = {
    "decision_tree": joblib.load("models/decision_tree_model.pkl"),
    "random_forest": joblib.load("models/random_forest_model.pkl"),
    "knn": joblib.load("models/knn_model.pkl"),
    "adaboost": joblib.load("models/adaboost_model.pkl"),
    "gradient_boosting": joblib.load("models/gradient_boosting_model.pkl")
}
scaler = joblib.load("models/scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Use keys without underscores
    required_keys = [
        'age', 'gender', 'chestpain', 'restingBP', 'serumcholestrol',
        'fastingbloodsugar', 'restingrelectro', 'maxheartrate', 'exerciseangia',
        'oldpeak', 'slope', 'noofmajorvessels'
    ]
    
    # Check for missing keys
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return jsonify({"error": f"Missing keys in request data: {missing_keys}"}), 400

    # Prepare features in correct order
    features = np.array([data[key] for key in required_keys]).reshape(1, -1)

    # Scale features
    features_scaled = scaler.transform(features)

    # Predict using each model and convert to int
    predictions = {model_name: int(model.predict(features_scaled)[0]) for model_name, model in models.items()}
    return jsonify(predictions)


if __name__ == '__main__':
    app.run(debug=True)
