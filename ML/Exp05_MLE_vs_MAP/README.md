# Experiment 05: MLE vs MAP (Probabilistic Regularization)

## What is this experiment all about?
When a machine learning model learns weights, where do those weights come from? There are two statistical philosophies:

1. **Maximum Likelihood Estimation (MLE)**:
   - *"Only trust the data we collected."*
   - It assumes nothing beforehand (a uniform, flat prior). It picks whichever weights fit the training samples best.
   - **The Catch**: If there is noise or correlated features, weights can blow up to huge, erratic numbers to squeeze out every drop of training fit.

2. **Maximum A Posteriori (MAP)**:
   - *"Trust the data, but balance it with common sense (Prior Belief)."*
   - **Gaussian Prior (Bell curve around 0)**: We believe weights shouldn't be massive. Mathematically, this produces **$L_2$ Ridge Regularization** (shrinks all weights smoothly).
   - **Laplace Prior (Sharp peak at 0)**: We believe most features are irrelevant. Mathematically, this produces **$L_1$ Lasso Regularization** (forces unnecessary weights to exactly 0).

## What is the code actually doing?
1. **Loads breast cancer data**: Takes 30 cellular characteristics and standardizes them.
2. **Trains Model 1 (MLE)**: Runs unregularized logistic regression (`penalty=None`). It fits the data with completely unconstrained weights.
3. **Trains Model 2 (MAP $L_2$ / Gaussian)**: Runs logistic regression with $L_2$ penalty (`C=0.1`).
4. **Trains Model 3 (MAP $L_1$ / Laplace)**: Runs logistic regression with $L_1$ penalty (`C=0.1`).
5. **Inspects the learned weights**:
   - Compares the total squared size of the weights (sum of squared coefficients) to show how MAP tames giant weights.
   - Counts how many weights were knocked down to exactly zero by MAP $L_1$ (sparsity).
6. **Plots the parameter estimates**: Draws a line chart showing the weights for the first 15 features across all three methods so you can visually verify shrinkage and sparsity.

## How to run
```bash
python exp5.py
```
