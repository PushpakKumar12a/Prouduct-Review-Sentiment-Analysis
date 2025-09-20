document.getElementById('predictForm').onsubmit = async function(e) {
    e.preventDefault();
    const text = document.getElementById('text').value;
    const resultDiv = document.getElementById('result');

    resultDiv.textContent = 'Analyzing...';
    resultDiv.className = 'show';

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await response.json();

        if (response.ok) {
            if (data.prediction === 'positive') {
                resultDiv.textContent = 'Sentiment: Positive! 😄';
                resultDiv.className = 'show positive';
            } else if (data.prediction === 'negative') {
                resultDiv.textContent = 'Sentiment: Negative! 😠';
                resultDiv.className = 'show negative';
            } else {
                resultDiv.textContent = 'Prediction: ' + data.prediction;
            }
        } else {
            resultDiv.textContent = 'Error: ' + (data.error || 'Unknown error');
            resultDiv.className = 'show';
        }
    } catch (err) {
        resultDiv.textContent = 'Error: ' + err.message;
        resultDiv.className = 'show negative';
    }
};
