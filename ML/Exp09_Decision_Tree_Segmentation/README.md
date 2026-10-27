# Experiment 09: Customer Segmentation with Decision Trees

## What is this experiment all about?
Imagine you are running an e-commerce platform and want to categorize shoppers into **Bronze**, **Silver**, and **Gold** loyalty tiers so you can target them with special deals.

You track three key metrics known in marketing as **RFM**:
- **Recency**: When was their last purchase? (Recent, Dormant, or At-Risk)
- **Frequency**: How often do they order? (Low, Medium, or High)
- **Monetary**: How much total money do they spend? (Low, Medium, or High)

A **Decision Tree** acts like an automated, intelligent flowchart. It asks a sequence of yes/no questions (e.g., *"Is their spending High?"*, *"Is their last purchase Recent?"*) to sort customers into the right bucket.

It decides which question to ask first using **Entropy** (a mathematical score for disorder or uncertainty). It chooses the split that creates the cleanest, most pure groups (maximum **Information Gain**).

## What is the code actually doing?
1. **Creates a customer dataset**: Synthesizes 800 customer profiles with realistic RFM shopping behaviors and loyalty tiers.
2. **Converts categories to numbers**: Encodes text categories into numeric values and maps Bronze/Silver/Gold to 0, 1, and 2.
3. **Trains the Decision Tree**: Builds a tree using `criterion='entropy'` with `max_depth=3` (pruned to 3 levels deep so the rules remain simple and human-readable).
4. **Calculates accuracy**: Tests the tree on unseen customer profiles to see how reliably it predicts loyalty tiers.
5. **Draws the flowchart & importance**:
   - Plots the actual tree diagram with colored boxes showing each split question, sample count, and class distribution.
   - Plots a feature importance chart showing whether Recency, Frequency, or Spending mattered most in determining customer tier.

## How to run
```bash
python exp9.py
```
