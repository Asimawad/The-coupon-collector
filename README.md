

# The Coupon Collector’s Problem

Each box of a certain breakfast cereal contains one of ten different coupons, each with the same probability. We win a prize if we manage to obtain a complete collection of all the different coupons. How long, on average, do we have to wait? 

For example, suppose we draw the following coupons, in order:
`5, 2, 3, 7, 5, 1, 1, 4, 8, 4, 1, 9, 10, 2, 3, 3, 6`.

With the last coupon (6), we have completed our collection, and so we stop (after altogether 17 steps). What if we had more coupons? Can we deduce an asymptotic formula for a large number of coupons? What about the case where some boxes do not have coupons, or one coupon is more/less probable to choose?

This repository contains a detailed exploration of the Coupon Collector’s Problem, including theoretical derivations, empirical simulations, and data analysis. The problem investigates the expected number of trials required to collect all `n` unique coupons, given certain probabilities.

---

## Problem Statement

The Coupon Collector's Problem asks:  
*Given `n` unique coupon types, how many trials are required, on average, to collect all coupons at least once?*

- **Equal Probability Case**: Each coupon is equally likely to appear in a random draw (probability = `1/n`).
- **Non-Uniform Probability Case**: Different coupons have varying probabilities of appearing.

---

## Theoretical Solution

The expected number of trials to collect all `n` unique coupons is:

```
T(n) = n * [1 + 1/2 + 1/3 + ... + 1/n]
```

Here, the sum `[1 + 1/2 + 1/3 + ... + 1/n]` is known as the harmonic number, denoted as `H(n)`. For large `n`, the harmonic number can be approximated as:

```
H(n) ≈ ln(n) + γ
```

where `ln(n)` is the natural logarithm and `γ` (gamma) is the Euler-Mascheroni constant (approximately 0.5772).

Thus, for large `n`, the expected number of trials grows approximately as:

```
T(n) ≈ n * (ln(n) + γ)
```

---

## Empirical Validation

An empirical simulation was conducted to validate the theoretical formula. The process involves:
1. Simulating random draws of coupons until all `n` unique coupons are collected.
2. Repeating the simulation for multiple trials (e.g., 1000 trials) and averaging the results.

---

### Results and Comparison

Empirical results closely align with the theoretical predictions. For example:

- **For `n = 50`:**
  - Empirical result: `T(50) ≈ 224.96`
  - Theoretical result: `T(50) ≈ 225.55`

---

### Fitted Function

A quadratic function was fitted to the empirical results to provide an approximation for finite `n`:

```
f(n) = 0.0252 * n^2 + 3.3731 * n - 5.3161
```

This fitted function serves as a practical approximation for the expected number of trials and aligns closely with the harmonic summation formula.

---

## Key Features of the Repository

1. **Empirical Simulation**: Python implementation of the Coupon Collector’s Problem simulation.
2. **Theoretical Validation**: Comparison of empirical and theoretical results.
3. **Quadratic Approximation**: A fitted quadratic function that provides an approximate solution for finite `n`.
4. **Generalization**:
   - Non-uniform probabilities for coupons.
   - Handling cases where some boxes are empty.

---

## How to Use

### Running the Simulation

Use the Python script provided to calculate the expected number of trials empirically or theoretically. The script allows you to:
1. Simulate the process for varying values of `n`.
2. Compare empirical results with the theoretical formula.
3. Generate plots of the results and fitted curves.

---

### Fitted Function

For practical purposes, the fitted quadratic function provides a close approximation for `n` in a finite range:

```
f(n) = 0.0252 * n^2 + 3.3731 * n - 5.3161
```

---

## Repository Contents

- `main.py`: Python script for running the empirical simulation and theoretical validation.
- `compare.pdf`: Plot comparing empirical and theoretical results.
- `curve.pdf`: Plot of the fitted quadratic function.
- `README.md`: Overview of the project.

---

## References

For a full explanation of the derivations, proofs, and additional cases (e.g., non-uniform probabilities and empty boxes), see the full report: [Full Report on Google Drive](https://drive.google.com/file/d/1Gh_7apzwcPUDyXaR4zbmYkuW-AHXRiil/view?usp=sharing)

---

## Author

[Asim Awad Hussein Osman](https://github.com/Asimawad)

---
