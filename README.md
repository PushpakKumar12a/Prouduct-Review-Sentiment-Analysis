# Product Review Sentiment Analysis

A Flask web app for sentiment analysis of product reviews using scikit-learn and NLTK. The app exposes a `/predict` API and a simple UI in `templates/index.html` that calls it.

## Features
- Web UI for entering a review and viewing sentiment.
- `/predict` REST endpoint returning JSON sentiment.
- Custom NLTK preprocessing preserving negations (e.g., "not").
- CORS enabled for browser access.

## Requirements
- Python 3.8+
- `Flask`, `flask-cors`, `scikit-learn`, `nltk`

Install via `requirements.txt`.

## Project Structure
```
requirements.txt
templates/
  index.html
static/
  script.js
  style.css
  github.svg (if referenced)
app.py
model.pkl
vectorizer.pkl
```

## Setup (Windows PowerShell)
```powershell
cd d:\Data_Science\Ibm_project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Download required NLTK data (the app calls `nltk.download`, but you can prefetch):
```powershell
python - << 'PY'
import nltk
nltk.download('stopwords')
nltk.download('punkt')
PY
```

Place trained artifacts in the project root:
- `model.pkl` — trained classifier
- `vectorizer.pkl` — fitted vectorizer

## Run
```python app.py
```

## API
- URL: `POST /predict`
- Request JSON: `{ "review": "Your review text" }`
- Response JSON: `{ "sentiment": "positive" | "negative" | "neutral" }`

## Frontend Behavior
- `static/script.js` sends the review to `/predict` and displays the result with emoji and color cues.
- `static/style.css` styles the form and result.

## Notes
- CORS is enabled via `flask-cors`.
- Negation words are excluded from stopwords to improve sentiment accuracy.
- Ensure `model.pkl` and `vectorizer.pkl` exist before starting the app.
