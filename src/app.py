from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":
        return jsonify({"message": "Hello from Flask API with CI/CD!"})

    if request.method == "POST":
        data = request.json
        return jsonify({
            "message": "POST request received",
            "your_data": data
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
