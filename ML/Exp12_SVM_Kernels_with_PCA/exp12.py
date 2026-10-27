import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
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
from tensorflow.keras.datasets import fashion_mnist

(X_train_full, y_train_full), (X_test_full, y_test_full) = fashion_mnist.load_data()
class_names = [
    'T-shirt/top',
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot',
]
print('Train shape:', X_train_full.shape), print('Test shape:', X_test_full.shape)

plt.figure(figsize=(10, 4))
for i in range(10):
  plt.subplot(2, 5, i + 1), plt.imshow(X_train_full[i], cmap='gray')
  plt.title(class_names[y_train_full[i]], fontsize=8), plt.axis('off')
plt.tight_layout(), plt.show()
print(pd.Series(y_train_full).value_counts().sort_index())

X_sub, _, y_sub, _ = train_test_split(
    X_train_full.reshape(len(X_train_full), -1),
    y_train_full,
    train_size=6000,
    stratify=y_train_full,
    random_state=42,
)
X_sub = X_sub.astype('float32') / 255.0
X_train, X_test, y_train, y_test = train_test_split(
    X_sub, y_sub, test_size=0.2, random_state=42, stratify=y_sub
)

scaler = StandardScaler()
X_train_scaled, X_test_scaled = scaler.fit_transform(X_train), scaler.transform(X_test)
pca = PCA(n_components=50, random_state=42)
X_train_pca, X_test_pca = pca.fit_transform(X_train_scaled), pca.transform(X_test_scaled)
print(f'Explained variance retained: {pca.explained_variance_ratio_.sum():.4f}')

start = time.time()
svm_linear = SVC(kernel='linear', C=1.0).fit(X_train_pca, y_train)
time_linear = time.time() - start
y_pred_linear = svm_linear.predict(X_test_pca)

start = time.time()
svm_poly = SVC(kernel='poly', degree=3, C=1.0, gamma='scale').fit(
    X_train_pca, y_train
)
time_poly = time.time() - start
y_pred_poly = svm_poly.predict(X_test_pca)

start = time.time()
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale').fit(X_train_pca, y_train)
time_rbf = time.time() - start
y_pred_rbf = svm_rbf.predict(X_test_pca)


def evaluate(name, y_true, y_pred, train_time):
  acc = accuracy_score(y_true, y_pred)
  prec = precision_score(y_true, y_pred, average='macro')
  rec = recall_score(y_true, y_pred, average='macro')
  f1 = f1_score(y_true, y_pred, average='macro')
  print(
      f'{name:12s} Acc={acc:.4f} Prec={prec:.4f} Rec={rec:.4f} F1={f1:.4f}'
      f' Time={train_time:.2f}s'
  )
  return [name, acc, prec, rec, f1, train_time]


results = [
    evaluate('Linear', y_test, y_pred_linear, time_linear),
    evaluate('Polynomial', y_test, y_pred_poly, time_poly),
    evaluate('RBF', y_test, y_pred_rbf, time_rbf),
]
results_df = pd.DataFrame(
    results, columns=['Kernel', 'Accuracy', 'Precision', 'Recall', 'F1', 'Train Time (s)']
)
print(results_df)

results_df.plot(x='Kernel', y='Accuracy', kind='bar', legend=False, color='steelblue')
plt.ylabel('Test Accuracy'), plt.title(
    'SVM Kernel Comparison on Fashion MNIST'
), plt.tight_layout(), plt.show()

cm = confusion_matrix(y_test, y_pred_rbf)
plt.figure(figsize=(7, 6))
plt.imshow(cm, cmap='Blues'), plt.colorbar()
plt.xticks(range(10), class_names, rotation=90), plt.yticks(range(10), class_names)
plt.xlabel('Predicted Label'), plt.ylabel('True Label')
plt.title('Confusion Matrix — Best Kernel'), plt.tight_layout(), plt.show()