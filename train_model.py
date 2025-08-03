import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('student_performance.csv')

# Encode categorical columns
label_encoders = {}
for col in ['sex', 'schoolsup', 'famsup']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Features and label
X = data[['sex', 'age', 'studytime', 'failures', 'schoolsup', 'famsup', 'absences', 'G1', 'G2']]
y = data['G3']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'encoders.pkl')

print("Linear Regression model and encoders saved.")
