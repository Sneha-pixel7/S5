# Algorithm: Polynomial Regression

1. **Load Data**:
   - Read Auto MPG dataset; drop rows with missing values in `displacement` ($X$) or `mpg` ($y$).
   - Split data into train (80%) and test (20%) sets.

2. **Fit Polynomial Models**:
   - For each degree $d \in [1, 2, 3, 4, 6, 8]$:
     - Generate polynomial features: $\phi(X) = [X, X^2, \dots, X^d]$ using `PolynomialFeatures`.
     - Fit an Ordinary Least Squares `LinearRegression` model on the transformed training features.
     - Predict on transformed test features and record MSE, RMSE, and $R^2$ score.

3. **Evaluate Trade-Off**:
   - Compare performance across degrees:
     - Degree 1: Underfitting (high bias).
     - Moderate degrees (2–4): Optimal fit with peak $R^2$.
     - High degrees (6–8): Overfitting (high variance).

4. **Visualize**:
   - Plot the fitted curves for degrees 1, 2, 4, and 8 over the actual test scatter points.
   - Plot $R^2$ score vs. degree to identify the best model complexity.
