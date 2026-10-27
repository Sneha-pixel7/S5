# Algorithm: Impact of Feature Scaling on Logistic Regression

1. **Load Data**:
   - Download Pima Indians Diabetes dataset (8 clinical predictors, 1 binary outcome).
   - Split into train (70%) and test (30%) sets (random_state=42).

2. **Train Unscaled Model**:
   - Train `LogisticRegression(solver='saga', max_iter=1000)` directly on raw $X_{\text{train}}$.
   - Predict on raw $X_{\text{test}}$ and record learned coefficients.

3. **Standardize Features**:
   - Fit `StandardScaler` on $X_{\text{train}}$ to calculate mean $\mu$ and std $\sigma$.
   - Transform both train and test sets: $z = \frac{x - \mu}{\sigma}$.

4. **Train Scaled Model**:
   - Train an identical `LogisticRegression(solver='saga', max_iter=1000)` on standardized $X_{\text{train\_scaled}}$.
   - Predict on standardized $X_{\text{test\_scaled}}$ and record learned coefficients.

5. **Compare & Visualize**:
   - Compute Accuracy, Precision, Recall, and F1-Score for both unscaled and scaled pipelines.
   - Plot a bar chart comparing learned feature weight coefficients.
   - Observe how scaling prevents features with large numeric scales (e.g., Insulin) from dominating gradient steps, yielding balanced, interpretable weights.
