document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('review-form');
    const reviewInput = document.getElementById('review-input');
    const resultDiv = document.getElementById('result');
    const predictBtn = document.querySelector('.btn');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const review = reviewInput.value.trim();

        if (!review) {
            resultDiv.textContent = 'Please enter a review.';
            resultDiv.style.color = '#B71C1C';
            return;
        }

        predictBtn.textContent = 'Predicting...';
        predictBtn.disabled = true;
        resultDiv.textContent = '';
        resultDiv.style.color = '';

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ review })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            let emoji = '';
            let color = '';
            let bg = '';
            const sentiment = data.sentiment.toLowerCase();
            if (sentiment === 'positive') {
                emoji = '😊';
                color = '#43A047'; // Green for positive
                bg = '#e8f5e9'; // Light green
            } else if (sentiment === 'negative') {
                emoji = '😞';
                color = '#B71C1C'; // Dark Red for negative
                bg = '#ffebee'; // Light red
            } else {
                emoji = '😐';
                color = '#757575'; // Grey for neutral
                bg = '#ede9fe'; // Light lavender/neutral
            }
            resultDiv.textContent = `Predicted Sentiment: ${data.sentiment} ${emoji}`;
            resultDiv.style.color = color;
            resultDiv.style.background = bg;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.textContent = 'Error predicting sentiment. Please try again.';
            resultDiv.style.color = '#B71C1C';
        })
        .finally(() => {
            predictBtn.textContent = 'Predict Sentiment';
            predictBtn.disabled = false;
        });
    });
});