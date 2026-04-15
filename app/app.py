from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('../model/model.pkl', 'rb'))

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

if __name__ == "__main__":
    app.run(debug=True)