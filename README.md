# 💳 Credit Card Fraud Detection
A machine learning web app to detect fraudulent credit card transactions using Random Forest and Decision Tree models.

## 🚀 Features
🔍 Real-time fraud prediction

📊 Model comparison: Random Forest vs Decision Tree

⚖️ SMOTE for handling class imbalance

🎨 Dark-themed, responsive web UI

🧪 Built-in test samples (fraud & legitimate)

📈 Precision, Recall, F1-Score, Confusion Matrix

## 🛠️ Tech Stack
Backend: Python, Flask, scikit-learn

Frontend: HTML, CSS, JavaScript

ML Tools: SMOTE, joblib, matplotlib, pandas

## 📦 Project Structure
```bash

├── app.py                 # Flask web app

├── train_model.py         # Model training

├── templates/index.html   # Web UI

├── static/                # Confusion matrix images

├── rf_model.pkl           # Random Forest model

├── dt_model.pkl           # Decision Tree model

├── dataset.csv            # Transaction data

└── requirements.txt       # Python dependencies
```

## ⚙️ Quick Start
```
# Clone repo
git clone https://github.com/tejasnaik/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# Set up environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Train models
python train_model.py

# Run the app
python app.py
```
#### Visit: http://127.0.0.1:5000

##📈 Model Metrics
Metric	Description

Accuracy	Overall correctness

Precision	% of predicted frauds that were true

Recall	% of actual frauds detected

F1-Score	Balance between precision & recall

Confusion Matrix	Visual performance check

## 📷 Screenshots
Add screenshots here (UI, prediction results, metrics, etc.)

## 👨‍💻 Author
Tejas M Naik

AI/ML Engineering Student, DLithe Consultancy

GitHub: @naiktejas

## 📝 License
Licensed under the MIT License

