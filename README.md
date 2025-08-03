💳 Credit Card Fraud Detection System

A comprehensive machine learning project that detects fraudulent credit card transactions using Random Forest and Decision Tree algorithms with an interactive web interface.

<div align="center">
Show Image
Show Image
Show Image
Show Image
Show Image
Show Image
Show Image
Show Image
</div>

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


✨ Features
<table>
<tr>
<td>
🔍 Real-time Detection

Instant fraud classification
Confidence score analysis
Sub-second response time

</td>
<td>
🤖 Multiple ML Models

Random Forest Classifier
Decision Tree Classifier
Performance comparison

</td>
</tr>
<tr>
<td>
🎨 Interactive Web UI

Modern dark theme interface
Responsive design
User-friendly controls

</td>
<td>
⚖️ Class Balance Handling

SMOTE implementation
Imbalanced dataset optimization
Synthetic sample generation

</td>
</tr>
<tr>
<td>
📊 Comprehensive Metrics

Precision, Recall, F1-Score
Confusion matrix visualization
Model performance dashboard

</td>
<td>
🧪 Sample Data Testing

Pre-loaded fraud examples
Legitimate transaction samples
Quick testing functionality

</td>
</tr>
</table>

🛠️ Technology Stack
<details open>
<summary><b>Backend Technologies</b></summary>
TechnologyVersionPurposeShow Image3.8+Core programming languageShow Image2.0+Web frameworkShow Image1.0+Machine learning libraryShow Image1.5+Data manipulationShow Image1.24+Numerical computing
</details>
<details>
<summary><b>Frontend Technologies</b></summary>
TechnologyPurposeShow ImageStructure and markupShow ImageStyling and designShow ImageInteractive functionality
</details>
<details>
<summary><b>ML & Data Science Libraries</b></summary>

imbalanced-learn: SMOTE implementation
matplotlib: Data visualization
joblib: Model serialization
ColumnTransformer: Feature preprocessing
Pipeline: ML workflow management

</details>

📊 Project Structure
📦 Credit-Card-Fraud-Detection/
├── 📄 app.py                                    # 🌐 Flask web application
├── 📄 train_model.py                           # 🤖 ML model training script
├── 📊 balanced_credit_card_fraud_dataset.csv   # 📈 Training dataset
├── 📋 requirements.txt                         # 📦 Python dependencies
├── 📁 templates/
│   └── 📄 index.html                          # 🎨 Web interface template
├── 📁 static/                                 # 🖼️ Static assets
│   ├── 📊 rf_conf_matrix.png                 # Random Forest confusion matrix
│   └── 📊 dt_conf_matrix.png                 # Decision Tree confusion matrix
├── 📁 .ipynb_checkpoints/                     # 📓 Jupyter checkpoints
├── 📄 rf_model.pkl                           # 🌲 Random Forest model
├── 📄 dt_model.pkl                           # 🌳 Decision Tree model
├── 📄 test_data.pkl                          # 🧪 Test dataset
├── 📄 model_features.pkl                     # 📋 Feature definitions
└── 📖 README.md                              # 📚 Documentation

🚀 Quick Start
📋 Prerequisites
<div align="center">
Show Image
Show Image
Show Image
</div>
⚡ Installation
bash# 1️⃣ Clone the repository
git clone https://github.com/tejasnaik/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# 2️⃣ Create virtual environment (recommended)
python -m venv fraud_detection_env

# 3️⃣ Activate virtual environment
# Windows:
fraud_detection_env\Scripts\activate
# macOS/Linux:
source fraud_detection_env/bin/activate

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Train the models
python train_model.py

# 6️⃣ Run the application
python app.py
🌐 Access the Application
Open your browser and navigate to:
http://127.0.0.1:5000

💡 Usage
🖥️ Web Interface Guide
<details open>
<summary><b>Step-by-Step Usage</b></summary>

🎯 Select Model
Choose between Random Forest or Decision Tree

📝 Input Transaction Details

💰 Amount: Transaction value (e.g., 1500.00)
🏪 Merchant ID: Unique identifier (e.g., 12345)
🛒 Transaction Type: Purchase or Refund
📍 Location: Geographic location


🔮 Get Prediction
Click "Predict" button for instant analysis

📊 View Results

Fraud/Legitimate classification
Confidence percentage
Model performance metrics



</details>
🧪 Sample Data Testing
ButtonDescriptionUse Case🟢 Load Legit SampleLoads legitimate transactionTest normal transaction flow🔴 Load Fraud SampleLoads fraudulent transactionTest fraud detection accuracy
🤖 Model Training
bash# Train both models with full pipeline
python train_model.py
Training Process:

✅ Data loading and preprocessing
✅ Feature engineering and encoding
✅ SMOTE class balancing
✅ Model training and evaluation
✅ Confusion matrix generation
✅ Model serialization


📈 Model Performance
📊 Dataset Overview
<table>
<tr>
<th>Feature</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td><b>Amount</b></td>
<td>Numerical</td>
<td>Transaction value</td>
<td>$1,299.99</td>
</tr>
<tr>
<td><b>MerchantID</b></td>
<td>Numerical</td>
<td>Unique merchant identifier</td>
<td>12345</td>
</tr>
<tr>
<td><b>TransactionType</b></td>
<td>Categorical</td>
<td>Purchase or Refund</td>
<td>purchase</td>
</tr>
<tr>
<td><b>Location</b></td>
<td>Categorical</td>
<td>Geographic location</td>
<td>New York</td>
</tr>
</table>
🔄 ML Pipeline Architecture
mermaidgraph LR
    A[Raw Data] --> B[Data Preprocessing]
    B --> C[Feature Engineering]
    C --> D[SMOTE Balancing]
    D --> E[Model Training]
    E --> F[Model Evaluation]
    F --> G[Web Deployment]
⚖️ Model Comparison
<div align="center">
Model🎯 Accuracy⚡ Speed🔍 Interpretability🚀 Best For🌲 Random ForestHigherModerateGoodProduction🌳 Decision TreeGoodFastExcellentAnalysis
</div>
📊 Evaluation Metrics

📈 Accuracy: Overall model correctness
🎯 Precision: True fraud detection rate
🔍 Recall: Fraud cases caught
⚖️ F1-Score: Balanced performance metric
📋 Confusion Matrix: Visual performance analysis


🖼️ Screenshots
<details>
<summary><b>🖥️ Application Interface</b></summary>
Main Dashboard
Coming Soon - Add your actual screenshots here
Fraud Detection Results
Coming Soon - Add your actual screenshots here
Performance Metrics
Coming Soon - Add your actual screenshots here
</details>

🚀 Deployment
🏠 Local Development
bashpython app.py
# Access at http://127.0.0.1:5000
☁️ Cloud Deployment Options
<details>
<summary><b>🌐 Heroku Deployment</b></summary>
bash# Create Procfile
echo "web: python app.py" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
</details>
<details>
<summary><b>🐳 Docker Deployment</b></summary>
dockerfileFROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
bash# Build and run
docker build -t fraud-detection .
docker run -p 5000:5000 fraud-detection
</details>
<details>
<summary><b>☁️ AWS EC2 Deployment</b></summary>

Launch EC2 instance
Install Python and dependencies
Clone repository
Run with Gunicorn for production

bashpip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
</details>

🤝 Contributing
We welcome contributions! Here's how you can help:
<details>
<summary><b>🛠️ Development Setup</b></summary>
bash# Fork the repository
git fork https://github.com/tejasnaik/Credit-Card-Fraud-Detection

# Clone your fork
git clone https://github.com/yourusername/Credit-Card-Fraud-Detection
cd Credit-Card-Fraud-Detection

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
</details>
🎯 Contribution Areas

🐛 Bug Fixes: Report and fix issues
✨ New Features: Add functionality
📚 Documentation: Improve docs
🧪 Testing: Add test cases
🎨 UI/UX: Enhance interface


📝 License
<div align="center">
Show Image
This project is licensed under the MIT License - see the LICENSE file for details.
</div>

👨‍💻 Author
<div align="center">
Tejas M Naik
AI/ML Engineering Student
Show Image
Show Image
Show Image
Registration: NNM23CS513
Institution: DLithe Consultancy Services Pvt. Ltd.
</div>

🙏 Acknowledgments
<div align="center">
🏢 Organization👥 Supervisors🛠️ TechnologiesDLithe ConsultancyMs. Archanascikit-learnServices Pvt. Ltd.Ms. SushmaFlask Framework
</div>
🌟 Special Thanks

🎓 DLithe Consultancy for the internship opportunity
👨‍🏫 Mentors for guidance and support
🔬 scikit-learn community for excellent ML tools
🌐 Flask team for the web framework
💡 Open source community for inspiration


🔮 Future Enhancements
<div align="center">
🚀 Roadmap
</div>

 🧠 Advanced Models: Neural Networks, XGBoost, LSTM
 🔄 Real-time API: Live transaction processing
 📱 Mobile App: React Native interface
 🤖 Auto-ML: Automated model selection
 📊 Advanced Analytics: Time-series analysis
 🔍 Explainable AI: LIME/SHAP integration
 📈 Model Monitoring: Drift detection
 ☁️ Cloud Integration: AWS/GCP deployment
 🔐 Security: Enhanced authentication
 📧 Alert System: Email/SMS notifications


<div align="center">
⭐ If you found this project helpful, please give it a star! ⭐
Show Image
Happy Coding! 🚀

Made with ❤️ by Tejas M Naik
</div>
