from flask import Flask, jsonify, request
from calculator import calculate, build_error_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Calculator API is running.",
        "usage": "POST /calculate with JSON {\"operation\": \"add\", \"a\": 1, \"b\": 2}"
    })


@app.route("/calculate", methods=["POST"])
def calculate_route():
    payload = request.get_json(silent=True)
    if not payload or not isinstance(payload, dict):
        return jsonify(build_error_response("Request body must be valid JSON.")), 400

    operation = payload.get("operation")
    if not operation or not isinstance(operation, str):
        return jsonify(build_error_response("operation must be a non-empty string.")), 400

    if "a" not in payload or "b" not in payload:
        return jsonify(build_error_response("Both a and b are required.")), 400

    try:
        result = calculate(operation, payload["a"], payload["b"])
    except ValueError as exc:
        return jsonify(build_error_response(str(exc))), 400

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
