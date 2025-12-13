from flask import Flask,request, jsonify, render_template
import pickle
import re
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

if not os.path.exists('nltk_data'):
    nltk.download('stopwords', download_dir='nltk_data')
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

stop_words = set(stopwords.words('english'))

# Remove negation words from stopwords as they're crucial for sentiment analysis
negation_words = {'not', 'no', 'never', 'none', 'nothing', 'neither', 'nobody', 
                  'nowhere', 'cannot', "can't", "won't", "shouldn't", "wouldn't", 
                  "couldn't", "doesn't", "don't", "didn't", "isn't", "aren't", 
                  "wasn't", "weren't", "hasn't", "haven't", "hadn't"}

# Create custom stopwords excluding negation words
custom_stop_words = stop_words - negation_words

stemmer = PorterStemmer()

def preprocess(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)
    tokens = text.split()
    # Use custom stopwords that preserve negation words
    tokens = [stemmer.stem(word) for word in tokens if word not in custom_stop_words]
    return ' '.join(tokens)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review', '')
    review_clean = preprocess(review)
    review_vec = vectorizer.transform([review_clean])
    prediction = model.predict(review_vec)[0]
    return jsonify({'sentiment': prediction})


if __name__ == '__main__':
    app.run()