# Experiment 08: K-Nearest Neighbors on Fashion-MNIST

## What is this experiment all about?
**K-Nearest Neighbors (KNN)** is often called the "lazy learner" because it does almost no training work beforehand. Instead, it memorizes all the training images.

When you hand it an unseen picture (e.g., a mystery clothing item) and ask *"What is this?"*:
1. It calculates the mathematical distance (pixel difference) between this new image and every single image in its database.
2. It picks the **$K$ closest neighbors**.
3. It takes a **majority vote**. If 4 out of 5 neighbors are shoes, it predicts "Shoe!"

This experiment explores the choice of $K$:
- If $K=1$, a single weird, distorted training image can trick the model.
- If $K$ is too high, it considers too many distant neighbors and blurs category lines.
- Because it has to compute distances to every training example at test time, KNN can take noticeable time to predict (high inference latency).

## What is the code actually doing?
1. **Loads clothing images**: Takes Fashion-MNIST (10 categories: T-shirts, trousers, pullovers, dresses, coats, sandals, shirts, sneakers, bags, ankle boots).
2. **Prepares the images**: Subsamples 5,000 training and 500 testing images to keep running time reasonable, flattens each $28 \times 28$ image into 784 numbers, and scales pixel brightness to between 0 and 1.
3. **Tests different $K$ values**: Runs KNN for $K = 1, 3, 5, 11$.
4. **Measures time & accuracy**: For each $K$, records test accuracy, F1-score, and precisely measures how many seconds the computer takes to search neighbors and make predictions.
5. **Plots the Trade-Off**: Displays a dual-axis chart:
   - Blue line: Accuracy across different values of $K$.
   - Red dashed line: How many seconds each prediction batch took.

## How to run
```bash
python exp8.py
```
