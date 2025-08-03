💳 Credit Card Fraud Detection System
A comprehensive machine learning project that detects fraudulent credit card transactions using Random Forest and Decision Tree algorithms with an interactive web interface.

📋 Table of Contents
✨ Features

🛠️ Technology Stack

📊 Project Structure

🚀 Quick Start

💡 Usage

📈 Model Performance

🖼️ Screenshots

🚀 Deployment

🤝 Contributing

📝 License

👨‍💻 Author

🙏 Acknowledgments

🔮 Future Enhancements

✨ Features
🔍 Real-time Detection	🤖 Multiple ML Models
- Instant fraud classification	- Random Forest Classifier
- Confidence score analysis	- Decision Tree Classifier
- Sub-second response time	- Performance comparison

🎨 Interactive Web UI	⚖️ Class Balance Handling
- Modern dark theme interface	- SMOTE implementation
- Responsive design	- Synthetic sample generation
- User-friendly controls	- Imbalanced data optimization

📊 Comprehensive Metrics	🧪 Sample Data Testing
- Precision, Recall, F1-Score	- Pre-loaded examples
- Confusion matrix visualization	- Legitimate & fraud samples
- Model performance dashboard	- Quick testing features

🛠️ Technology Stack
<details open> <summary><strong>Backend</strong></summary>
Python 3.8+

Flask 2.0+

scikit-learn 1.0+

pandas 1.5+

numpy 1.24+

</details> <details> <summary><strong>Frontend</strong></summary>
HTML

CSS

JavaScript

</details> <details> <summary><strong>ML & Data Science</strong></summary>
imbalanced-learn (SMOTE)

matplotlib

joblib

ColumnTransformer

Pipeline

</details>
📊 Project Structure
csharp
Copy
Edit
📦 Credit-Card-Fraud-Detection/
├── app.py                         # Flask web application
├── train_model.py                 # Model training script
├── balanced_credit_card_fraud_dataset.csv
├── requirements.txt
├── templates/
│   └── index.html                 # Web interface
├── static/
│   ├── rf_conf_matrix.png
│   └── dt_conf_matrix.png
├── rf_model.pkl
├── dt_model.pkl
├── test_data.pkl
├── model_features.pkl
└── README.md
🚀 Quick Start
📋 Prerequisites
Make sure you have Python 3.8+ and Git installed.

⚡ Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/tejasnaik/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train models
python train_model.py

# Run the application
python app.py
🌐 Access the App
Open your browser and go to:
http://127.0.0.1:5000

💡 Usage
Step-by-Step
Choose Model: Random Forest or Decision Tree

Input Transaction:

Amount

Merchant ID

Transaction Type (Purchase/Refund)

Location

Predict: Click "Predict"

Results: View prediction, confidence, and metrics

📈 Model Performance
📊 Dataset Features
Feature	Type	Description	Example
Amount	Numerical	Transaction value	$1,299.99
MerchantID	Numerical	Unique merchant identifier	12345
TransactionType	Categorical	Purchase or Refund	Refund
Location	Categorical	Geographic location	New York

🔄 ML Pipeline
nginx
Copy
Edit
Raw Data → Preprocessing → Feature Engineering → SMOTE → Training → Evaluation → Deployment
⚖️ Model Comparison
Model	Accuracy	Speed	Interpretability	Best For
Random Forest	High	Medium	Medium	Production
Decision Tree	Good	Fast	High	Analysis

📊 Evaluation Metrics
Accuracy: Overall correctness

Precision: Correct fraud predictions

Recall: Caught fraud cases

F1-Score: Balance between precision & recall

Confusion Matrix: Visual performance

🖼️ Screenshots
<details> <summary><strong>Click to Expand</strong></summary>
UI View	Fraud Detection Result	Performance Metrics View
Add screenshots here	Add screenshots here	Add screenshots here

</details>
🚀 Deployment
🏠 Local
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000

🌐 Heroku (Optional)
bash
Copy
Edit
echo "web: python app.py" > Procfile
heroku create your-app-name
git push heroku main
🐳 Docker
Dockerfile:

dockerfile
Copy
Edit
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
Build and Run:

bash
Copy
Edit
docker build -t fraud-detection .
docker run -p 5000:5000 fraud-detection
🤝 Contributing
We welcome contributions!
Please fork the repo and submit a pull request.

Example
bash
Copy
Edit
# Fork and clone
git clone https://github.com/your-username/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# Create a branch
git checkout -b feature/new-feature

# Commit and push
git commit -m "Add new feature"
git push origin feature/new-feature
Contribution Ideas
🐛 Bug fixes

✨ New features

📚 Documentation updates

🧪 Test cases

🎨 UI improvements

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Tejas M Naik
AI/ML Engineering Student
DLithe Consultancy Services Pvt. Ltd.
Registration: NNM23CS513

🙏 Acknowledgments
DLithe Consultancy – Internship opportunity

Ms. Archana / Ms. Sushma – Mentorship

scikit-learn & Flask – Core technologies

Open-source community – Inspiration

🔮 Future Enhancements
🧠 Advanced Models: XGBoost, LSTM

🔄 Real-time APIs

📱 Mobile App interface (React Native)

⚙️ AutoML Integration

📊 Time-series Analysis

🔍 Explainable AI (LIME / SHAP)

☁️ Cloud Deployment: AWS / GCP

📧 Alert System (Email / SMS)

<div align="center"> ⭐ If you found this project helpful, please give it a star! Made with ❤️ by Tejas M Naik </div>
