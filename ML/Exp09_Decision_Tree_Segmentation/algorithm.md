# Algorithm: Customer Segmentation using Decision Tree (ID3 / Information Gain)

1. **Generate & Encode Dataset**:
   - Synthesize $n = 800$ customer profiles with Recency, Frequency, and Monetary tiers and target Segments (`Bronze`, `Silver`, `Gold`).
   - Encode categorical tiers into numerical codes and map segments to $\{0, 1, 2\}$.
   - Split data into train (75%) and test (25%) sets (random_state=42).

2. **Fit Decision Tree Classifier**:
   - Initialize `DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)`.
   - Compute node splits using Shannon Entropy and Information Gain:
     $$\text{IG}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$$
   - Apply pre-pruning constraint (`max_depth=3`) to prevent overfitting.
   - Fit model on $X_{\text{train}}$ and predict on $X_{\text{test}}$.

3. **Evaluate**:
   - Compute test classification accuracy.
   - Extract Mean Decrease in Impurity (MDI) feature importances from `clf_tree.feature_importances_`.

4. **Visualize**:
   - Render the complete tree diagram using `plot_tree()` showing decision rules, entropy, and class distributions at every node.
   - Plot a bar chart ranking the relative feature importances of Recency, Frequency, and Monetary features.
