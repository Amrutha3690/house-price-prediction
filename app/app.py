from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('app/model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    prediction = model.predict([[area, bedrooms, bathrooms]])

    return render_template('index.html', prediction_text=f'Price: {prediction[0]}')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)