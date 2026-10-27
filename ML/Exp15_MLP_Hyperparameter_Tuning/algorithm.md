# Algorithm: Hyperparameter Grid Search for Multi-Layer Perceptron on Fashion-MNIST

1. **Load & Subsample Data**:
   - Download Fashion-MNIST dataset; normalize pixel values to $[0.0, 1.0]$.
   - Split into train (80%) and test (20%) sets with stratification.
   - Extract a representative stratified subset of 10,000 samples for efficient grid search.

2. **Define Hyperparameter Search Space**:
   - Define discrete parameter grid:
     - Learning Rates ($\eta$): $[0.001, 0.1]$
     - Mini-Batch Sizes ($B$): $[32, 256]$
     - Training Epochs: $[10, 20]$
   - Total configurations: $2 \times 2 \times 2 = 8$ combinations.

3. **Execute Grid Search Loop**:
   - For each combination of $(\eta, B, \text{epochs})$:
     - Initialize `MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='sgd', learning_rate_init=lr, batch_size=bs, max_iter=epochs, random_state=42)`.
     - Record training start time, fit model on the 10,000-sample training subset, record training duration.
     - Predict on test set and calculate classification accuracy percentage.
     - Store configuration parameters, runtime, and accuracy.

4. **Tabulate & Rank**:
   - Convert logged results into a summary DataFrame.
   - Rank configurations based on test accuracy vs. computational time.

5. **Visualize**:
   - Construct descriptive configuration tags (e.g., `LR:0.1|B:32|E:20`).
   - Plot a horizontal bar chart (`barh`) illustrating accuracy across all 8 configurations to identify the optimal hyperparameter combination.
