# Experiment 06: Feature Scaling in Classification

## What is this experiment all about?
Imagine calculating someone's health score using their:
- **Insulin level**: ranges from 0 to 800
- **Diabetes pedigree function**: ranges from 0.08 to 2.4

Without scaling, the computer sees 800 as hundreds of times more impactful than 0.5 purely because the number is bigger, not because it's actually more important!

Furthermore, gradient-based optimization algorithms (like SAGA or gradient descent) bounce and zig-zag erratically when one feature is huge and another is microscopic.

**Feature Scaling** (Standardization) levels the playing field: it subtracts the average and divides by the spread, centering every feature around 0 with a standard deviation of 1.

## What is the code actually doing?
1. **Loads real medical data**: Downloads the famous Pima Indians Diabetes dataset (8 health measurements including glucose, blood pressure, BMI, age, and insulin).
2. **Trains on RAW numbers**: Fits a logistic regression model directly on unscaled data and records how it performs and what weights it learns.
3. **Scales the features**: Transforms the features using `StandardScaler` so every column is on the same normalized scale.
4. **Trains on SCALED numbers**: Fits the exact same model configuration on the standardized numbers.
5. **Compares results**:
   - Prints a clear comparison table showing Accuracy, Precision, Recall, and F1-score for both cases.
   - Plots a side-by-side bar chart showing the weights learned by both models. You'll clearly see how unscaled weights are wildly distorted, whereas standardized weights properly reflect real biological risk factors.

## How to run
```bash
python exp6.py
```
