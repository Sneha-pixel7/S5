# Algorithm: Maximum Likelihood Estimation (MLE) vs Maximum A Posteriori (MAP)

1. **Load & Scale Data**:
   - Load Breast Cancer dataset; split into train (80%) and test (20%) sets.
   - Standardize features using `StandardScaler`.

2. **Fit MLE (Unregularized / Uniform Prior)**:
   - Train `LogisticRegression(penalty=None, solver='lbfgs')`.
   - Maximize likelihood: $\hat{\mathbf{w}}_{\text{MLE}} = \arg\max \sum \log P(y_i | \mathbf{x}_i; \mathbf{w})$.
   - Extract weight vector $\mathbf{w}_{\text{MLE}}$, compute test accuracy and weight norm $\sum w^2$.

3. **Fit MAP $L_2$ (Gaussian Prior)**:
   - Train `LogisticRegression(penalty='l2', C=0.1, solver='lbfgs')`.
   - Assume zero-mean Gaussian prior $\mathbf{w} \sim \mathcal{N}(0, \sigma^2)$; minimizes loss $+ \lambda \|\mathbf{w}\|_2^2$.
   - Extract weights $\mathbf{w}_{L_2}$, compute test accuracy and weight norm.

4. **Fit MAP $L_1$ (Laplace Prior)**:
   - Train `LogisticRegression(penalty='l1', C=0.1, solver='saga')`.
   - Assume zero-mean Laplace prior $P(\mathbf{w}) \propto e^{-|\mathbf{w}|/b}$; minimizes loss $+ \lambda \|\mathbf{w}\|_1$.
   - Extract weights $\mathbf{w}_{L_1}$, compute test accuracy, and count zeroed weights (sparsity).

5. **Compare & Visualize**:
   - Tabulate weight comparisons across the first 10 features for MLE, MAP $L_2$, and MAP $L_1$.
   - Plot weight profile across features: observe large unconstrained weights in MLE, smooth shrinkage in MAP $L_2$, and true sparsity in MAP $L_1$.
