from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

# Swagger Configuration
swagger = Swagger(app)

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home Endpoint
    ---
    tags:
      - Home
    parameters:
      - name: body
        in: body
        schema:
          type: object
          properties:
            name:
              type: string
              example: Vikas
    responses:
      200:
        description: Successful response
    """

    if request.method == "GET":
        return jsonify({"message": "Hello from Flask API with CI/CD!"})

    if request.method == "POST":
        data = request.json
        return jsonify({
            "message": "POST request received",
            "your_data": data
        })


@app.route("/health", methods=["GET"])
def health():
    """
    Health Check Endpoint
    ---
    tags:
      - Health
    responses:
      200:
        description: API Health Status
        schema:
          type: object
          properties:
            status:
              type: string
              example: healthy
            service:
              type: string
              example: flask-api
            message:
              type: string
              example: API is running
    """

    return jsonify({
        "status": "healthy",
        "service": "flask-api",
        "message": "API is running"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
