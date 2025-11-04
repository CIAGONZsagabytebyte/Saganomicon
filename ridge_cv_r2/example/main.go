// example/main.go
// MIT License – Copyright (c) 2025 Saga Gonzo / KlonkGronkZonk
// Example usage of Ridge CV R² optimization

package main

import (
	"fmt"
	"math"
	"math/rand"

	"github.com/CIAGONZsagabytebyte/Saganomicon/ridge_cv_r2"
	"gonum.org/v1/gonum/mat"
)

func main() {
	fmt.Println("=== Ridge CV R² Optimization Example ===")
	fmt.Println()

	// Example 1: Simple linear regression
	fmt.Println("Example 1: Simple Linear Regression")
	simpleLinearExample()
	fmt.Println()

	// Example 2: Polynomial features
	fmt.Println("Example 2: Polynomial Regression")
	polynomialExample()
	fmt.Println()

	// Example 3: Noisy data
	fmt.Println("Example 3: Noisy Data with Regularization")
	noisyDataExample()
	fmt.Println()
}

func simpleLinearExample() {
	// Generate data: y = 2*x1 + 3*x2 + 1
	n := 100
	X := mat.NewDense(n, 2, nil)
	Y := mat.NewDense(n, 1, nil)

	for i := 0; i < n; i++ {
		x1 := float64(i) / 10.0
		x2 := float64(i) / 20.0
		X.Set(i, 0, x1)
		X.Set(i, 1, x2)
		y := 2*x1 + 3*x2 + 1
		Y.Set(i, 0, y)
	}

	// Create RidgeCV with 5-fold cross-validation
	cv := ridge_cv_r2.NewRidgeCV(5)

	// Find optimal regularization
	result, err := cv.CrossValidate(X, Y)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Printf("  Best λ: %.6f\n", result.BestLambda)
	fmt.Printf("  Best R²: %.6f\n", result.BestR2)
	fmt.Printf("  Weights: [%.4f, %.4f]\n",
		result.W.At(0, 0), result.W.At(1, 0))

	// Make predictions
	pred := ridge_cv_r2.Predict(X, result.W)
	mse := ridge_cv_r2.MSE(pred, Y)
	fmt.Printf("  MSE: %.6f\n", mse)
}

func polynomialExample() {
	// Generate polynomial data: y = x + x² - 0.1*x³
	n := 50
	X := mat.NewDense(n, 3, nil) // [x, x², x³]
	Y := mat.NewDense(n, 1, nil)

	for i := 0; i < n; i++ {
		x := float64(i)/10.0 - 2.5 // range [-2.5, 2.5]
		X.Set(i, 0, x)
		X.Set(i, 1, x*x)
		X.Set(i, 2, x*x*x)
		y := x + x*x - 0.1*x*x*x
		Y.Set(i, 0, y)
	}

	// Use custom lambda range for polynomial regression
	lambdas := []float64{0.001, 0.01, 0.1, 1.0, 10.0, 100.0}
	cv := ridge_cv_r2.NewRidgeCV(5, lambdas...)

	result, err := cv.CrossValidate(X, Y)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Printf("  Best λ: %.6f\n", result.BestLambda)
	fmt.Printf("  Best R²: %.6f\n", result.BestR2)
	fmt.Printf("  Coefficients: [%.4f, %.4f, %.4f]\n",
		result.W.At(0, 0), result.W.At(1, 0), result.W.At(2, 0))

	// Show R² scores for all lambdas
	fmt.Println("  R² scores for all λ values:")
	for i, lam := range lambdas {
		fmt.Printf("    λ=%.3f: R²=%.6f\n", lam, result.AllR2Scores[i])
	}
}

func noisyDataExample() {
	// Generate noisy linear data
	rand.Seed(42)
	n := 80
	nFeatures := 5
	X := mat.NewDense(n, nFeatures, nil)
	Y := mat.NewDense(n, 1, nil)

	// True weights: [1, 2, 3, 0, 0] (last two features are noise)
	trueWeights := []float64{1, 2, 3, 0, 0}

	for i := 0; i < n; i++ {
		var y float64
		for j := 0; j < nFeatures; j++ {
			x := rand.NormFloat64()
			X.Set(i, j, x)
			y += trueWeights[j] * x
		}
		// Add noise
		y += rand.NormFloat64() * 0.5
		Y.Set(i, 0, y)
	}

	// Test different fold counts
	folds := []int{3, 5, 10}
	lambdas := []float64{0.01, 0.1, 1.0, 10.0, 100.0}

	for _, k := range folds {
		cv := ridge_cv_r2.NewRidgeCV(k, lambdas...)
		result, err := cv.CrossValidate(X, Y)
		if err != nil {
			fmt.Printf("  Error with %d-fold CV: %v\n", k, err)
			continue
		}

		fmt.Printf("  %d-fold CV:\n", k)
		fmt.Printf("    Best λ: %.6f\n", result.BestLambda)
		fmt.Printf("    Best R²: %.6f\n", result.BestR2)
		fmt.Printf("    Learned weights: [")
		for j := 0; j < nFeatures; j++ {
			fmt.Printf("%.3f", result.W.At(j, 0))
			if j < nFeatures-1 {
				fmt.Printf(", ")
			}
		}
		fmt.Println("]")
		fmt.Printf("    True weights:    [")
		for j := 0; j < nFeatures; j++ {
			fmt.Printf("%.3f", trueWeights[j])
			if j < nFeatures-1 {
				fmt.Printf(", ")
			}
		}
		fmt.Println("]")

		// Calculate weight error
		var weightError float64
		for j := 0; j < nFeatures; j++ {
			diff := result.W.At(j, 0) - trueWeights[j]
			weightError += diff * diff
		}
		weightError = math.Sqrt(weightError)
		fmt.Printf("    Weight RMSE: %.4f\n", weightError)
		fmt.Println()
	}
}
