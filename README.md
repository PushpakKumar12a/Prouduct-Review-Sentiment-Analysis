# Sentiment Analysis Flask App

A simple web application for sentiment analysis using Flask, scikit-learn, and NLTK.
The app loads a pre-trained Naive Bayes classifier along with a vectorizer to predict the sentiment (positive / negative / neutral) of user input text.

## Features
- Web interface for sentiment prediction
- REST API endpoint for predictions
- Text preprocessing with NLTK stopwords

## Requirements
- Python 3.x
- Flask
- scikit-learn
- nltk

## Setup Instructions
1. **Clone the repository or copy the project files.**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Download NLTK stopwords:**
   Run the following in Python before starting the app:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.donload('punkt')
   ```
   Or add these lines to the top of `app.py` if not already present.
4. **Ensure `model.pkl` and `vectorizer.pkl` are present in the project directory.**

## Usage
- Start the Flask app:
  ```
  python app.py
  ```
- Open your browser and go to `http://127.0.0.1:5000/` to use the web interface.
- Use the `/predict` endpoint for API requests (POST JSON with a `text` field).

## Deployment Notes
- For production, use a WSGI server (e.g., Gunicorn or Waitress).
- Set `debug=False` in `app.py` for production.
- Make sure all required files (`model.pkl`, `vectorizer.pkl`) are included.

## Project Structure
```
app.py
model.pkl
vectorizer.pkl
requirements.txt
static/
    script.js
    style.css
    github.svg
templates/
    index.html
```
