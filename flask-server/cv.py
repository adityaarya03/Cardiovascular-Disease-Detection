# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import seaborn as sb
import matplotlib.pyplot as plt

# Load the dataset and drop missing values
df = pd.read_csv('Cardiovascular_Disease_Dataset.csv').dropna()
if 'patientid' in df.columns:
    df = df.drop(columns=['patientid'])

# Separate features and target
X = df.drop('target', axis=1)  # Only features
y = df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features and save the scaler
scaler = StandardScaler()
scaler.fit(X_train)  # Fit only on the 12 feature columns
joblib.dump(scaler, 'models/scaler.pkl')  # Save the scaler
print("Scaler saved successfully as scaler.pkl")

# Function to train, evaluate, and save each model
def evaluate_and_save_model(model, X_train, X_test, y_train, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} Accuracy: {accuracy}")
    
    # Display confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sb.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'Confusion Matrix for {model.__class__.__name__}')
    plt.savefig(f'models/Confusion_Matrix_{model_name}.svg', format='svg', bbox_inches='tight')
    plt.show()
    
    # Save the model
    joblib.dump(model, f'models/{model_name}.pkl')
    print(f"{model_name} model saved successfully as {model_name}.pkl")

# Train and save each model
models = {
    'decision_tree_model': DecisionTreeClassifier(),
    'random_forest_model': RandomForestClassifier(),
    'knn_model': KNeighborsClassifier(),
    'adaboost_model': AdaBoostClassifier(),
    'gradient_boosting_model': GradientBoostingClassifier()
}

# Scale training and test sets
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

for model_name, model in models.items():
    evaluate_and_save_model(model, X_train_scaled, X_test_scaled, y_train, y_test, model_name)
