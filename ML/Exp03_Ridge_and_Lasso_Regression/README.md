# Experiment 03: Regularized Linear Regression (Ridge & Lasso)

## What is this experiment all about?
When you have many features predicting an outcome (like age, blood pressure, cholesterol, and blood sugar predicting diabetes progression), standard linear regression can become overconfident. It might assign enormous, unrealistic weights to noisy features, making predictions brittle on new data.

**Regularization** acts like a speed governor on the model: it penalizes large weights so the model stays simple and reliable:
- **Ridge Regression ($L_2$)**: Shrinks all feature weights down gently toward zero. Every feature still contributes a little bit.
- **Lasso Regression ($L_1$)**: Shrinks weights aggressively and forces useless or redundant features completely to zero, effectively acting as an automatic feature selector.
- **Ordinary Least Squares (OLS)**: Standard regression with no penalties at all.

## What is the code actually doing?
1. **Loads diabetes data**: Takes 10 health measurements from diabetes patients.
2. **Standardizes numbers**: Scales all features so each has mean 0 and standard deviation 1 (ensuring no single large-scale measurement dominates the penalty unfairly).
3. **Picks the best penalty strength ($\alpha$)**: Uses 5-fold cross-validation (`RidgeCV` and `LassoCV`) to automatically discover the optimal regularization strength.
4. **Trains all 3 models**: Fits OLS, Ridge, and Lasso side-by-side.
5. **Compares feature weights & accuracy**:
   - Compares the learned coefficients: you'll see Lasso zeroing out unimportant features while Ridge scales them down.
   - Evaluates test accuracy ($R^2$) and prediction errors (MSE, RMSE).
6. **Draws comparison charts**: Displays a grouped bar chart of the feature weights and an $R^2$ score comparison.

## How to run
```bash
python exp3.py
```
