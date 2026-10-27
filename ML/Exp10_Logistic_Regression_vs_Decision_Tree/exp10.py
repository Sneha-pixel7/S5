import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
columns = [
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'gain',
    'loss',
    'hours',
    'country',
    'income',
]
df = pd.read_csv(url, names=columns, skipinitialspace=True, na_values='?').dropna()
df['income'] = df['income'].apply(lambda x: 1 if '>50K' in x else 0)

cat_cols = [
    'workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'sex',
]
num_cols = ['age', 'education-num', 'gain', 'loss', 'hours']
df_encoded = pd.get_dummies(
    df[cat_cols + num_cols + ['income']], columns=cat_cols, drop_first=True
)

X, y = df_encoded.drop('income', axis=1).values, df_encoded['income'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train_scaled, X_test_scaled = scaler.fit_transform(X_train), scaler.transform(
    X_test
)
print(f'Encoded dataset feature bounds: {X_train_scaled.shape}')

log_reg = LogisticRegression(max_iter=1000, random_state=42).fit(
    X_train_scaled, y_train
)
y_pred_lr = log_reg.predict(X_test_scaled)

tree_clf = DecisionTreeClassifier(
    max_depth=5, criterion='entropy', random_state=42
).fit(X_train, y_train)
y_pred_dt = tree_clf.predict(X_test)


def compile_metrics(y_true, y_pred, name):
  return {
      'Model Framework': name,
      'Accuracy': accuracy_score(y_true, y_pred),
      'Precision': precision_score(y_true, y_pred),
      'Recall': recall_score(y_true, y_pred),
      'F1-Score': f1_score(y_true, y_pred),
  }


metrics_df = pd.DataFrame([
    compile_metrics(y_test, y_pred_lr, 'Logistic Regression'),
    compile_metrics(y_test, y_pred_dt, 'Decision Tree Classifier'),
])
print('\nPerformance Comparisons Matrix:\n', metrics_df.to_string(index=False))