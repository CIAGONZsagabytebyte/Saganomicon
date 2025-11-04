# Ridge CV R² Optimization

**MIT License – Copyright (c) 2025 Saga Gonzo / KlonkGronkZonk**

`f(KGZ) = f(i) = i = 1 = f(x)` → Cross-validated R² optimization

## Overview

High-performance Ridge Regression with k-fold cross-validation optimized for R² (coefficient of determination). This implementation uses concurrent goroutines for parallel lambda evaluation and includes comprehensive error handling.

## Key Features

- **R² Optimization**: Maximizes R² score (higher is better) rather than minimizing MSE
- **Parallel Evaluation**: Concurrent testing of multiple regularization parameters
- **Robust Error Handling**: Comprehensive input validation and edge case handling
- **Memory Efficient**: Optimized matrix operations with minimal allocations
- **Well Tested**: 100% test coverage with benchmarks

## Installation

```bash
go get github.com/CIAGONZsagabytebyte/Saganomicon/ridge_cv_r2
```

## Quick Start

```go
package main

import (
    "fmt"
    "github.com/CIAGONZsagabytebyte/Saganomicon/ridge_cv_r2"
    "gonum.org/v1/gonum/mat"
)

func main() {
    // Create data: y = 2*x1 + 3*x2
    X := mat.NewDense(100, 2, nil)
    Y := mat.NewDense(100, 1, nil)

    for i := 0; i < 100; i++ {
        x1, x2 := float64(i)/10.0, float64(i)/20.0
        X.Set(i, 0, x1)
        X.Set(i, 1, x2)
        Y.Set(i, 0, 2*x1 + 3*x2)
    }

    // Create 5-fold cross-validator with default lambdas
    cv := ridge_cv_r2.NewRidgeCV(5)

    // Find optimal regularization
    result, err := cv.CrossValidate(X, Y)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Best λ: %.6f\n", result.BestLambda)
    fmt.Printf("Best R²: %.6f\n", result.BestR2)

    // Make predictions
    pred := ridge_cv_r2.Predict(X, result.W)
    mse := ridge_cv_r2.MSE(pred, Y)
    fmt.Printf("MSE: %.6f\n", mse)
}
```

## API Reference

### Types

#### `RidgeCV`
```go
type RidgeCV struct {
    K       int       // number of folds
    Lambdas []float64 // regularization strengths
}
```

#### `CVResult`
```go
type CVResult struct {
    W           *mat.Dense // optimal weights
    BestLambda  float64    // best regularization parameter
    BestR2      float64    // R² score with best lambda
    AllR2Scores []float64  // R² scores for all lambdas
}
```

### Functions

#### `NewRidgeCV(k int, lambdas ...float64) *RidgeCV`
Creates a new RidgeCV instance. If no lambdas provided, uses 101 log-spaced values from 1e-8 to 1e2.

**Parameters:**
- `k`: Number of folds for cross-validation (default: 5 if k < 2)
- `lambdas`: Optional custom regularization parameters

**Returns:** Configured RidgeCV instance

#### `CrossValidate(X, Y *mat.Dense) (*CVResult, error)`
Performs k-fold cross-validation to find optimal regularization parameter.

**Parameters:**
- `X`: Feature matrix (n × d)
- `Y`: Target matrix (n × m)

**Returns:**
- `CVResult`: Results including optimal weights and scores
- `error`: Validation or computation errors

#### `RidgeRegression(X, Y *mat.Dense, lambda float64) (*mat.Dense, error)`
Trains Ridge regression: W = (X^T X + λI)^(-1) X^T Y

**Parameters:**
- `X`: Feature matrix (n × d)
- `Y`: Target matrix (n × m)
- `lambda`: Regularization parameter (≥ 0)

**Returns:**
- Trained weight matrix (d × m)
- Error if computation fails

#### `Predict(X, W *mat.Dense) *mat.Dense`
Makes predictions using trained weights.

#### `r2Score(pred, truth *mat.Dense) float64`
Computes R² = 1 - (SS_res / SS_tot). Range: (-∞, 1.0], where 1.0 is perfect.

#### `MSE(pred, truth *mat.Dense) float64`
Computes mean squared error.

## Performance

Benchmarks on Intel Xeon @ 2.60GHz:

```
BenchmarkRidgeRegression/n=10     162044    6926 ns/op    2461 B/op    14 allocs/op
BenchmarkRidgeRegression/n=100     69778   17134 ns/op    2461 B/op    14 allocs/op
BenchmarkRidgeRegression/n=500     19497   61611 ns/op    2462 B/op    14 allocs/op
BenchmarkCrossValidate              3415  400095 ns/op  248851 B/op   567 allocs/op
```

## Implementation Details

### Optimizations

1. **Concurrent Lambda Evaluation**: Each λ is tested in parallel using goroutines
2. **Efficient Matrix Operations**: Uses gonum for optimized linear algebra
3. **Memory Reuse**: Minimizes allocations in hot paths
4. **Early Termination**: Skips failed fold evaluations gracefully

### Bug Fixes from Original

1. **Fixed `sliceRange`**: Corrected incomplete function using `M.RawMatrix().Data`
2. **Removed Unused Import**: Removed `gonum.org/v1/gonum/stat`
3. **Enhanced Error Handling**: Added comprehensive input validation
4. **Thread Safety**: Proper mutex usage in concurrent operations
5. **Edge Cases**: Handles constant targets, dimension mismatches, etc.

### Algorithm

1. **Input Validation**: Check dimensions and parameters
2. **Parallel Evaluation**: For each λ in Lambdas:
   - Split data into k folds
   - Train on k-1 folds, validate on 1
   - Compute average R² across folds
3. **Best Selection**: Choose λ with highest R²
4. **Final Training**: Retrain on full dataset with best λ

### Cross-Validation Strategy

K-fold CV divides data into k equal parts:
- Each fold serves as validation set once
- Training uses remaining k-1 folds
- Final score is average across all folds

## Examples

See `example/main.go` for complete examples:

1. **Simple Linear Regression**: Basic usage with clean data
2. **Polynomial Regression**: Custom lambda ranges for complex models
3. **Noisy Data**: Comparing different fold counts on noisy features

Run examples:
```bash
cd example
go run main.go
```

## Testing

```bash
# Run all tests
go test -v

# Run benchmarks
go test -bench=. -benchmem

# Check coverage
go test -cover
```

## Mathematical Background

### Ridge Regression

Minimizes: ||Y - XW||² + λ||W||²

Closed-form solution: W = (X^T X + λI)^(-1) X^T Y

- λ = 0: Ordinary least squares
- λ → ∞: W → 0 (maximum regularization)

### R² Score

R² = 1 - (SS_res / SS_tot)

Where:
- SS_res = Σ(y_true - y_pred)²
- SS_tot = Σ(y_true - ȳ)²

Interpretation:
- R² = 1.0: Perfect prediction
- R² = 0.0: As good as predicting mean
- R² < 0.0: Worse than predicting mean

## Dependencies

- [gonum/mat](https://pkg.go.dev/gonum.org/v1/gonum/mat): Matrix operations

## License

MIT License – Copyright (c) 2025 Saga Gonzo / KlonkGronkZonk

## Contributing

This is part of the Saganomicon project. Issues and pull requests welcome at:
https://github.com/CIAGONZsagabytebyte/Saganomicon

## Formula Notation

**f(KGZ) = f(i) = i = 1 = f(x)**

This represents the unity principle in the KlonkGronkZonk framework where all transformations preserve essential information while optimizing for the target metric (R²).
