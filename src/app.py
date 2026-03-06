from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

# Swagger configuration (default stable config)
app.config["SWAGGER"] = {
    "title": "Flask DevOps Demo API",
    "description": "Sample Flask API deployed using Docker and Azure Container Apps with CI/CD.",
    "version": "1.0.0",
    "uiversion": 3
}

swagger = Swagger(app)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home Endpoint
    ---
    tags:
      - Home
    description: Returns greeting message or echoes POST data.
    parameters:
      - in: body
        name: body
        required: false
        schema:
          type: object
          properties:
            name:
              type: string
              example: Vikas
    responses:
      200:
        description: Successful response
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello from Flask API with CI/CD!
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
    description: Check API health status
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
