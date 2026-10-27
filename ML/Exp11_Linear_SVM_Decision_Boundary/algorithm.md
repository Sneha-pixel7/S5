# Algorithm: Linear Support Vector Machine (SVM) Decision Boundary & Margin Visualization

1. **Load & Prepare Data**:
   - Load Fisher's Iris dataset; inspect petal dimensions across species.
   - Formulate binary classification task: Setosa ($y = 1$) vs. Non-Setosa ($y = 0$) using two features (`petal length` and `petal width`).
   - Split into train (80%) and test (20%) sets with stratification; scale features using `StandardScaler`.

2. **Train Linear SVM**:
   - Fit `SVC(kernel='linear', C=1.0)` on scaled training data.
   - Solve maximal margin optimization:
     $$\min \frac{1}{2} \|\mathbf{w}\|^2 + C \sum \xi_i \quad \text{s.t.} \quad y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i$$
   - Predict binary classes on scaled test data.

3. **Evaluate**:
   - Compute Test Accuracy, Precision, Recall, F1-Score, and print Confusion Matrix.

4. **Visualize Hyperplane, Margins & Support Vectors**:
   - Inverse-transform coordinates back to original physical scale (cm).
   - Generate a 2D meshgrid across the feature space and evaluate the decision function $Z = \mathbf{w}^T \mathbf{x} + b$.
   - Draw contour lines:
     - $Z = 0$: Optimal separating hyperplane (solid line).
     - $Z = \pm 1$: Margin boundaries (dashed lines).
   - Highlight the critical support vector samples (`model.support_vectors_`) with distinct circular markers.
