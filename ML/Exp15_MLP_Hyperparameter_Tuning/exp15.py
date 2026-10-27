import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

fashion_mnist = fetch_openml('Fashion-MNIST', version=1, as_frame=False, parser='auto')
X, y = fashion_mnist.data / 255.0, fashion_mnist.target.astype(int)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)
X_train_sub, _, y_train_sub, _ = train_test_split(
    X_train, y_train, train_size=10000, stratify=y_train, random_state=42
)

results_registry = []
for lr in [0.001, 0.1]:
  for bs in [32, 256]:
    for epochs in [10, 20]:
      mlp = MLPClassifier(
          hidden_layer_sizes=(128, 64),
          activation='relu',
          solver='sgd',
          learning_rate_init=lr,
          batch_size=bs,
          max_iter=epochs,
          random_state=42,
      )
      start = time.time()
      mlp.fit(X_train_sub, y_train_sub)
      results_registry.append({
          'LR': lr,
          'Batch': bs,
          'Epochs': epochs,
          'Time': time.time() - start,
          'Accuracy': accuracy_score(y_test, mlp.predict(X_test)) * 100,
      })

summary_df = pd.DataFrame(results_registry)
print(summary_df.to_string(index=False))

plt.figure(figsize=(10, 5))
configs = [
    f"LR:{r['LR']}|B:{r['Batch']}|E:{r['Epochs']}" for r in results_registry
]
plt.barh(configs, [r['Accuracy'] for r in results_registry], color='steelblue')
plt.xlabel('Test Accuracy (%)'), plt.title(
    'Hyperparameter Configuration vs Accuracy'
), plt.show()