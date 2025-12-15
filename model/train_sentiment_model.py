import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from pathlib import Path

# Sample training data
data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Very happy with the service",
        "I hate this experience",
        "This is terrible",
        "Very disappointed with the product"
    ],
    "sentiment": [1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df["text"]
y = df["sentiment"]

# NLP + ML pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

pipeline.fit(X, y)

MODEL_PATH = Path("model/sentiment_model.pkl")
with open(MODEL_PATH, "wb") as f:
    pickle.dump(pipeline, f)

print("Sentiment model trained and saved successfully")
