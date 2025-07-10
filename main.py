from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)
STATUS_FILE = "status.json"

@app.route("/")
def home():
    return "✅ Bot Status Controller Active"

@app.route("/status", methods=["GET", "POST"])
def status():
    if request.method == "POST":
        data = request.get_json()
        if "status" in data:
            with open(STATUS_FILE, "w") as f:
                json.dump({"status": data["status"]}, f)
            return jsonify({"message": "Status updated", "status": data["status"]})
        else:
            return jsonify({"error": "Missing 'status' field"}), 400

    else:
        if not os.path.exists(STATUS_FILE):
            return jsonify({"status": "OFF"})
        with open(STATUS_FILE) as f:
            data = json.load(f)
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
