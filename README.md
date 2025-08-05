<!-- # Linear-Regression

<img width="1885" height="914" alt="image" src="https://github.com/user-attachments/assets/f018ae0a-88db-462e-827e-67a8451a2892" />
<img width="1867" height="902" alt="image" src="https://github.com/user-attachments/assets/d35a82da-1f4a-4a4a-b2bf-a0b852059833" /> -->

## Final Grade Predictor – Linear Regression Model

This project uses a Linear Regression model to predict a student's final grade (G3) based on various personal, academic, and behavioral factors. A user-friendly Flask web app allows real-time prediction through a responsive web interface.

---

## Model

- Type: Linear Regression (sklearn.linear_model.LinearRegression)

- Target Variable: Final Grade (G3)

- Training Data: Cleaned and encoded from the student-mat.csv dataset

---

## Project Structure

```
Linear-Regression/
├── app.py                    # Flask application
├── train_model.py            # Model training script
├── model.pkl                 # Serialized Linear Regression model
├── encoders.pkl              # Label encoders for categorical inputs
├── student_data.csv          # Dataset used for training
│
├── templates/
│   └── index.html            # Web form to collect inputs
└── static/
    └── style.css             # Styling (if any)

```

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Linear-Regression.git
cd Linear-Regression
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:10000

## Screenshots

<img width="1885" height="914" alt="image" src="https://github.com/user-attachments/assets/f018ae0a-88db-462e-827e-67a8451a2892" />
<img width="1867" height="902" alt="image" src="https://github.com/user-attachments/assets/d35a82da-1f4a-4a4a-b2bf-a0b852059833" />

## Future Improvements

Display prediction error/confidence intervals

Visualize learning patterns

Add batch CSV prediction support

Integrate grade improvement suggestions
