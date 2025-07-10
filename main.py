from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
STATUS_FILE = "status.json"

@app.route('/')
def home():
    return "🟢 Shorts Control Server aktif", 200

@app.route('/status', methods=["GET", "POST"])
def status():
    if request.method == "POST":
        data = request.get_json()
        if "status" in data:
            with open(STATUS_FILE, "w") as f:
                json.dump({"status": data["status"]}, f)
            return jsonify({"message": f"Status updated to {data['status']}"})
        return jsonify({"error": "Missing 'status' field"}), 400

    # GET method
    if not os.path.exists(STATUS_FILE):
        return jsonify({"status": "OFF"})
    with open(STATUS_FILE, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
