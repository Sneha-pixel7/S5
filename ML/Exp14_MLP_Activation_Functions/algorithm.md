# Algorithm: Impact of Activation Functions in Multi-Layer Perceptrons on MNIST

1. **Load & Normalize MNIST**:
   - Download the full MNIST handwritten digit dataset ($70,000$ images of size $28 \times 28$).
   - Normalize pixel intensity values to $[0.0, 1.0]$ by dividing by 255.0.
   - Split into train (85%) and test (15%) sets (random_state=42).

2. **Define Multi-Layer Architecture**:
   - Fixed topology: Two hidden layers with 128 and 64 neurons: `hidden_layer_sizes=(128, 64)`.
   - Set fixed budget of `max_iter=25` epochs for direct convergence comparison.

3. **Train Across Activation Functions**:
   - For each activation `act` in `['logistic', 'tanh', 'relu']`:
     - Initialize `MLPClassifier(hidden_layer_sizes=(128, 64), activation=act, max_iter=25, random_state=42)`.
     - Fit network on $(X_{\text{train}}, y_{\text{train}})$.
     - Record training loss trajectory: `history_loss[act] = mlp.loss_curve_`.
     - Predict on test set and calculate accuracy: `test_accuracies[act]`.

4. **Analyze Mathematical Properties**:
   - **Logistic (Sigmoid)**: $f(z) = \frac{1}{1 + e^{-z}}$. Prone to vanishing gradients in saturation regions.
   - **Tanh**: $f(z) = \tanh(z)$. Zero-centered outputs improve gradient flow over sigmoid, but still saturates at extremes.
   - **ReLU**: $f(z) = \max(0, z)$. Constant derivative of $1$ for positive inputs prevents gradient decay and enables rapid convergence.

5. **Visualize**:
   - Plot comparative training loss curves (Loss vs. Epochs) for Logistic, Tanh, and ReLU on a single figure.
   - Visually demonstrate ReLU's steep, superior loss reduction within 25 epochs.
