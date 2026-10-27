# Algorithm: Regularized Linear Regression (Ridge vs Lasso vs OLS)

1. **Load & Scale Data**:
   - Load Diabetes dataset (10 clinical features, 1 disease progression target).
   - Split into train (80%) and test (20%) sets.
   - Standardize training and test features using `StandardScaler`.

2. **Optimize Penalty Parameter ($\alpha$)**:
   - Define search space of 50 log-spaced $\alpha$ values from $10^{-3}$ to $10^2$.
   - Find best $\alpha$ for Ridge via 5-fold cross-validation (`RidgeCV`).
   - Find best $\alpha$ for Lasso via 5-fold cross-validation (`LassoCV`).

3. **Train Models**:
   - Fit unregularized Ordinary Least Squares (`LinearRegression`).
   - Fit `Ridge` with optimal $\alpha$ (minimizes $\text{SSE} + \lambda \|\mathbf{w}\|_2^2$).
   - Fit `Lasso` with optimal $\alpha$ (minimizes $\text{SSE} + \lambda \|\mathbf{w}\|_1$).

4. **Evaluate & Inspect Weights**:
   - Predict test values for all three models; compute MSE, RMSE, and $R^2$.
   - Observe feature coefficients: Ridge shrinks weights uniformly, while Lasso zeroes out redundant features (feature selection).

5. **Visualize**:
   - Bar chart comparing coefficient weights across all 10 features for OLS, Ridge, and Lasso.
   - Bar chart comparing final $R^2$ scores across the models.
