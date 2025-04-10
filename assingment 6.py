from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib  # for saving and loading the model

# Step 1: Generate synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                           n_redundant=5, random_state=42)

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Save model using joblib
joblib.dump(model, 'random_forest_model.pkl')
print("✅ Model saved to 'random_forest_model.pkl'")

# Step 5: Load the saved model
loaded_model = joblib.load('random_forest_model.pkl')
print("✅ Model loaded from file")

# Step 6: Predict and evaluate
y_pred = loaded_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Accuracy on test set: {accuracy:.4f}")
