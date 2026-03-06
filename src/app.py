from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

# Swagger Configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "swagger",
            "route": "/swagger.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "swagger_ui": True,
    "specs_route": "/docs/",
    "swagger_ui_config": {
        "url": "/swagger.json"
    }
}

# Swagger Template
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask DevOps Demo API",
        "description": "A sample Flask API with Swagger documentation for CI/CD, Docker, and Azure Container Apps deployment.",
        "version": "1.0.0",
        "contact": {
            "name": "API Support"
        }
    }
}

# Initialize Swagger
swagger = Swagger(app, config=swagger_config, template=swagger_template)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home Endpoint
    ---
    tags:
      - Home
    description: Returns greeting message or echoes POST data.
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
