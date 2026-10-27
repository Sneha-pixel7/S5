import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
columns = [
    'Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigree',
    'Age',
    'Outcome',
]
df = pd.read_csv(url, names=columns)
X, y = df.drop('Outcome', axis=1).values, df['Outcome'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_unscaled = LogisticRegression(
    solver='saga', max_iter=1000, random_state=42
).fit(X_train, y_train)
y_pred_unscaled = model_unscaled.predict(X_test)

scaler = StandardScaler()
X_train_scaled, X_test_scaled = scaler.fit_transform(X_train), scaler.transform(
    X_test
)
model_scaled = LogisticRegression(
    solver='saga', max_iter=1000, random_state=42
).fit(X_train_scaled, y_train)
y_pred_scaled = model_scaled.predict(X_test_scaled)


def calculate_metrics(y_true, y_pred, label):
  return {
      'Framework': label,
      'Accuracy': accuracy_score(y_true, y_pred),
      'Precision': precision_score(y_true, y_pred),
      'Recall': recall_score(y_true, y_pred),
      'F1-Score': f1_score(y_true, y_pred),
  }


metrics_df = pd.DataFrame([
    calculate_metrics(y_test, y_pred_unscaled, 'Without Scaling'),
    calculate_metrics(y_test, y_pred_scaled, 'With Scaling (Standardized)'),
])
print(metrics_df.to_string(index=False))

plt.figure(figsize=(10, 5))
plt.bar(
    columns[:-1],
    model_unscaled.coef_[0],
    alpha=0.6,
    label='Unscaled Weights',
    color='red',
)
plt.bar(
    columns[:-1],
    model_scaled.coef_[0],
    alpha=0.6,
    label='Scaled Weights',
    color='blue',
)
plt.axhline(0, color='black', linestyle=':')
plt.xticks(rotation=30)
plt.ylabel('Weight Parameter Coefficient Value')
plt.title('Weight Coefficients: Unscaled vs. Standardized Features')
plt.legend()
plt.tight_layout()
plt.show()