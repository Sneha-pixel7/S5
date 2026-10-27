# Algorithm: K-Nearest Neighbors (KNN) Classifier on Fashion-MNIST

1. **Load & Preprocess Data**:
   - Load Fashion-MNIST dataset; subsample 5,000 training images and 500 test images for computational efficiency.
   - Flatten 2D image matrices ($28 \times 28$) into 1D 784-dimensional vectors.
   - Normalize pixel intensity values to $[0.0, 1.0]$ by dividing by 255.0.

2. **Evaluate Hyperparameter $K$**:
   - For each neighborhood size $K \in [1, 3, 5, 11]$:
     - Initialize `KNeighborsClassifier(n_neighbors=K, metric='euclidean')`.
     - Index training data (fit step) and measure training time.
     - Classify test data (majority vote of $K$ nearest points) and measure inference latency (seconds).
     - Calculate Accuracy and Macro F1-Score.

3. **Analyze Results**:
   - Tabulate Accuracy, F1-Score, and Inference Delay across all tested $K$ values.
   - Observe trade-off: $K=1$ is susceptible to noise; higher $K$ values smooth decision boundaries but increase computation.

4. **Visualize**:
   - Plot a dual-axis graph displaying Test Accuracy (left Y-axis) and Inference Latency in seconds (right Y-axis) against $K$.
