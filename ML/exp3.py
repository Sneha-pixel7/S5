import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, LassoCV, LinearRegression, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load & Preprocess Data
df = load_diabetes(as_frame=True).frame
X, y = df.drop(columns=['target']).values, df['target'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

# 2. Train Models with Cross-Validation for Alpha
alphas = np.logspace(-3, 2, 50)
lin = LinearRegression().fit(X_train_sc, y_train)
ridge = Ridge(alpha=RidgeCV(alphas=alphas, cv=5).fit(X_train_sc, y_train).alpha_).fit(X_train_sc, y_train)
lasso = Lasso(alpha=LassoCV(alphas=alphas, cv=5, max_iter=10000).fit(X_train_sc, y_train).alpha_, max_iter=10000).fit(X_train_sc, y_train)

# 3. Evaluate & Print Metrics
models = {'Linear': lin, 'Ridge': ridge, 'Lasso': lasso}
results = []
for name, m in models.items():
  pred = m.predict(X_test_sc)
  mse, r2 = mean_squared_error(y_test, pred), r2_score(y_test, pred)
  results.append({'Model': name, 'MSE': mse, 'RMSE': mse**0.5, 'R2': r2})
  print(f'{name:18s} | MSE: {mse:.4f} | RMSE: {mse**0.5:.4f} | R2: {r2:.4f}')
results_df = pd.DataFrame(results)

# 4. Visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 4))
features = df.drop(columns=['target']).columns
x_pos, width = np.arange(len(features)), 0.25

# Coefficients Comparison
axes[0].bar(x_pos - width, lin.coef_, width, label='Linear', color='steelblue')
axes[0].bar(x_pos, ridge.coef_, width, label='Ridge', color='crimson')
axes[0].bar(x_pos + width, lasso.coef_, width, label='Lasso', color='green')
axes[0].set_xticks(x_pos)
axes[0].set_xticklabels(features, rotation=45)
axes[0].set_title('Coefficient Comparison')
axes[0].legend()
axes[0].axhline(0, color='black', lw=0.8)

# R² Score Comparison
axes[1].bar(results_df['Model'], results_df['R2'], color=['steelblue', 'crimson', 'green'])
axes[1].set_title('R² Score Comparison')
axes[1].set_ylabel('R² Score')

plt.tight_layout()
plt.show()