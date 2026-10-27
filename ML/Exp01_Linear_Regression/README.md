# Experiment 01: Simple Linear Regression

## What is this experiment all about?
Imagine you want to predict house prices based on how many rooms a house has. In simple words, more rooms usually mean a higher price. Linear regression draws the single best-fitting straight line through your data points so you can make predictions on new houses.

There are two primary ways to find this best-fitting line:
1. **Gradient Descent**: An iterative, step-by-step guessing approach. It starts with random values and slowly nudges the line in small steps to reduce prediction errors until it settles on the best line.
2. **Normal Equation**: A direct, one-shot mathematical formula that calculates the exact best line instantly without needing any loops or steps.

## What is the code actually doing?
1. **Loads the data**: Fetches real California housing data and filters out extreme outlier values (houses with over 10 rooms or capped prices).
2. **Splits & scales**: Reserves 80% for training and 20% for testing, scaling the room count so numbers are small and easy to work with.
3. **Calculates the line twice**:
   - Runs a custom loop for 1000 steps using Gradient Descent to iteratively minimize error.
   - Computes the exact weights analytically in one line of math using the Normal Equation.
4. **Compares results**: Measures how well both methods did on test data using standard error metrics (MSE, RMSE, and $R^2$). Both arrive at essentially identical lines.
5. **Draws graphs**: Shows the error dropping down to a minimum over time and displays the final fitted lines drawn directly over the test data points.

## How to run
```bash
python exp1.py
```
