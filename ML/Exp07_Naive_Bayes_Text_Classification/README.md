# Experiment 07: Text Classification with Naïve Bayes

## What is this experiment all about?
How does an email client know whether an incoming message is spam or which folder to sort it into? Most text classifiers start with **Naïve Bayes**, a fast, probability-based algorithm that calculates:
*"Given the words in this document, which topic has the highest probability?"*

It is called "Naïve" because it simplifies the math by assuming every word occurs independently of all others (ignoring grammar or sentence structure). Despite this assumption, it works remarkably well in practice.

When converting words into numbers, there are two common approaches:
1. **Multinomial Naïve Bayes**: Counts **how many times** each word appears (frequency). E.g., if "patient" appears 7 times, that strongly signals medicine.
2. **Bernoulli Naïve Bayes**: Only checks **whether** a word appears (binary: yes/no). It doesn't care if a word appeared once or 10 times.

## What is the code actually doing?
1. **Downloads newsgroup posts**: Loads hundreds of discussion forum posts across 4 topics: Medicine (`sci.med`), Space (`sci.space`), Computer Graphics (`comp.graphics`), and Politics (`talk.politics.misc`).
2. **Cleans the text**: Strips out email headers, footers, and signatures so the model only learns from the actual message body.
3. **Converts text into tables of numbers**:
   - Creates a frequency count matrix for Multinomial NB.
   - Creates a 0/1 presence matrix for Bernoulli NB.
4. **Trains both classifiers**: Trains `MultinomialNB` and `BernoulliNB` with Laplace smoothing ($\alpha=1.0$) so unseen words don't cause zero-probability math errors.
5. **Compares accuracy**: Tests both models on unseen documents and compares their classification accuracy and Macro F1-scores.
6. **Plots performance**: Draws a bar chart showing why counting word repetition (Multinomial) usually outperforms simple presence checking (Bernoulli) on full-length articles.

## How to run
```bash
python exp7.py
```
