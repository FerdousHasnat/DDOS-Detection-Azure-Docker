from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Initialize the model
model = None

@app.before_first_request
def init():
    global model
    try:
        model_path = "random_forest_ddos_model.pkl"  # Ensure the correct model path
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}")
    except Exception as e:
        print(f"Error during model loading: {e}")
        raise e

# Define the /score route
@app.route('/score', methods=['POST'])
def score():
    try:
        # Parse input data
        input_data = request.get_json()
        print(f"Received input data: {input_data}")
        input_df = pd.DataFrame(input_data)
        print(f"Input DataFrame: {input_df}")

        # Generate predictions
        predictions = model.predict(input_df)
        response = {"predictions": predictions.tolist()}
        return jsonify(response)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
