import pickle
from pathlib import Path

MODEL_PATH = Path("model/sentiment_model.pkl")

class SentimentModel:
    def __init__(self):
        with open(MODEL_PATH, "rb") as f:
            self.pipeline = pickle.load(f)

    def predict(self, text: str) -> str:
        prediction = self.pipeline.predict([text])[0]
        return "Positive" if prediction == 1 else "Negative"

