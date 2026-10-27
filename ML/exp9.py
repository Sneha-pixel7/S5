import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

np.random.seed(42)
n = 800
df = pd.DataFrame({
    'Recency_Tier': np.random.choice(
        ['Recent', 'Dormant', 'At-Risk'], n, p=[0.5, 0.3, 0.2]
    ),
    'Frequency_Tier': np.random.choice(
        ['Low', 'Medium', 'High'], n, p=[0.4, 0.4, 0.2]
    ),
    'Monetary_Tier': np.random.choice(
        ['Low', 'Medium', 'High'], n, p=[0.3, 0.5, 0.2]
    ),
    'Segment': np.random.choice(['Bronze', 'Silver', 'Gold'], n, p=[0.4, 0.4, 0.2]),
})

for col in ['Recency_Tier', 'Frequency_Tier', 'Monetary_Tier']:
  df[col] = df[col].astype('category').cat.codes
df['Segment'] = df['Segment'].map({'Bronze': 0, 'Silver': 1, 'Gold': 2})

X, y = df.drop('Segment', axis=1), df['Segment']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print(df.head())

clf_tree = DecisionTreeClassifier(
    criterion='entropy', max_depth=3, random_state=42
).fit(X_train, y_train)
y_pred = clf_tree.predict(X_test)
print(f'Model Classification Accuracy: {accuracy_score(y_test, y_pred):.4f}')

plt.figure(figsize=(14, 8))
plot_tree(
    clf_tree,
    feature_names=list(X.columns),
    class_names=['Bronze', 'Silver', 'Gold'],
    filled=True,
    rounded=True,
)
plt.title('Customer Segmentation Decision Tree Structure (Entropy/ID3 Split)')
plt.tight_layout()
plt.show()

feat_imp = pd.Series(clf_tree.feature_importances_, index=X.columns).sort_values(
    ascending=False
)
plt.figure(figsize=(8, 4))
feat_imp.plot(kind='bar', color='teal')
plt.ylabel('Relative Importance Scaling')
plt.title('RFM Feature Importance Breakdown')
plt.tight_layout()
plt.show()
print('\nFeature Importance Metrics:\n', feat_imp)