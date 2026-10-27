# Experiment 10: Logistic Regression vs Decision Trees

## What is this experiment all about?
When approaching a real-world classification task, you often face a fundamental design choice between two classic modeling approaches:

1. **Logistic Regression (Linear & Parametric)**:
   - Draws a straight, flat boundary (a line or plane) through your data.
   - Calculates a weighted sum of all inputs.
   - Requires feature scaling and works best when features combine additively to influence the outcome.
2. **Decision Tree (Non-Linear & Non-Parametric)**:
   - Makes axis-aligned "box" cuts through the data using sequential If-Then rules.
   - Doesn't need feature scaling and handles complex interactions naturally (e.g., *"If age > 30 AND married AND hours > 40"*).

In this experiment, we pit them against each other on the famous **Census Income dataset** to predict whether a citizen makes more than $50,000 per year based on their age, education, occupation, marital status, and hours worked.

## What is the code actually doing?
1. **Downloads census records**: Fetches real US Census data from the UCI Machine Learning repository.
2. **Cleans & encodes**:
   - Removes missing values (entries marked with `'?'`).
   - Converts the target label (Income $>50\text{K}$) into 1 and 0.
   - Performs One-Hot Encoding on categories like education and occupation into binary columns.
3. **Prepares training sets**: Splits the data 75/25 and standardizes the features for Logistic Regression (leaving the Decision Tree with raw features to demonstrate scaling invariance).
4. **Trains both models**:
   - Trains Logistic Regression with an iterative solver.
   - Trains a Decision Tree with entropy-based splits up to 5 levels deep.
5. **Compares performance**: Outputs a side-by-side performance table showing Accuracy, Precision, Recall, and F1-score to highlight which model captures real-world demographic patterns more effectively.

## How to run
```bash
python exp10.py
```
