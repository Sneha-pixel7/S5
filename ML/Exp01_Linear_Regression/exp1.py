import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load & Preprocess Data
df = fetch_california_housing(as_frame=True).frame
X, y = df[['AveRooms']].values, df['MedHouseVal'].values
mask = (X.flatten() < 10) & (y < 5)
X, y = X[mask], y[mask]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_sc, X_test_sc = scaler.fit_transform(X_train), scaler.transform(X_test)


# 2. Gradient Descent
def gradient_descent(X, y, lr=0.01, epochs=1000):
  X_flat = X.flatten()
  t0, t1, costs = 0.0, 0.0, []
  for _ in range(epochs):
    err = (t0 + t1 * X_flat) - y
    t0 -= lr * err.mean()
    t1 -= lr * (err * X_flat).mean()
    costs.append(0.5 * (err**2).mean())
  return t0, t1, costs


t0_gd, t1_gd, costs = gradient_descent(X_train_sc, y_train)


# 3. Normal Equation
def normal_equation(X, y):
  X_b = np.c_[np.ones(len(X)), X]
  return tuple(np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y)


t0_ne, t1_ne = normal_equation(X_train_sc, y_train)

# 4. Evaluation
for name, t0, t1 in [
    ('Gradient Descent', t0_gd, t1_gd),
    ('Normal Equation', t0_ne, t1_ne),
]:
  pred = t0 + t1 * X_test_sc.flatten()
  mse = mean_squared_error(y_test, pred)
  print(
      f'{name:18s} | MSE: {mse:.4f} | RMSE: {mse**0.5:.4f} | R2:'
      f' {r2_score(y_test, pred):.4f}'
  )

# 5. Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(costs), axes[0].set_title('GD Cost Convergence')
for ax, (name, t0, t1) in zip(
    axes[1:],
    [('Gradient Descent', t0_gd, t1_gd), ('Normal Equation', t0_ne, t1_ne)],
):
  ax.scatter(X_test_sc, y_test, alpha=0.3, s=5, color='steelblue')
  xs = np.linspace(X_test_sc.min(), X_test_sc.max(), 200)
  ax.plot(xs, t0 + t1 * xs, color='crimson', lw=2)
  ax.set_title(name)
plt.tight_layout()
plt.show()