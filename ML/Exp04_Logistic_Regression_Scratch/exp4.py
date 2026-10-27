import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
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

# Data
cancer = load_breast_cancer(as_frame=True)
X_tr, X_te, y_tr, y_te = train_test_split(
    cancer.data.values, cancer.target.values, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_tr_sc, X_te_sc = scaler.fit_transform(X_tr), scaler.transform(X_te)


# Scratch Logistic Regression
def sigmoid(z):
  return 1 / (1 + np.exp(-z))


def train_lr(X, y, lr=0.1, epochs=1000):
  m, n = X.shape
  X_b, w = np.c_[np.ones(m), X], np.zeros(n + 1)
  for _ in range(epochs):
    w -= lr * np.dot(X_b.T, sigmoid(np.dot(X_b, w)) - y) / m
  return w


w = train_lr(X_tr_sc, y_tr)
p_scratch = (
    sigmoid(np.dot(np.c_[np.ones(len(X_te_sc)), X_te_sc], w)) >= 0.5
).astype(int)

# Sklearn Model
sk_model = LogisticRegression(max_iter=1000).fit(X_tr_sc, y_tr)
p_sk = sk_model.predict(X_te_sc)

# Evaluation
for name, p in [('Scratch', p_scratch), ('Sklearn', p_sk)]:
  print(
      f'{name:10s} | Acc: {accuracy_score(y_te, p):.4f} | Prec:'
      f' {precision_score(y_te, p):.4f} | Rec: {recall_score(y_te, p):.4f} | F1:'
      f' {f1_score(y_te, p):.4f}'
  )
  print(confusion_matrix(y_te, p))