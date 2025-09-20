from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    """API root to test response"""
    return jsonify({"message": "Hello, World!"})


@app.route("/echo", methods=["POST"])
def echo():
    """Echoes back the message sent in the request body"""
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    message = data["message"]
    return jsonify({"message": message})


if __name__ == "__main__":
    app.run(debug=True)
