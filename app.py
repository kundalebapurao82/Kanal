from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load the medicine data safely
file_path = os.path.join(os.path.dirname(__file__), "Medicine_Details_Final.csv")
df = pd.read_csv(file_path)

# Home route for Render
@app.route('/')
def home():
    return "Medicine API is running!"

# Define a route to get medicine details
@app.route('/medicine', methods=['GET'])
def get_medicine_info():
    medicine_name = request.args.get('name')

    if not medicine_name:
        return jsonify({"error": "Please provide a medicine name"}), 400

    # Search for the medicine (case-insensitive, avoid NaN errors)
    result = df[df['Medicine Name'].str.contains(medicine_name, case=False, na=False)]

    if result.empty:
        return jsonify({"error": "Medicine not found"}), 404

    return jsonify(result.to_dict(orient='records')[0])

# Run the Flask app with dynamic port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get Render's port
    app.run(host="0.0.0.0", port=port)
