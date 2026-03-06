from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

# Swagger configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "swagger",
            "route": "/swagger.json",   # clean spec URL
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

# Swagger template
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask DevOps Demo API",
        "description": "Sample Flask API deployed using Docker and Azure Container Apps with CI/CD.",
        "version": "1.0.0",
        "contact": {
            "name": "API Support"
        }
    }
}

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
    """

    return jsonify({
        "status": "healthy",
        "service": "flask-api",
        "message": "API is running"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
