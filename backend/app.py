from flask import Flask, request, jsonify
from flask_cors import CORS

from services.metrics import calculate_metrics
from services.report_generator import generate_report

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "EvalBoard API is running"})


@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()

    required_fields = [
        "true_positive",
        "false_positive",
        "false_negative",
        "true_negative",
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    metrics = calculate_metrics(
        data["true_positive"],
        data["false_positive"],
        data["false_negative"],
        data["true_negative"],
    )

    report = generate_report(metrics)

    return jsonify({
        "project_name": data.get("project_name", "Untitled Project"),
        "metrics": metrics,
        "report": report,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    