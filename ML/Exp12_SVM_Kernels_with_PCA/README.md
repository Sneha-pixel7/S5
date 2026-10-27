# Experiment 12: SVM Kernels with PCA on Fashion-MNIST

## What is this experiment all about?
Most real-world data cannot be separated by a simple flat sheet of paper (a linear plane). Clothing images (shirts vs. dresses vs. coats) have complex textures, folds, and shapes.

Support Vector Machines solve this using the **Kernel Trick**:
Imagine your points are mixed up on a 2D floor. The kernel trick lifts points into a 3D space where a flat sheet can now slide right between them, separating them cleanly!
- **Linear Kernel**: Assumes a simple flat boundary.
- **Polynomial Kernel**: Creates curved, bending boundaries by considering interactions between features.
- **RBF (Radial Basis Function) Kernel**: The most popular and flexible kernel. It wraps soft "bubbles" around clusters of data in an infinite-dimensional mathematical space.

Also, image data has 784 pixels per photo, which makes kernel math computationally heavy. We use **PCA (Principal Component Analysis)** to compress 784 pixels down into the **50 most informative components**, preserving image details while speeding up training dramatically!

## What is the code actually doing?
1. **Loads clothing photos**: Takes 6,000 stratified sample images from the Fashion-MNIST dataset.
2. **Compresses images with PCA**: Reduces dimensions from 784 pixels down to 50 principal components while retaining the core visual variance.
3. **Trains 3 different SVM kernels**:
   - Linear SVM
   - Polynomial SVM (degree 3)
   - RBF SVM (Gaussian)
4. **Measures time & accuracy**: Records how long each kernel took to train and how accurately it classified unseen clothing items.
5. **Draws comparisons**:
   - Plots a bar chart of accuracy across all three kernels (showing RBF outperforming the others).
   - Plots a confusion matrix heatmap for the best kernel (RBF) so you can see which clothing items it occasionally confuses (e.g., shirts vs. T-shirts).

## How to run
```bash
python exp12.py
```
