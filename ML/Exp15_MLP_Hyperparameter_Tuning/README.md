# Experiment 15: MLP Hyperparameter Tuning on Fashion-MNIST

## What is this experiment all about?
Training a neural network is like tuning a high-performance sports car: you have several knobs (called **Hyperparameters**) that you must calibrate before you start driving:

1. **Learning Rate ($\eta$)**: How big of a leap the network takes when updating its weights.
   - Too low ($0.001$): It learns at a snail's pace and barely improves within limited epochs.
   - Higher ($0.1$): It learns aggressively and reaches good accuracy quickly.
2. **Batch Size ($B$)**: How many clothing images the network looks at before doing a math update to its weights.
   - Small batch ($32$): Frequent updates with healthy noise that helps shake the network out of bad local minima.
   - Large batch ($256$): Smoother, faster GPU computation per epoch, but fewer total weight updates per epoch.
3. **Epochs**: How many complete times the network reads through the entire training dataset ($10$ vs. $20$ rounds).

To find the winning configuration, we run a **Grid Search**: testing every single combination of these knobs side-by-side.

## What is the code actually doing?
1. **Loads Fashion-MNIST clothing images**: Takes 10,000 stratified samples (shoes, shirts, coats, trousers, etc.) to keep the grid search fast and practical.
2. **Defines the search grid**:
   - 2 Learning Rates: $0.001$ and $0.1$
   - 2 Batch Sizes: $32$ and $256$
   - 2 Epoch budgets: $10$ and $20$
   - **Total**: $2 \times 2 \times 2 = 8$ distinct training runs.
3. **Trains a 2-layer MLP for all 8 configurations**: Uses Stochastic Gradient Descent (`solver='sgd'`) with ReLU activation on a `(128, 64)` hidden-layer network.
4. **Tracks stopwatch time & accuracy**: Records the exact training time in seconds and test accuracy for each setup.
5. **Displays summary & rankings**:
   - Prints a complete performance table ranking all 8 configurations.
   - Plots a horizontal bar chart of accuracy across all configurations so you can visually spot the champion setup at a glance.

## How to run
```bash
python exp15.py
```
