# 💳 Credit Card Fraud Detection System
A comprehensive machine learning project that detects fraudulent credit card transactions using Random Forest and Decision Tree algorithms with an interactive web interface.


## 🚀 Features

Real-time Fraud Detection: Instant transaction classification with confidence scores
Multiple ML Models: Compare Random Forest and Decision Tree performance
Interactive Web Interface: User-friendly Flask application with modern UI
Class Balance Handling: SMOTE implementation for imbalanced datasets
Comprehensive Evaluation: Detailed metrics and confusion matrix visualization
Sample Data Loading: Quick testing with pre-loaded fraud/legitimate examples


## 🛠️ Technology Stack

Backend: Python, Flask
Machine Learning: scikit-learn, imbalanced-learn
Data Processing: pandas, NumPy
Visualization: Matplotlib
Frontend: HTML, CSS, JavaScript
Model Persistence: joblib

## 📊 Project Structure
Credit-Card-Fraud-Detection/
├── app.py                                    # Flask web application

├── train_model.py                           # ML model training script

├── balanced_credit_card_fraud_dataset.csv  # Dataset

├── requirements.txt                         # Python dependencies

├── templates/

│   └── index.html                          # Web interface template

├── static/                                 # Static files (CSS, images)

│   ├── rf_conf_matrix.png                 # Random Forest confusion matrix

│   └── dt_conf_matrix.png                 # Decision Tree confusion matrix

├── .ipynb_checkpoints/                     # Jupyter notebook checkpoints

├── models/                                 # Trained model files

│   ├── rf_model.pkl                       # Random Forest model

│   ├── dt_model.pkl                       # Decision Tree model

│   ├── test_data.pkl                      # Test dataset

│   └── model_features.pkl                 # Feature list

└── README.md                              # Project documentation


## 🔧 Installation & Setup
Prerequisites

Python 3.8 or higher
pip package manager

1. Clone the Repository
bashgit clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection
2. Create Virtual Environment (Recommended)
bashpython -m venv fraud_detection_env
source fraud_detection_env/bin/activate  # On Windows: fraud_detection_env\Scripts\activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Train the Models
bashpython train_model.py
5. Run the Web Application
bashpython app.py
Visit http://127.0.0.1:5000 in your browser to access the application.
📋 Requirements
Create a requirements.txt file with the following dependencies:
Flask==2.3.3
pandas==2.0.3
scikit-learn==1.3.0
imbalanced-learn==0.11.0
matplotlib==3.7.2
joblib==1.3.2
numpy==1.24.3
💡 Usage
Web Interface

Select Model: Choose between Random Forest or Decision Tree
Input Transaction Details:

Amount: Transaction value
Merchant ID: Unique merchant identifier
Transaction Type: Purchase or Refund
Location: Transaction location


Get Prediction: Click "Predict" to get fraud classification
View Results: See prediction, confidence score, and model metrics

Sample Data

Click "🟢 Load Legit Sample" for legitimate transaction example
Click "🔴 Load Fraud Sample" for fraudulent transaction example

Model Training
bashpython train_model.py
This script will:

Load and preprocess the dataset
Handle class imbalance using SMOTE
Train Random Forest and Decision Tree models
Generate confusion matrices
Save trained models for deployment

📈 Model Performance
Dataset Features

Amount: Transaction value (numerical)
MerchantID: Merchant identifier (numerical)
TransactionType: Purchase/Refund (categorical)
Location: Geographic location (categorical)

Preprocessing Pipeline

Numerical Features: StandardScaler normalization
Categorical Features: One-Hot Encoding
Class Imbalance: SMOTE oversampling
Data Split: 80% training, 20% testing (stratified)

Evaluation Metrics

Accuracy
Precision (Fraud detection)
Recall (Fraud detection)
F1-Score (Fraud detection)
Confusion Matrix visualization

🔍 Model Comparison
ModelAdvantagesUse CaseRandom ForestHigher accuracy, robust against overfittingProduction deploymentDecision TreeInterpretable, faster predictionsRegulatory compliance
🖼️ Screenshots
Main Interface
<img width="750" height="600" alt="image" src="https://github.com/user-attachments/assets/d846b171-308b-46da-895e-2dc4a4a21abe" />

Fraud Detection Result
<img width="750" height="600" alt="image" src="https://github.com/user-attachments/assets/e2a7e7e4-bbb4-4e1b-aeef-a0b3d28b1549" />

Model Metrics Dashboard
<img width="200" height="115" alt="image" src="https://github.com/user-attachments/assets/57207f2c-2d6c-4ed6-b768-6abaea06478f" />

📊 Dataset Information
The project uses a balanced credit card fraud dataset with the following characteristics:

Target Variable: IsFraud (0: Legitimate, 1: Fraudulent)
Class Distribution: Balanced dataset for optimal training
Data Quality: Preprocessed and cleaned for ML applications

🚀 Deployment
Local Development
bashpython app.py
Production Deployment
For production deployment, consider:

Heroku: Easy cloud deployment
AWS EC2: Scalable cloud infrastructure
Docker: Containerized deployment
Gunicorn: Production WSGI server

Docker Deployment (Optional)
dockerfileFROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Tejas M Naik

Registration: NNM23CS513
Email: naiktejasmn@gmail.com
GitHub: https://github.com/naiktejas

🙏 Acknowledgments

DLithe Consultancy Services Pvt. Ltd. for internship opportunity
Supervisors: Ms. Archana, Ms. Sushma for guidance and mentorship
scikit-learn community for excellent ML libraries
Flask team for the web framework

📚 References

scikit-learn Documentation
Flask Documentation
imbalanced-learn Documentation
Fraud Detection Best Practices

🔮 Future Enhancements

 Integration with real-time payment APIs
 Advanced neural network models (LSTM, CNN)
 Explainable AI features (LIME/SHAP)
 Model drift monitoring
 Automated retraining pipeline
 Mobile-responsive interface improvements
 Advanced feature engineering (time-series analysis)
 Multi-model ensemble predictions


⭐ If you found this project helpful, please give it a star! ⭐
