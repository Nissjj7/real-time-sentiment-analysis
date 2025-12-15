from flask import Flask, request, jsonify
from backend.model import SentimentModel
import logging

app = Flask(__name__)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load sentiment model once at startup
model = SentimentModel()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Sentiment API is running"}), 200


@app.route("/predict", methods=["POST"])
def predict_sentiment():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify(
                {"error": "Invalid input. Expected JSON with 'text' field."}
            ), 400

        text = data["text"]

        if not isinstance(text, str) or not text.strip():
            return jsonify(
                {"error": "Text must be a non-empty string."}
            ), 400

        sentiment = model.predict(text)

        logger.info("Sentiment prediction generated successfully")

        return jsonify(
            {
                "text": text,
                "sentiment": sentiment
            }
        ), 200

    except Exception:
        logger.error("Error during sentiment prediction", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

