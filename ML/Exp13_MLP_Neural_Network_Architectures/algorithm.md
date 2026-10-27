# Algorithm: Multi-Layer Perceptron (MLP) Architecture Exploration

1. **Load & Preprocess Wine Dataset**:
   - Download the UCI Red Wine Quality dataset (11 chemical features, quality score 3–8).
   - Formulate binary target `good_quality`: 1 if `quality >= 7`, else 0.
   - Split into train (80%) and test (20%) sets with stratification; scale features with `StandardScaler`.

2. **Train Baseline Network**:
   - Fit a shallow baseline: `MLPClassifier(hidden_layer_sizes=(8,), activation='relu', max_iter=500, random_state=42)`.
   - Record test accuracy.

3. **Systematic Topology Search**:
   - Define network architectures to compare:
     `architectures = [(4,), (16,), (64,), (16, 8), (32, 16, 8)]`.
   - For each architecture `arch`:
     - Fit `MLPClassifier(hidden_layer_sizes=arch, activation='relu', max_iter=1000, random_state=42)` on scaled training data.
     - Predict on scaled test data.
     - Compute Accuracy, Precision, Recall, and F1-Score; record total layer count.
     - Save the trained model instance.

4. **Identify Optimal Network**:
   - Select the architecture yielding the highest test F1-score (`best_arch`).

5. **Visualize**:
   - Bar chart comparing test accuracies across all tested architectures.
   - Training loss curve (`best_model.loss_curve_`) across epochs to verify convergence stability.
   - Confusion matrix for the best architecture.
