# Algorithm: Binary Logistic Regression from Scratch vs Scikit-Learn

1. **Load & Scale Data**:
   - Load Breast Cancer Wisconsin dataset (30 features, binary label: benign vs. malignant).
   - Split into train (80%) and test (20%) sets; standardize features with `StandardScaler`.

2. **Train from Scratch via Gradient Descent**:
   - Define Sigmoid: $\sigma(z) = \frac{1}{1 + e^{-z}}$.
   - Augment training matrix with bias column: $X_b = [1, X]$.
   - Initialize weights $\mathbf{w} = \mathbf{0}$. Set learning rate $\alpha = 0.1$, $\text{epochs} = 1000$.
   - Loop for 1000 epochs:
     - Compute probabilities: $\mathbf{p} = \sigma(X_b \mathbf{w})$
     - Compute gradient: $\nabla = \frac{1}{m} X_b^T (\mathbf{p} - \mathbf{y})$
     - Update weights: $\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla$

3. **Inference (Scratch)**:
   - Compute test probabilities: $\mathbf{p}_{\text{test}} = \sigma([1, X_{\text{test}}] \mathbf{w})$.
   - Predict binary class: $\hat{y} = 1$ if $p \ge 0.5$, else $0$.

4. **Train Scikit-Learn Baseline**:
   - Fit `LogisticRegression(max_iter=1000)` on scaled training data and predict on test data.

5. **Evaluate & Compare**:
   - Calculate Accuracy, Precision, Recall, F1-Score, and Confusion Matrix for both implementations.
   - Verify that the scratch implementation matches the scikit-learn benchmark.
