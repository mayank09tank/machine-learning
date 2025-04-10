from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Use "estimator" instead of "base_estimator"
bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=50, random_state=42)
adaboost = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, random_state=42)

# Fit models
bagging.fit(X_train, y_train)
adaboost.fit(X_train, y_train)

# Predictions
y_pred_bag = bagging.predict(X_test)
y_pred_ada = adaboost.predict(X_test)

# Metrics function
def evaluate(y_true, y_pred, name):
    print(f"\n{name} Performance:")
    print(f"Accuracy : {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred):.4f}")
    print(f"Recall   : {recall_score(y_true, y_pred):.4f}")

# Evaluate both models
evaluate(y_test, y_pred_bag, "Bagging Classifier")
evaluate(y_test, y_pred_ada, "AdaBoost Classifier")