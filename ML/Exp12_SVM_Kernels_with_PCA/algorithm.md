# Algorithm: Support Vector Machine (SVM) Kernels with PCA on Fashion-MNIST

1. **Load & Subsample Images**:
   - Load Fashion-MNIST dataset; subsample a stratified set of 6,000 images across 10 clothing categories.
   - Flatten images to 784-dimensional vectors; scale pixel intensities to $[0.0, 1.0]$.
   - Split into train (80%) and test (20%) sets with stratification (random_state=42).

2. **Standardize & Reduce Dimensionality (PCA)**:
   - Standardize features using `StandardScaler`.
   - Apply `PCA(n_components=50)`: project feature space from 784 dimensions down to 50 principal components while retaining dominant variance.

3. **Train & Benchmark Kernels**:
   - **Linear Kernel**: Train `SVC(kernel='linear', C=1.0)`. Record training time and predict on test set.
   - **Polynomial Kernel**: Train `SVC(kernel='poly', degree=3, C=1.0)`. Record training time and predict on test set.
   - **RBF Kernel**: Train `SVC(kernel='rbf', C=1.0)`. Record training time and predict on test set.

4. **Evaluate Metrics**:
   - For each kernel, calculate Accuracy, Macro Precision, Macro Recall, Macro F1-Score, and Training Duration.
   - Assemble results into a comparison table and determine the optimal kernel (RBF).

5. **Visualize**:
   - Bar chart comparing test accuracies across the three SVM kernels.
   - Confusion Matrix heatmap for the best-performing kernel (RBF) with category labels.
