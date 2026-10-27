# Experiment 04: Logistic Regression from Scratch vs Scikit-Learn

## What is this experiment all about?
When you want to answer a Yes/No question—like *"Is this tumor benign (harmless) or malignant (cancerous)?"*—linear regression won't work because it can output numbers like $-5$ or $+200$. We need probabilities between 0% and 100%.

**Logistic Regression** squashes any number into a probability between 0 and 1 using the S-shaped **Sigmoid function**. If the probability is 0.5 (50%) or higher, we predict class 1; otherwise, class 0.

To truly understand how machine learning works under the hood, this experiment builds a complete logistic regression classifier from scratch using basic math and matrix operations in NumPy, and tests it against Python's official `scikit-learn` library.

## What is the code actually doing?
1. **Loads tumor measurements**: Uses the Wisconsin Breast Cancer dataset (cell nucleus measurements like radius, texture, and smoothness).
2. **Scales numbers**: Standardizes the measurements so gradient descent steps remain steady.
3. **Builds the model from scratch**:
   - Implements the Sigmoid formula: $\sigma(z) = 1 / (1 + e^{-z})$.
   - Implements Gradient Descent: starts with zero weights and calculates error gradients step-by-step for 1,000 rounds.
   - Makes predictions: any test sample with predicted probability $\ge 0.5$ is classified as 1, else 0.
4. **Trains Scikit-Learn's prebuilt model**: Runs `LogisticRegression()` on the exact same data as a gold-standard reference.
5. **Compares head-to-head**: Evaluates Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. Both methods achieve virtually identical, high-accuracy classification scores.

## How to run
```bash
python exp4.py
```
