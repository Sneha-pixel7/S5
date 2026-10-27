# Algorithm: Simple Linear Regression

1. **Load & Preprocess Data**:
   - Fetch California Housing data; extract feature `AveRooms` ($X$) and target `MedHouseVal` ($y$).
   - Filter outliers (`AveRooms < 10` and `MedHouseVal < 5`).
   - Split into train (80%) and test (20%) sets; standardize $X$ using `StandardScaler`.

2. **Train via Gradient Descent**:
   - Initialize $\theta_0 = 0$, $\theta_1 = 0$, $\alpha = 0.01$, $\text{epochs} = 1000$.
   - Repeat for 1000 iterations:
     - Compute error: $e = (\theta_0 + \theta_1 X) - y$
     - Update parameters: $\theta_0 \leftarrow \theta_0 - \alpha \cdot \text{mean}(e)$, $\theta_1 \leftarrow \theta_1 - \alpha \cdot \text{mean}(e \cdot X)$
     - Record cost: $J = \frac{1}{2} \text{mean}(e^2)$

3. **Train via Normal Equation**:
   - Add bias column of 1s: $X_b = [1, X]$.
   - Solve closed-form weights: $\theta = (X_b^T X_b)^{-1} X_b^T y$.

4. **Evaluate & Compare**:
   - Predict test values for both methods: $\hat{y} = \theta_0 + \theta_1 X_{\text{test}}$.
   - Compute MSE, RMSE, and $R^2$ score for both.

5. **Visualize**:
   - Plot cost vs. epochs for Gradient Descent.
   - Plot regression lines from both methods over the test scatter data.
