import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import joblib
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("balanced_credit_card_fraud_dataset.csv")
df = df.drop(columns=["TransactionID", "TransactionDate"], errors="ignore")

# Separate features and target
X = df.drop("IsFraud", axis=1)
y = df["IsFraud"]

# Feature groups
numerical_features = ["Amount", "MerchantID"]
categorical_features = ["TransactionType", "Location"]

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

# Pipelines for both models
pipelines = {
    'rf': ImbPipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=42)),
        ('classifier', RandomForestClassifier(random_state=42))
    ]),
    'dt': ImbPipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=42)),
        ('classifier', DecisionTreeClassifier(random_state=42))
    ])
}

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Ensure static folder exists for saving plots
os.makedirs("static", exist_ok=True)

# Train and evaluate models
for name, pipeline in pipelines.items():
    print(f"\n🔧 Training {name.upper()}...")
    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    # Print classification report
    print(f"\n📊 Classification Report for {name.upper()}:\n")
    print(classification_report(y_test, preds))

    # Print accuracy
    accuracy = accuracy_score(y_test, preds)
    print(f"✅ Accuracy for {name.upper()}: {accuracy:.4f}")

    # Save confusion matrix image
    cm = confusion_matrix(y_test, preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Legit", "Fraud"])
    fig, ax = plt.subplots(figsize=(5, 5))
    disp.plot(ax=ax, cmap="Blues", values_format='d')
    plt.title(f"{name.upper()} Confusion Matrix")
    plt.savefig(f"static/{name}_conf_matrix.png")
    plt.close()

    # Save model
    joblib.dump(pipeline, f"{name}_model.pkl")

# Save test data for Flask app
joblib.dump((X_test, y_test), "test_data.pkl")
joblib.dump(list(X.columns), "model_features.pkl")
