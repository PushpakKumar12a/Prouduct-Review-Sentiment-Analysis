from flask import Flask, request, jsonify, render_template
import nltk
import pickle
import os
import re
from nltk.corpus import stopwords

nltk.download('stopwords')
app = Flask(__name__)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

model_path = 'model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    model = None

stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model file not found. Please add model.pkl.'}), 500
    data = request.get_json(force=True)
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided.'}), 400
    review_clean = clean_text(text)
    review_vec = vectorizer.transform([review_clean])
    pred = model.predict(review_vec)[0]
    

    if pred == 2:
        sentiment = 'positive'
    elif pred == 1:
        sentiment = 'neutral'
    else:  # pred == 0
        sentiment = 'negative'
    
    return jsonify({'prediction': sentiment})

if __name__ == '__main__':
    app.run(debug=True)

