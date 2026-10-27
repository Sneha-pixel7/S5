import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# 1. Load & Preprocess Data
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv'
df = pd.read_csv(url).dropna(subset=['displacement', 'mpg'])
X, y = df[['displacement']].values, df['mpg'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Train & Evaluate Models across Degrees
degrees = [1, 2, 3, 4, 6, 8]
models = {}

for d in degrees:
  poly = PolynomialFeatures(degree=d, include_bias=False)
  Xtr_p, Xte_p = poly.fit_transform(X_train), poly.transform(X_test)
  model = LinearRegression().fit(Xtr_p, y_train)
  pred = model.predict(Xte_p)
  mse, r2 = mean_squared_error(y_test, pred), r2_score(y_test, pred)
  models[d] = (poly, model)
  print(f'Degree {d:2d} | MSE: {mse:.4f} | RMSE: {mse**0.5:.4f} | R2: {r2:.4f}')

# 3. Visualization
xs = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Fitted curves
ax1.scatter(X_test, y_test, alpha=0.4, s=15, color='steelblue', label='Data')
for d, color in zip([1, 2, 4, 8], ['black', 'crimson', 'green', 'orange']):
  poly, model = models[d]
  ax1.plot(
      xs,
      model.predict(poly.transform(xs)),
      color=color,
      lw=2,
      label=f'Deg {d}',
  )
ax1.set(title='Polynomial Fits', xlabel='Displacement', ylabel='MPG')
ax1.legend()

# Performance curve
ax2.plot(
    degrees,
    [r2_score(y_test, models[d][1].predict(models[d][0].transform(X_test))) for d in degrees],
    marker='o',
    color='crimson',
)
ax2.set(title='R² vs Degree', xlabel='Degree', ylabel='R² Score')
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()