import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

print("Loading MNIST dataset...")
try:
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="auto")
except TypeError:
    # Workaround for Python 3.14 / Pandas 3+ bug in scikit-learn arff parser
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="liac-arff")
X, y = mnist.data / 255.0, mnist.target.astype(int)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)
print("Dataset processing complete.")

history_loss = {}
test_accuracies = {}
activations = ["logistic", "tanh", "relu"]

for act in activations:
    print(f"Training network using activation: {act}")
    mlp = MLPClassifier(
        hidden_layer_sizes=(128, 64),
        activation=act,
        max_iter=25,
        random_state=42,
    )
    mlp.fit(X_train, y_train)
    history_loss[act] = mlp.loss_curve_
    test_accuracies[act] = accuracy_score(y_test, mlp.predict(X_test))

plt.figure(figsize=(10, 5))
for act in activations:
    plt.plot(history_loss[act], label=act)

plt.title("Loss Convergence Comparison")
plt.xlabel("Epochs")
plt.ylabel("Loss Value")
plt.legend()
plt.show()