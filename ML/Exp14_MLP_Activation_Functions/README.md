# Experiment 14: Neural Network Activation Functions on MNIST

## What is this experiment all about?
In an artificial neural network, every neuron computes a weighted sum of its inputs and then passes that number through an **Activation Function**.

Why do we need an activation function?
Without one, stacking even 100 neural network layers would just collapse mathematically into one simple linear equation! Activation functions introduce **non-linearity**, allowing neural networks to learn handwriting, faces, speech, and complex real-world relationships.

This experiment compares the three most famous activation functions on handwritten digit recognition:
1. **Logistic (Sigmoid)**: $\sigma(z) = 1 / (1 + e^{-z})$. Squeezes numbers between 0 and 1.
   - **The Flaw**: When numbers are large or small, the curve goes completely flat. Its slope (derivative) drops near zero, causing the **Vanishing Gradient Problem**—deeper layers learn painfully slowly.
2. **Tanh (Hyperbolic Tangent)**: Squeezes numbers between $-1$ and $+1$. Because it is centered around zero, gradient updates flow better than Sigmoid, but it still flattens out at the ends.
3. **ReLU (Rectified Linear Unit)**: $f(z) = \max(0, z)$. If the input is positive, the output equals the input (constant slope of 1). It never flattens out for positive numbers, completely dodging vanishing gradients and training drastically faster!

## What is the code actually doing?
1. **Loads MNIST handwritten digits**: Takes 70,000 real images of handwritten numbers 0 through 9, flattening each $28 \times 28$ image into 784 normalized grayscale inputs.
2. **Fixes the network architecture**: Builds a 2-hidden-layer network with 128 neurons in the first layer and 64 neurons in the second layer.
3. **Trains under each activation for 25 epochs**:
   - Trains using Logistic (Sigmoid)
   - Trains using Tanh
   - Trains using ReLU
4. **Tracks training loss per epoch**: Records how quickly the loss drops epoch-by-epoch for all three functions.
5. **Plots the convergence curves**: Displays a side-by-side loss graph clearly proving how ReLU drops down rapidly within just a few rounds while Sigmoid struggles to make progress.

## How to run
```bash
python exp14.py
```
