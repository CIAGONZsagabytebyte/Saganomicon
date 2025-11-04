// ridge_cv_r2.go
// MIT License – Copyright (c) 2025 Saga Gonzo / KlonkGronkZonk
// f(KGZ) = f(i) = i = 1 = f(x) → Cross-validated R² optimization
// Optimized version with bug fixes and performance improvements

package ridge_cv_r2

import (
	"fmt"
	"math"
	"sync"

	"gonum.org/v1/gonum/mat"
)

// RidgeCV optimizes Ridge regression for R² (higher = better)
type RidgeCV struct {
	K       int       // number of folds for cross-validation
	Lambdas []float64 // regularization strengths to test
}

// NewRidgeCV creates a new RidgeCV with default log-space lambdas if none provided
func NewRidgeCV(k int, lambdas ...float64) *RidgeCV {
	if k < 2 {
		k = 5 // default to 5-fold CV
	}

	if len(lambdas) == 0 {
		// Create 101 log-spaced lambdas from 1e-8 to 1e2
		lambdas = make([]float64, 0, 101)
		for i := -8.0; i <= 2.0; i += 0.1 {
			lambdas = append(lambdas, math.Pow(10, i))
		}
	}

	return &RidgeCV{K: k, Lambdas: lambdas}
}

// CVResult contains cross-validation results
type CVResult struct {
	W           *mat.Dense // optimal weights
	BestLambda  float64    // best regularization parameter
	BestR2      float64    // R² score with best lambda
	AllR2Scores []float64  // R² scores for all lambdas
}

// CrossValidate returns optimal weights, lambda, and R² score
func (cv *RidgeCV) CrossValidate(X, Y *mat.Dense) (*CVResult, error) {
	// Input validation
	if X == nil || Y == nil {
		return nil, fmt.Errorf("X and Y cannot be nil")
	}

	n, d := X.Dims()
	yn, _ := Y.Dims()

	if n != yn {
		return nil, fmt.Errorf("X and Y must have same number of rows: %d != %d", n, yn)
	}

	if n < cv.K {
		return nil, fmt.Errorf("not enough samples (%d) for %d-fold CV", n, cv.K)
	}

	if d == 0 {
		return nil, fmt.Errorf("X must have at least one feature")
	}

	if len(cv.Lambdas) == 0 {
		return nil, fmt.Errorf("must provide at least one lambda value")
	}

	type result struct {
		lambda float64
		r2     float64
		err    error
	}

	bestR2 := math.Inf(-1)
	var bestLambda float64
	allR2Scores := make([]float64, len(cv.Lambdas))

	var wg sync.WaitGroup
	results := make(chan result, len(cv.Lambdas))

	// Evaluate each lambda in parallel
	for i, lambda := range cv.Lambdas {
		wg.Add(1)
		go func(idx int, lam float64) {
			defer wg.Done()
			r2, err := cv.evaluateLambdaR2(X, Y, lam)
			results <- result{lambda: lam, r2: r2, err: err}
		}(i, lambda)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	// Collect results
	validResults := 0
	for res := range results {
		if res.err != nil {
			continue // skip failed evaluations
		}

		// Find index of this lambda
		for i, lam := range cv.Lambdas {
			if lam == res.lambda {
				allR2Scores[i] = res.r2
				break
			}
		}

		if res.r2 > bestR2 {
			bestR2 = res.r2
			bestLambda = res.lambda
		}
		validResults++
	}

	if validResults == 0 {
		return nil, fmt.Errorf("all lambda evaluations failed")
	}

	// Retrain on full data with best lambda
	W, err := RidgeRegression(X, Y, bestLambda)
	if err != nil {
		return nil, fmt.Errorf("final training failed: %w", err)
	}

	return &CVResult{
		W:           W,
		BestLambda:  bestLambda,
		BestR2:      bestR2,
		AllR2Scores: allR2Scores,
	}, nil
}

// evaluateLambdaR2 computes average R² over k folds for a given lambda
func (cv *RidgeCV) evaluateLambdaR2(X, Y *mat.Dense, lambda float64) (float64, error) {
	n, _ := X.Dims()
	foldSize := n / cv.K

	r2Scores := make([]float64, cv.K)
	var wg sync.WaitGroup
	errChan := make(chan error, cv.K)

	for k := 0; k < cv.K; k++ {
		wg.Add(1)
		go func(fold int) {
			defer wg.Done()

			start := fold * foldSize
			end := start + foldSize
			if fold == cv.K-1 {
				end = n // include remaining samples in last fold
			}

			// Split data
			Xtrain := sliceExclude(X, start, end)
			Ytrain := sliceExclude(Y, start, end)
			Xtest := sliceRange(X, start, end)
			Ytest := sliceRange(Y, start, end)

			// Train model on fold
			W, err := RidgeRegression(Xtrain, Ytrain, lambda)
			if err != nil {
				errChan <- fmt.Errorf("fold %d training failed: %w", fold, err)
				return
			}

			// Predict and score
			var pred mat.Dense
			pred.Mul(Xtest, W)
			r2 := r2Score(&pred, Ytest)

			r2Scores[fold] = r2
		}(k)
	}

	wg.Wait()
	close(errChan)

	// Check for errors
	if len(errChan) > 0 {
		return math.Inf(-1), <-errChan
	}

	// Compute mean R²
	var totalR2 float64
	for _, r2 := range r2Scores {
		totalR2 += r2
	}

	return totalR2 / float64(cv.K), nil
}

// r2Score computes R² = 1 - (SS_res / SS_tot)
// Higher is better, 1.0 is perfect, negative values indicate poor fit
func r2Score(pred, truth *mat.Dense) float64 {
	rp, cp := pred.Dims()
	rt, ct := truth.Dims()

	if rp != rt || cp != ct {
		return math.Inf(-1)
	}

	if rp == 0 || cp == 0 {
		return math.Inf(-1)
	}

	// Compute mean of true values
	var ySum float64
	count := 0
	for i := 0; i < rt; i++ {
		for j := 0; j < ct; j++ {
			ySum += truth.At(i, j)
			count++
		}
	}
	yMean := ySum / float64(count)

	// Total sum of squares (SS_tot)
	var ssTot float64
	for i := 0; i < rt; i++ {
		for j := 0; j < ct; j++ {
			diff := truth.At(i, j) - yMean
			ssTot += diff * diff
		}
	}

	if ssTot == 0 {
		// All y values are the same
		// Check if predictions match
		var ssRes float64
		for i := 0; i < rp; i++ {
			for j := 0; j < cp; j++ {
				diff := pred.At(i, j) - truth.At(i, j)
				ssRes += diff * diff
			}
		}
		if ssRes == 0 {
			return 1.0 // perfect prediction
		}
		return 0.0 // constant prediction for constant target
	}

	// Residual sum of squares (SS_res)
	var ssRes float64
	for i := 0; i < rp; i++ {
		for j := 0; j < cp; j++ {
			diff := pred.At(i, j) - truth.At(i, j)
			ssRes += diff * diff
		}
	}

	return 1.0 - (ssRes / ssTot)
}

// RidgeRegression solves the Ridge regression problem:
// W = (X^T X + λI)^(-1) X^T Y
func RidgeRegression(X, Y *mat.Dense, lambda float64) (*mat.Dense, error) {
	if X == nil || Y == nil {
		return nil, fmt.Errorf("X and Y cannot be nil")
	}

	n, d := X.Dims()
	yn, _ := Y.Dims()

	if n != yn {
		return nil, fmt.Errorf("X and Y must have same number of rows")
	}

	if n == 0 || d == 0 {
		return nil, fmt.Errorf("X must have non-zero dimensions")
	}

	if lambda < 0 {
		return nil, fmt.Errorf("lambda must be non-negative")
	}

	// Compute X^T X
	XT := X.T()
	var XTX mat.Dense
	XTX.Mul(XT, X)

	// Add regularization: X^T X + λI
	for i := 0; i < d; i++ {
		val := XTX.At(i, i)
		XTX.Set(i, i, val+lambda)
	}

	// Compute X^T Y
	var XTY mat.Dense
	XTY.Mul(XT, Y)

	// Solve (X^T X + λI) W = X^T Y
	var W mat.Dense
	if err := W.Solve(&XTX, &XTY); err != nil {
		return nil, fmt.Errorf("matrix solve failed: %w", err)
	}

	return &W, nil
}

// sliceExclude returns a copy of M excluding rows [start, end)
func sliceExclude(M *mat.Dense, start, end int) *mat.Dense {
	rows, cols := M.Dims()

	if start < 0 || end > rows || start >= end {
		panic(fmt.Sprintf("invalid range [%d, %d) for matrix with %d rows", start, end, rows))
	}

	newRows := rows - (end - start)
	if newRows == 0 {
		return mat.NewDense(0, cols, nil)
	}

	data := make([]float64, newRows*cols)
	idx := 0

	raw := M.RawMatrix()
	for i := 0; i < rows; i++ {
		if i < start || i >= end {
			offset := i * cols
			copy(data[idx:idx+cols], raw.Data[offset:offset+cols])
			idx += cols
		}
	}

	return mat.NewDense(newRows, cols, data)
}

// sliceRange returns a copy of M containing only rows [start, end)
func sliceRange(M *mat.Dense, start, end int) *mat.Dense {
	rows, cols := M.Dims()

	if start < 0 || end > rows || start >= end {
		panic(fmt.Sprintf("invalid range [%d, %d) for matrix with %d rows", start, end, rows))
	}

	rangeRows := end - start
	data := make([]float64, rangeRows*cols)

	raw := M.RawMatrix()
	for i := 0; i < rangeRows; i++ {
		srcOffset := (start + i) * cols
		dstOffset := i * cols
		copy(data[dstOffset:dstOffset+cols], raw.Data[srcOffset:srcOffset+cols])
	}

	return mat.NewDense(rangeRows, cols, data)
}

// Predict makes predictions using trained weights
func Predict(X, W *mat.Dense) *mat.Dense {
	var pred mat.Dense
	pred.Mul(X, W)
	return &pred
}

// MSE computes mean squared error
func MSE(pred, truth *mat.Dense) float64 {
	rp, cp := pred.Dims()
	rt, ct := truth.Dims()

	if rp != rt || cp != ct {
		return math.Inf(1)
	}

	var sum float64
	count := 0
	for i := 0; i < rp; i++ {
		for j := 0; j < cp; j++ {
			diff := pred.At(i, j) - truth.At(i, j)
			sum += diff * diff
			count++
		}
	}

	return sum / float64(count)
}
