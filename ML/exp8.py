import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.datasets import fashion_mnist

(X_train_raw, y_train), (X_test_raw, y_test) = fashion_mnist.load_data()
train_mask = np.random.choice(X_train_raw.shape[0], 5000, replace=False)
test_mask = np.random.choice(X_test_raw.shape[0], 500, replace=False)
X_train_sub, y_train = X_train_raw[train_mask], y_train[train_mask]
X_test_sub, y_test = X_test_raw[test_mask], y_test[test_mask]

X_train = (
    X_train_sub.reshape(X_train_sub.shape[0], -1).astype('float32') / 255.0
)
X_test = X_test_sub.reshape(X_test_sub.shape[0], -1).astype('float32') / 255.0
class_names = [
    'T-shirt/top',
    'Trouser',
    'Pullover',
    'Drop',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot',
]
print(f'Training feature array matrix shape: {X_train.shape}')

k_values = [1, 3, 5, 11]
results = []
for k in k_values:
  print(f'Training KNN framework with K={k}...')
  knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')

  start_time = time.time()
  knn.fit(X_train, y_train)
  train_time = time.time() - start_time

  start_time = time.time()
  y_pred = knn.predict(X_test)
  test_time = time.time() - start_time

  acc = accuracy_score(y_test, y_pred)
  f1 = f1_score(y_test, y_pred, average='macro')

  results.append({
      'K-Value': k,
      'Accuracy': acc,
      'Macro F1-Score': f1,
      'Inference Latency (s)': test_time,
  })

results_df = pd.DataFrame(results)
print('\nHyperparameter Performance Summary Table:\n')
print(results_df.to_string(index=False))

fig, ax1 = plt.subplots(figsize=(8, 4))
color = 'tab:blue'
ax1.set_xlabel('Hyperparameter Value (K)')
ax1.set_ylabel('Test Accuracy Score', color=color)
ax1.plot(
    results_df['K-Value'],
    results_df['Accuracy'],
    marker='o',
    color=color,
    linewidth=2,
)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Inference Delay Time (Seconds)', color=color)
ax2.plot(
    results_df['K-Value'],
    results_df['Inference Latency (s)'],
    marker='s',
    color=color,
    linestyle='--',
)
ax2.tick_params(axis='y', labelcolor=color)
plt.title('KNN Parameter Grid Search Analysis: Accuracy vs. Efficiency')
fig.tight_layout()
plt.show()