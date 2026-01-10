import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load clean data (assuming analysis.py or previous step cleaned it, but we'll re-clean for safety in this standalone script)
try:
    df = pd.read_csv('data/survey.csv')
except:
    print("Error loading data")
    exit()

# Simple Cleaning pipeline
def clean_data(df):
    # Standardize Gender
    def clean_gender(g):
        if isinstance(g, str):
            g = g.lower().strip()
            if g in ['male', 'm', 'man', 'cis male', 'mal', 'male (cis)', 'make', 'male-ish', 'maile']:
                return 'Male'
            elif g in ['female', 'f', 'woman', 'cis female', 'femake', 'female ']:
                return 'Female'
            else:
                return 'Other'
        return 'Other'

    df['Gender'] = df['Gender'].apply(clean_gender)
    
    # Handle Age
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]
    
    # Drop timestamp and comments
    df = df.drop(columns=['Timestamp', 'comments', 'state', 'Country'], errors='ignore')
    
    # Fill NA
    df = df.fillna('Unknown')
    return df

df = clean_data(df)

# Encoding
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# Model Prep
X = df.drop('treatment', axis=1)
y = df['treatment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature Importance
feature_imp = pd.Series(clf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop 5 Feature Importances:")
print(feature_imp.head(5))
