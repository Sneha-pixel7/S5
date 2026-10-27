import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]
print(df.head()), print(df['species'].value_counts())

plt.figure(figsize=(7, 5))
for species, color in zip(iris.target_names, ['crimson', 'steelblue', 'green']):
  sub = df[df['species'] == species]
  plt.scatter(
      sub['petal length (cm)'],
      sub['petal width (cm)'],
      label=species,
      alpha=0.7,
      color=color,
  )
plt.xlabel('Petal Length (cm)'), plt.ylabel('Petal Width (cm)')
plt.title('Petal Length vs Petal Width by Species'), plt.legend(), plt.show()

y_bin = (iris.target == 0).astype(int)
X = df[['petal length (cm)', 'petal width (cm)']].values
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y_bin, test_size=0.2, random_state=42, stratify=y_bin
)

scaler = StandardScaler()
X_tr_sc, X_te_sc = scaler.fit_transform(X_tr), scaler.transform(X_te)
svm = SVC(kernel='linear', C=1.0).fit(X_tr_sc, y_tr)
pred = svm.predict(X_te_sc)

print(
    f'Accuracy={accuracy_score(y_te, pred):.4f}'
    f' Precision={precision_score(y_te, pred):.4f}'
    f' Recall={recall_score(y_te, pred):.4f} F1={f1_score(y_te, pred):.4f}'
)
print('Confusion Matrix:\n', confusion_matrix(y_te, pred))


def plot_svm(model, X, y, scl):
  X_org = scl.inverse_transform(X)
  plt.figure(figsize=(8, 6))
  plt.scatter(X_org[y == 1, 0], X_org[y == 1, 1], color='crimson', label='Setosa')
  plt.scatter(
      X_org[y == 0, 0], X_org[y == 0, 1], color='steelblue', label='Non-Setosa'
  )
  ax = plt.gca()
  xlim, ylim = ax.get_xlim(), ax.get_ylim()
  xx, yy = np.linspace(xlim[0], xlim[1], 200), np.linspace(ylim[0], ylim[1], 200)
  YY, XX = np.meshgrid(yy, xx)
  Z = model.decision_function(scl.transform(np.c_[XX.ravel(), YY.ravel()])).reshape(
      XX.shape
  )
  ax.contour(XX, YY, Z, colors='black', levels=[-1, 0, 1], alpha=0.7, linestyles=['--', '-', '--'])
  sv = scl.inverse_transform(model.support_vectors_)
  ax.scatter(sv[:, 0], sv[:, 1], s=120, facecolors='none', edgecolors='black', linewidths=1.5, label='Support Vectors')
  plt.xlabel('Petal Length (cm)'), plt.ylabel('Petal Width (cm)')
  plt.title('Linear SVM Decision Boundary and Margin (Setosa vs Non-Setosa)')
  plt.legend(), plt.show()


plot_svm(svm, X_tr_sc, y_tr, scaler)