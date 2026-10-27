# Algorithm: Logistic Regression vs Decision Tree Classifier

1. **Load & Clean Census Data**:
   - Download the UCI Adult Census Income dataset; assign standard column names.
   - Replace missing values (`'?'`) with `NaN` and drop incomplete rows.
   - Binarize target `income`: 1 if `>50K`, else 0.

2. **Feature Engineering**:
   - Apply one-hot dummy encoding (`pd.get_dummies(..., drop_first=True)`) on categorical features (workclass, education, marital status, occupation, relationship, sex).
   - Combine with numerical features (age, education-num, gain, loss, hours).
   - Split dataset into train (75%) and test (25%) sets (random_state=42).

3. **Train Logistic Regression (Linear Model)**:
   - Scale features using `StandardScaler` (fit on train, transform train and test).
   - Fit `LogisticRegression(max_iter=1000, random_state=42)` on scaled training data.
   - Predict classes on scaled test data.

4. **Train Decision Tree (Non-Linear Model)**:
   - Fit `DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=42)` directly on unscaled training data.
   - Predict classes on unscaled test data.

5. **Compare Metrics**:
   - Compute Accuracy, Precision, Recall, and F1-Score for both models.
   - Assemble results into a comparative evaluation matrix and analyze linear vs. hierarchical non-linear decision boundaries.
