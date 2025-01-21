# ML_Project_Customer_Churn_Prediction_Model

This project predicts customer churn for a telecom company using machine learning techniques. The model predicts whether a customer will churn or not based on customer data. The project is built using Flask for creating a simple web application interface and a Logistic Regression model for prediction.

## Project Overview

The project uses a dataset from the telecom industry, which includes customer data such as contract type, tenure, internet service, etc. The goal is to predict if a customer will leave the company (churn) in the next month.

### Dataset Info

- **Each row represents a customer**, and each column contains customer attributes described in the column metadata.
- **Churn:** Customers who left within the last month. This is the target variable (1 = churned, 0 = not churned).

### Dataset Link

You can access the dataset on [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

---

## Getting Started

### Prerequisites

Make sure you have to install requirements.txt file


You can install them using pip:

```bash
pip install flask pandas numpy scikit-learn
```

### Project Structure

```
Customer_Churn_Prediction/
│
├── app.py                  # Main application file
├── Telco_Customer_Churn.csv # Dataset file
├── logistic_model.pkl      # Trained machine learning model
└── templates/
    └── index.html          # HTML template for the web app
```

---

## How to Run the Application

1. Clone or download the project to your local machine.
2. Navigate to the project directory.
3. Ensure that the `logistic_model.pkl` (trained model file) is correctly placed in the project directory or update the `model_path` in the `app.py` file.
4. Run the following command to start the Flask web application:

```bash
python app.py
```

5. Open a browser  to access the application.

---



### `app.py`

The main code for the Flask application. It includes:

- Loading the trained model using `pickle`.
- Preprocessing data (using `LabelEncoder` and `StandardScaler`).
- Receiving input data via a web form.
- Making a prediction using the Logistic Regression model.
- Displaying the result on the webpage.



## Model File

The model used in this project is a **Logistic Regression** model that has been trained on the Telco Customer Churn dataset. The trained model is saved in a `logistic_model.pkl` file, which is loaded during application runtime to make predictions.

---

## Conclusion

This project provides a simple yet effective implementation for predicting customer churn using machine learning. You can easily use this as a base for further development, such as adding more features, trying different machine learning models, or deploying it to a cloud service.

---

