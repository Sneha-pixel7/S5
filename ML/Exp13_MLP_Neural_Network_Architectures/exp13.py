import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
df = pd.read_csv(url, sep=';')
print(df.head()), print(df['quality'].value_counts().sort_index())

plt.figure(figsize=(7, 4))
plt.hist(
    df['quality'], bins=range(3, 10), color='steelblue', edgecolor='white', align='left'
)
plt.xlabel('Quality Score'), plt.ylabel('Count'), plt.title(
    'Distribution of Wine Quality Scores'
), plt.show()
print(df.describe()), print(df.isna().sum())

df['good_quality'] = (df['quality'] >= 7).astype(int)
X, y = (
    df.drop(columns=['quality', 'good_quality']).values,
    df['good_quality'].values,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled, X_test_scaled = scaler.fit_transform(X_train), scaler.transform(
    X_test
)

baseline_mlp = MLPClassifier(
    hidden_layer_sizes=(8,), activation='relu', max_iter=500, random_state=42
).fit(X_train_scaled, y_train)
y_pred_base = baseline_mlp.predict(X_test_scaled)
print(f'Baseline (8,) => Accuracy={accuracy_score(y_test, y_pred_base):.4f}')

architectures = [(4,), (16,), (64,), (16, 8), (32, 16, 8)]
results, models = [], {}
for arch in architectures:
  mlp = MLPClassifier(
      hidden_layer_sizes=arch, activation='relu', max_iter=1000, random_state=42
  ).fit(X_train_scaled, y_train)
  y_pred = mlp.predict(X_test_scaled)
  acc, prec, rec, f1 = (
      accuracy_score(y_test, y_pred),
      precision_score(y_test, y_pred, zero_division=0),
      recall_score(y_test, y_pred, zero_division=0),
      f1_score(y_test, y_pred, zero_division=0),
  )
  results.append((str(arch), acc, prec, rec, f1, mlp.n_layers_))
  models[str(arch)] = mlp
  print(
      f'{str(arch):15s} Acc={acc:.4f} Prec={prec:.4f} Rec={rec:.4f} F1={f1:.4f}'
  )

results_df = pd.DataFrame(
    results, columns=['Architecture', 'Accuracy', 'Precision', 'Recall', 'F1', 'Layers']
)
print(results_df)

plt.figure(figsize=(8, 5))
plt.bar(results_df['Architecture'], results_df['Accuracy'], color='steelblue')
plt.ylabel('Test Accuracy'), plt.xlabel('Hidden Layer Architecture'), plt.title(
    'Effect of MLP Architecture on Test Accuracy'
)
plt.xticks(rotation=20), plt.tight_layout(), plt.show()

best_arch = results_df.loc[results_df['F1'].idxmax(), 'Architecture']
best_model = models[best_arch]

plt.figure(figsize=(7, 4))
plt.plot(best_model.loss_curve_, color='crimson')
plt.xlabel('Epoch'), plt.ylabel('Training Loss'), plt.title(
    f'Training Loss Curve — Best Architecture {best_arch}'
)
plt.grid(alpha=0.3), plt.show()

y_pred_best = best_model.predict(X_test_scaled)
print(
    f'Best architecture: {best_arch}\nConfusion'
    f' Matrix:\n{confusion_matrix(y_test, y_pred_best)}'
)