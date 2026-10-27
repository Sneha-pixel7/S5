# Experiment 11: Linear SVM Decision Boundary & Margins

## What is this experiment all about?
When two groups of dots can be separated by a straight line, there are actually infinitely many lines you could draw. Which one is best?

A **Support Vector Machine (SVM)** doesn't just draw any separating line—it finds the line with the **widest possible street** (maximum margin) between the two classes.

The data points that sit right on the edge of this street are called **Support Vectors**. They are the hardest, most borderline cases. Amazingly, the entire decision boundary is anchored solely by these few support vectors—if you deleted all the easy data points far away, the decision line wouldn't change at all!

## What is the code actually doing?
1. **Loads flower measurements**: Uses Fisher's famous Iris dataset and extracts two visual features: Petal Length and Petal Width.
2. **Frames binary task**: Separates *Iris Setosa* flowers from all other iris species.
3. **Trains a Linear SVM**: Fits an `SVC(kernel='linear', C=1.0)` model after standardizing features.
4. **Calculates accuracy**: Checks precision, recall, and confusion matrix on held-out test flowers (achieving 100% clean separation).
5. **Draws the visual geometry**:
   - Plots the flower points in their original centimeter scale.
   - Draws a solid center line: the optimal separating boundary ($w^T x + b = 0$).
   - Draws dashed outer lines: the margin edges ($w^T x + b = \pm 1$).
   - Circles the exact **Support Vectors** so you can see which specific flowers determine the boundary.

## How to run
```bash
python exp11.py
```
