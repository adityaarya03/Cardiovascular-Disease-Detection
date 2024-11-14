# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load the dataset
df = pd.read_csv('Cardiovascular_Disease_Dataset.csv')

# Separate features and target
X = df.drop('target', axis=1)
y = df['target'].values  # Convert to numpy array

# Check for missing values and drop if any
df.dropna(inplace=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler for later use in the API
joblib.dump(scaler, 'models/scaler.pkl')
print("Scaler saved successfully as scaler.pkl")

# Define each model
decision_tree = DecisionTreeClassifier()
random_forest = RandomForestClassifier()
knn = KNeighborsClassifier()
adaboost = AdaBoostClassifier()
gradient_boosting = GradientBoostingClassifier()

# Function to train and evaluate models
def evaluate_and_save_model(model, X_train, X_test, y_train, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    # Display confusion matrix
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
    
    return accuracy, report, y_pred

# Train and save each model
print("\nDecision Tree (No Feature Selection)")
evaluate_and_save_model(decision_tree, X_train_scaled, X_test_scaled, y_train, y_test, 'decision_tree_model')

print("\nRandom Forest (No Feature Selection)")
evaluate_and_save_model(random_forest, X_train_scaled, X_test_scaled, y_train, y_test, 'random_forest_model')

print("\nK-Nearest Neighbors (No Feature Selection)")
evaluate_and_save_model(knn, X_train_scaled, X_test_scaled, y_train, y_test, 'knn_model')

print("\nAdaBoost (No Feature Selection)")
evaluate_and_save_model(adaboost, X_train_scaled, X_test_scaled, y_train, y_test, 'adaboost_model')

print("\nGradient Boosting (No Feature Selection)")
evaluate_and_save_model(gradient_boosting, X_train_scaled, X_test_scaled, y_train, y_test, 'gradient_boosting_model')
