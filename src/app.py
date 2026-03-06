from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

# -----------------------------
# Swagger UI Configuration
# -----------------------------
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
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "swagger_ui_config": {
        "docExpansion": "list",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "filter": True
    }
}

# -----------------------------
# Swagger Template (Branding)
# -----------------------------
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask DevOps Demo API",
        "description": """
        Production-ready **Flask API** demonstrating:

        ✔ Docker containerization  
        ✔ CI/CD pipeline integration  
        ✔ Azure Container Apps deployment  
        ✔ Interactive Swagger documentation  

        This project is part of a **DevOps portfolio demonstration**.
        """,
        "version": "1.0.0",
        "contact": {
            "name": "API Support Team"
        }
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "tags": [
        {
            "name": "Home",
            "description": "Main application endpoints"
        },
        {
            "name": "Health",
            "description": "Service monitoring endpoints"
        }
    ]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

# -----------------------------
# Custom Dark Theme CSS
# -----------------------------
@app.route("/swagger-dark.css")
def swagger_dark():
    return """
    body { background-color: #0f172a; color: #e2e8f0; }
    .topbar { background-color: #020617 !important; }
    .swagger-ui .info h2 { color: #38bdf8; }
    .swagger-ui .scheme-container { background: #020617; }
    """


# -----------------------------
# Home Endpoint
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home Endpoint
    ---
    tags:
      - Home
    description: |
      Root endpoint of the API.

      • **GET** returns a welcome message  
      • **POST** echoes back JSON payload
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
            message:
              type: string
              example: Hello API
    responses:
      200:
        description: Successful response
        schema:
          type: object
          properties:
            message:
              type: string
    """

    if request.method == "GET":
        return jsonify({"message": "Hello from Flask API with CI/CD!"})

    if request.method == "POST":
        data = request.json
        return jsonify({
            "message": "POST request received",
            "your_data": data
        })


# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    """
    Health Check Endpoint
    ---
    tags:
      - Health
    description: Returns API health status used by monitoring tools.
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


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
