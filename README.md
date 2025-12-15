# Real-Time Sentiment Analysis Web Application

## Overview
This project implements a real-time sentiment analysis web application that classifies user input text as Positive or Negative using a machine learning model. The system integrates a Flask-based backend API with a lightweight frontend interface to deliver instant sentiment predictions.


## Problem Statement
Understanding customer sentiment in real time is critical for many applications such as customer feedback analysis, social media monitoring, and product reviews. Manual sentiment evaluation is inefficient and does not scale. This project demonstrates how machine learning can be integrated into a web application to provide instant sentiment insights.


## Solution Architecture
The application follows a modular, end-to-end architecture:
**1. Model Training** – A classical NLP pipeline using TF-IDF and Logistic Regression is trained and persisted.
**2. Backend API** – A Flask service loads the trained model and exposes a /predict endpoint for real-time inference.
**3. Frontend UI** – A simple HTML and JavaScript interface captures user input and displays sentiment results instantly.
**4. Integration Layer** – The frontend communicates with the backend via REST APIs.


## Technologies Used
• Programming Language: Python
• Machine Learning: Scikit-learn (TF-IDF, Logistic Regression)
• Backend Framework: Flask
• Frontend: HTML, JavaScript
• Data Handling: Pandas, NumPy
• Version Control: Git, GitHub


## Project Structure
real-time-sentiment-analysis/
├── backend/
│   ├── app.py              # Flask backend API
│   └── model.py            # Sentiment model loading and inference
├── frontend/
│   ├── index.html          # Web UI
│   └── script.js           # Frontend logic
├── model/
│   ├── train_sentiment_model.py
│   └── sentiment_model.pkl
├── requirements.txt
└── README.md


## API Endpoints
### Health Check
#### GET /health
Response:
{
  "status": "Sentiment API is running"
}

## Sentiment Prediction
### POST /predict
Request Body:
{
  "text": "I really like this product"
}
Response:
{
  "text": "I really like this product",
  "sentiment": "Positive"
}

## Running the Application (Local)
1. Install dependencies:
pip install -r requirements.txt
2. Start the backend:
python backend/app.py
3. Open the frontend:
   • Open frontend/index.html in a browser
4. Enter text and view sentiment predictions in real time.

   
## Key Features
• Real-time sentiment classification
• Clean separation of ML, backend, and frontend layers
• Input validation and error handling
• Lightweight and extensible architecture


## Future Enhancements
• Multi-class sentiment classification
• Model performance evaluation and monitoring
• UI enhancements and styling
• Containerisation and cloud deployment


## Author
### Nissiya Thomas
MSc Advanced Computer Science – University of Liverpool
