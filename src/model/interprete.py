from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract and preprocess data as done during training
    # Example:
    # features = [data['year'], data['rolling_average'], ...]
    # X = pd.DataFrame([features], columns=...)
    # X_scaled = scaler.transform(X)
    # prediction = model.predict(X_scaled)
    # return jsonify({'prediction': prediction[0]})

    pass  # Implement based on your input format

if __name__ == '__main__':
    app.run(debug=True)
