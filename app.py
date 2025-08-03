from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
encoders = joblib.load('encoders.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            sex = request.form['sex']
            age = int(request.form['age'])
            studytime = float(request.form['studytime'])
            failures = int(request.form['failures'])
            schoolsup = request.form['schoolsup']
            famsup = request.form['famsup']
            absences = int(request.form['absences'])
            g1 = float(request.form['g1'])
            g2 = float(request.form['g2'])

            # Encode categorical values
            sex_enc = encoders['sex'].transform([sex])[0]
            schoolsup_enc = encoders['schoolsup'].transform([schoolsup])[0]
            famsup_enc = encoders['famsup'].transform([famsup])[0]

            # Make prediction
            features = [[sex_enc, age, studytime, failures, schoolsup_enc, famsup_enc, absences, g1, g2]]
            pred = model.predict(features)[0]
            prediction = round(pred, 2)

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
