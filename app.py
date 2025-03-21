from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the medicine data
df = pd.read_csv(r"C:\Users\Bapurao Anil Kundale\Desktop\PK\Medicine_Details_Final.csv")

# Define a route to get medicine details
@app.route('/medicine', methods=['GET'])
def get_medicine_info():
    medicine_name = request.args.get('name')
    
    if not medicine_name:
        return jsonify({"error": "Please provide a medicine name"}), 400

    # Search for the medicine
    result = df[df['Medicine Name'].str.lower() == medicine_name.lower()]
    
    if result.empty:
        return jsonify({"error": "Medicine not found"}), 404

    # Convert result to JSON
    return jsonify(result.to_dict(orient='records')[0])

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
