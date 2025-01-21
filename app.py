# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder, StandardScaler

label_encoder = LabelEncoder()
scaler = StandardScaler()

# model = pickle.load(open('logistic_model.pkl','rb'))
df = pd.read_csv("Telco_Customer_Churn.csv")

# Load the trained model
model_path = 'D:\Customer_Attrition_Project_Machine_Learning\logistic_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)


# df = pd.read_csv("Telco_Customer_Churn.csv.csv")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    output = 'Churn' if prediction[0] == 1 else 'Not Churn'

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)