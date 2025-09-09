# This repository contains Python practice scripts and examples for learning and experimenting with **SciPy**, NumPy, and related scientific computing tools.  
np.random.multivariate_normal(mean, cov, size)

Purpose: Generate samples from a multivariate normal (Gaussian) distribution.
Arguments:
    mean: The mean vector of the distribution.
    cov: The covariance matrix.
    size: Number of samples to generate.

1. Mean vector → [0, 2]
    This means:
    The first variable has mean 0
    The second variable has mean 2
    So the center of the distribution is around (0, 2).

2. Covariance matrix → [[2, 1], [1, 1.5]]
    This is a 2×2 symmetric matrix:
    Σ=[2,1
        1,1.5]
    Diagonal elements: variances of each variable
        Var(X₁) = 2
        Var(X₂) = 1.5
    Off-diagonal elements: covariance
        Cov(X₁, X₂) = 1
    → This means the two variables are positively correlated.
    ->covariance matrices must satisfy
        cov(x,y)=cov(y,x)
    -> it must satisfy:
        a≥0,d≥0 (variances must be non-negative)
        ad-b^2≥0 or b^2ad (determinant must be ≥ 0 → ensures positive semi-definite)
3. Size → 200
    Generate 200 samples from this 2D Gaussian distribution.
    a will be a (200, 2) NumPy array (200 rows, 2 columns).
