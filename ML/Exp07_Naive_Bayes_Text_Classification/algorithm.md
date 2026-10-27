# Algorithm: Text Classification using Naïve Bayes (Multinomial vs Bernoulli)

1. **Load Corpus**:
   - Fetch 20 Newsgroups text data for 4 categories (`sci.med`, `sci.space`, `comp.graphics`, `talk.politics.misc`).
   - Strip headers, footers, and quotes to prevent metadata leakage.

2. **Feature Extraction (Tokenization & Vectorization)**:
   - **Frequency Matrix (Multinomial)**: Fit `CountVectorizer(stop_words='english', min_df=2, binary=False)` to extract word counts.
   - **Binary Matrix (Bernoulli)**: Fit `CountVectorizer(stop_words='english', min_df=2, binary=True)` to extract word presence/absence (0 or 1).

3. **Train Classifiers**:
   - Fit `MultinomialNB(alpha=1.0)` with Laplace smoothing on the word-frequency matrix.
   - Fit `BernoulliNB(alpha=1.0)` with Laplace smoothing on the binary indicator matrix.

4. **Evaluate Performance**:
   - Predict categories on held-out test documents for both models.
   - Compute Test Accuracy and Macro-averaged F1-Score.

5. **Visualize & Compare**:
   - Display a performance comparison table.
   - Plot a grouped bar chart comparing Accuracy and Macro F1 between Multinomial (frequency-based) and Bernoulli (presence-based) variants.
