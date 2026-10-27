import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

cancer = load_breast_cancer(as_frame=True)
X, y, features = cancer.data.values, cancer.target.values, cancer.feature_names
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_sc, X_test_sc = scaler.fit_transform(X_train), scaler.transform(X_test)

mle_model = LogisticRegression(
    penalty=None, solver='lbfgs', max_iter=10000
).fit(X_train_sc, y_train)
w_mle, y_pred_mle = mle_model.coef_[0], mle_model.predict(X_test_sc)
print(
    f'MLE (Unregularized) Test Accuracy: {accuracy_score(y_test, y_pred_mle):.4f}'
)
print(f'MLE Norm (sum of squared weights): {np.sum(w_mle**2):.4f}')

map_l2_model = LogisticRegression(
    penalty='l2', C=0.1, solver='lbfgs', max_iter=10000
).fit(X_train_sc, y_train)
w_l2, y_pred_l2 = map_l2_model.coef_[0], map_l2_model.predict(X_test_sc)
print(
    f'MAP L2 (Gaussian Prior) Test Accuracy:'
    f' {accuracy_score(y_test, y_pred_l2):.4f}'
)
print(f'MAP L2 Norm (sum of squared weights): {np.sum(w_l2**2):.4f}')

map_l1_model = LogisticRegression(
    penalty='l1', C=0.1, solver='saga', max_iter=10000, random_state=42
).fit(X_train_sc, y_train)
w_l1, y_pred_l1 = map_l1_model.coef_[0], map_l1_model.predict(X_test_sc)
print(
    f'MAP L1 (Laplace Prior) Test Accuracy:'
    f' {accuracy_score(y_test, y_pred_l1):.4f}'
)
print(
    f'MAP L1 Sparsity (Zero Coefficients): {np.sum(w_l1 == 0)} out of'
    f' {len(w_l1)}'
)

print(
    '\nWeight Comparison Table:\n',
    pd.DataFrame({
        'Feature': features,
        'MLE (No Prior)': w_mle,
        'MAP L2 (Gaussian Prior)': w_l2,
        'MAP L1 (Laplace Prior)': w_l1,
    }).head(10),
)

plt.figure(figsize=(12, 6))
plt.plot(
    features[:15],
    w_mle[:15],
    label='MLE (No Prior)',
    marker='o',
    color='red',
    linestyle='--',
)
plt.plot(
    features[:15],
    w_l2[:15],
    label='MAP L2 (Gaussian)',
    marker='s',
    color='blue',
)
plt.plot(
    features[:15],
    w_l1[:15],
    label='MAP L1 (Laplace)',
    marker='^',
    color='green',
)
plt.axhline(0, color='black', linestyle=':', alpha=0.5)
plt.xticks(rotation=45, ha='right')
plt.title('Parameter Estimates Comparison (First 15 Features)')
plt.ylabel('Weight Value')
plt.legend()
plt.tight_layout()
plt.show()