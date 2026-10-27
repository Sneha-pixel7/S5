import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.naive_bayes import BernoulliNB, MultinomialNB

categories = ['sci.med', 'sci.space', 'comp.graphics', 'talk.politics.misc']
train_data = fetch_20newsgroups(
    subset='train', categories=categories, remove=('headers', 'footers', 'quotes')
)
test_data = fetch_20newsgroups(
    subset='test', categories=categories, remove=('headers', 'footers', 'quotes')
)
X_train, y_train = train_data.data, train_data.target
X_test, y_test = test_data.data, test_data.target

vectorizer_multinomial = CountVectorizer(stop_words='english', min_df=2)
X_train_counts = vectorizer_multinomial.fit_transform(X_train)
X_test_counts = vectorizer_multinomial.transform(X_test)

vectorizer_bernoulli = CountVectorizer(
    stop_words='english', binary=True, min_df=2
)
X_train_binary = vectorizer_bernoulli.fit_transform(X_train)
X_test_binary = vectorizer_bernoulli.transform(X_test)

clf_multinomial = MultinomialNB(alpha=1.0).fit(X_train_counts, y_train)
y_pred_multi = clf_multinomial.predict(X_test_counts)
print('--- Multinomial Naïve Bayes Complete ---')
print(f'Accuracy: {accuracy_score(y_test, y_pred_multi):.4f}')

clf_bernoulli = BernoulliNB(alpha=1.0).fit(X_train_binary, y_train)
y_pred_bern = clf_bernoulli.predict(X_test_binary)
print('--- Bernoulli Naïve Bayes Complete ---')
print(f'Accuracy: {accuracy_score(y_test, y_pred_bern):.4f}')

metrics_summary = {
    'Model Framework': [
        'Multinomial Naïve Bayes (Frequency)',
        'Bernoulli Naïve Bayes (Binary)',
    ],
    'Test Accuracy': [
        accuracy_score(y_test, y_pred_multi),
        accuracy_score(y_test, y_pred_bern),
    ],
    'Macro F1-Score': [
        f1_score(y_test, y_pred_multi, average='macro'),
        f1_score(y_test, y_pred_bern, average='macro'),
    ],
}
df_res = pd.DataFrame(metrics_summary)
print('\nPerformance Comparisons:\n', df_res.to_string(index=False))

df_res.set_index('Model Framework').plot(kind='bar', figsize=(8, 5))
plt.ylabel('Score Metric Scale')
plt.title('Naïve Bayes Variant Analysis on Text Corpora')
plt.xticks(rotation=0)
plt.ylim(0.5, 1.0)
plt.tight_layout()
plt.show()