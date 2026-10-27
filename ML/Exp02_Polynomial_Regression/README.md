# Experiment 02: Polynomial Regression

## What is this experiment all about?
Not all data follows a straight line. For example, bigger car engines get lower miles per gallon (mpg), but the drop curves rather than going straight down.

If you draw a straight line through curved data, the model is too simple and misses the trend—this is called **underfitting** (high bias). But if you give the line too much freedom to curve (like degree 8), it bends wildly trying to pass through every single point including random noise—this is called **overfitting** (high variance).

Polynomial regression helps find the "sweet spot" curve that bends just enough to fit the real pattern without overcomplicating things.

## What is the code actually doing?
1. **Loads the car data**: Reads vehicle engine displacement and fuel economy (mpg) data.
2. **Creates powers of X**: Transforms the single engine size feature into powers ($X, X^2, X^3, \dots, X^d$) for different degrees ($1, 2, 3, 4, 6, 8$).
3. **Trains 6 different models**: Fits a regression model for each degree to see how curvature affects predictions.
4. **Compares accuracy**: Evaluates error (MSE) and accuracy ($R^2$) on unseen test cars.
5. **Draws curves**:
   - Plots curves of degrees 1, 2, 4, and 8 over the data scatter so you can clearly see underfitting (stiff line), good fit (smooth gentle curve), and overfitting (wild bends).
   - Plots $R^2$ score against degree to pinpoint where performance peaks.

## How to run
```bash
python exp2.py
```
