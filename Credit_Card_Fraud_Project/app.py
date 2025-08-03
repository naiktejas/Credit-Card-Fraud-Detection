from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

app = Flask(__name__)

# Load models and test data
rf_model = joblib.load("rf_model.pkl")
dt_model = joblib.load("dt_model.pkl")
features = ['Amount', 'MerchantID', 'TransactionType', 'Location']
X_test, y_test = joblib.load("test_data.pkl")

# Available options
transaction_types = ['purchase', 'refund']
locations = list(X_test['Location'].unique())

@app.route("/")
def home():
    return render_template("index.html",
                           features=features,
                           transaction_types=transaction_types,
                           locations=locations,
                           preset={})

@app.route("/sample/<label>")
def sample(label):
    label_int = 1 if label == "fraud" else 0
    sample_row = X_test[y_test == label_int].iloc[0]
    sample_dict = sample_row.to_dict()

    return render_template("index.html",
                           features=features,
                           transaction_types=transaction_types,
                           locations=locations,
                           preset=sample_dict)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        model_choice = request.form["model"]
        model = rf_model if model_choice == "RandomForest" else dt_model
        graph_path = f"static/{'rf' if model_choice == 'RandomForest' else 'dt'}_conf_matrix.png"

        input_data = {
            'Amount': float(request.form['Amount']),
            'MerchantID': int(request.form['MerchantID']),
            'TransactionType': request.form['TransactionType'],
            'Location': request.form['Location']
        }

        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        result = "⚠️ FRAUDULENT" if prediction == 1 else "✅ LEGITIMATE"
        confidence = f"{prob*100:.2f}%" if prediction == 1 else f"{(1 - prob)*100:.2f}%"

        preds = model.predict(X_test)
        report = classification_report(y_test, preds, output_dict=True)
        accuracy = accuracy_score(y_test, preds)
        metrics = {
            "Accuracy": f"{accuracy * 100:.2f}%",
            "Precision (Fraud)": f"{report['1']['precision']:.4f}",
            "Recall (Fraud)": f"{report['1']['recall']:.4f}",
            "F1-Score (Fraud)": f"{report['1']['f1-score']:.4f}"
        }

        return render_template("index.html",
                               features=features,
                               transaction_types=transaction_types,
                               locations=locations,
                               selected_model=model_choice,
                               result=result,
                               confidence=confidence,
                               metrics=metrics,
                               graph_path=graph_path,
                               preset=input_data)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
