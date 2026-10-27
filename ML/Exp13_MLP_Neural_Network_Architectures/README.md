# Experiment 13: MLP Neural Network Architectures

## What is this experiment all about?
A **Multi-Layer Perceptron (MLP)** is the foundation of modern Artificial Neural Networks. It is built out of interconnected layers of "neurons":
- **Input Layer**: Receives the raw features.
- **Hidden Layers**: Perform non-linear transformations, extracting higher-level concepts and relationships.
- **Output Layer**: Produces the final prediction.

One of the biggest questions in deep learning is: **How deep and wide should your network be?**
- Too shallow or narrow (e.g., just 4 neurons), and it might fail to learn subtle patterns (underfitting).
- Too deep or wide (e.g., multiple big layers), and it might memorize noise, take longer to compute, or overfit.

In this experiment, we explore different network shapes (shallow single layers vs. multi-layer deep networks) on chemical wine data to predict whether a bottle of wine is high quality (rating $\ge 7$).

## What is the code actually doing?
1. **Loads wine lab tests**: Reads 1,599 red wine records containing 11 chemical properties (acidity, volatile acidity, citric acid, residual sugar, chlorides, sulfur dioxide, density, pH, sulphates, and alcohol).
2. **Defines binary quality**: Marks wines with a score of 7 or higher as "Good" (1) and all others as "Average" (0).
3. **Scales the chemistry metrics**: Uses `StandardScaler` so differences in units (e.g., pH around 3 vs. sulfur dioxide in 100s) don't unbalance the neural weights.
4. **Trains a range of network designs**:
   - Single-layer: 4 neurons `(4,)`, 16 neurons `(16,)`, 64 neurons `(64,)`
   - Multi-layer: 2 layers `(16, 8)` and 3 layers `(32, 16, 8)`
5. **Evaluates performance**: Measures Accuracy, Precision, Recall, and F1-Score for every topology and selects the best performer.
6. **Draws loss & performance plots**:
   - Plots a bar chart showing how accuracy changes across architectures.
   - Plots the training loss curve over time for the winning design to verify smooth gradient descent convergence.
   - Displays a confusion matrix of test predictions.

## How to run
```bash
python exp13.py
```
