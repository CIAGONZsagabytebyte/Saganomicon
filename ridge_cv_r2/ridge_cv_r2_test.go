// ridge_cv_r2_test.go
// MIT License – Copyright (c) 2025 Saga Gonzo / KlonkGronkZonk
// Comprehensive tests for Ridge CV R² optimization

package ridge_cv_r2

import (
	"fmt"
	"math"
	"testing"

	"gonum.org/v1/gonum/mat"
)

const epsilon = 1e-9

func TestNewRidgeCV(t *testing.T) {
	tests := []struct {
		name           string
		k              int
		lambdas        []float64
		expectedK      int
		expectedLambda int
	}{
		{"default lambdas", 5, nil, 5, 101},
		{"custom lambdas", 10, []float64{0.1, 1.0, 10.0}, 10, 3},
		{"k too small", 0, nil, 5, 101},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			cv := NewRidgeCV(tt.k, tt.lambdas...)
			if cv.K != tt.expectedK {
				t.Errorf("expected K=%d, got %d", tt.expectedK, cv.K)
			}
			if len(cv.Lambdas) != tt.expectedLambda {
				t.Errorf("expected %d lambdas, got %d", tt.expectedLambda, len(cv.Lambdas))
			}
		})
	}
}

func TestR2Score(t *testing.T) {
	tests := []struct {
		name     string
		pred     *mat.Dense
		truth    *mat.Dense
		expected float64
	}{
		{
			name:     "perfect prediction",
			pred:     mat.NewDense(3, 1, []float64{1, 2, 3}),
			truth:    mat.NewDense(3, 1, []float64{1, 2, 3}),
			expected: 1.0,
		},
		{
			name:     "worst prediction",
			pred:     mat.NewDense(3, 1, []float64{3, 2, 1}),
			truth:    mat.NewDense(3, 1, []float64{1, 2, 3}),
			expected: -3.0,
		},
		{
			name:     "mean prediction",
			pred:     mat.NewDense(3, 1, []float64{2, 2, 2}),
			truth:    mat.NewDense(3, 1, []float64{1, 2, 3}),
			expected: 0.0,
		},
		{
			name:     "constant truth",
			pred:     mat.NewDense(3, 1, []float64{5, 5, 5}),
			truth:    mat.NewDense(3, 1, []float64{5, 5, 5}),
			expected: 1.0,
		},
		{
			name:     "dimension mismatch",
			pred:     mat.NewDense(3, 1, []float64{1, 2, 3}),
			truth:    mat.NewDense(2, 1, []float64{1, 2}),
			expected: math.Inf(-1),
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			r2 := r2Score(tt.pred, tt.truth)
			if math.IsInf(tt.expected, -1) {
				if !math.IsInf(r2, -1) {
					t.Errorf("expected -Inf, got %f", r2)
				}
			} else if math.Abs(r2-tt.expected) > epsilon {
				t.Errorf("expected R²=%f, got %f", tt.expected, r2)
			}
		})
	}
}

func TestMSE(t *testing.T) {
	tests := []struct {
		name     string
		pred     *mat.Dense
		truth    *mat.Dense
		expected float64
	}{
		{
			name:     "perfect prediction",
			pred:     mat.NewDense(3, 1, []float64{1, 2, 3}),
			truth:    mat.NewDense(3, 1, []float64{1, 2, 3}),
			expected: 0.0,
		},
		{
			name:     "simple error",
			pred:     mat.NewDense(3, 1, []float64{2, 3, 4}),
			truth:    mat.NewDense(3, 1, []float64{1, 2, 3}),
			expected: 1.0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			mse := MSE(tt.pred, tt.truth)
			if math.Abs(mse-tt.expected) > epsilon {
				t.Errorf("expected MSE=%f, got %f", tt.expected, mse)
			}
		})
	}
}

func TestRidgeRegression(t *testing.T) {
	// Simple linear problem: y = 2*x + 1
	X := mat.NewDense(5, 2, []float64{
		1, 0,
		1, 1,
		1, 2,
		1, 3,
		1, 4,
	})
	Y := mat.NewDense(5, 1, []float64{1, 3, 5, 7, 9})

	tests := []struct {
		name         string
		lambda       float64
		expectError  bool
		checkWeights bool
	}{
		{"no regularization", 0.0, false, true},
		{"small regularization", 0.01, false, true},
		{"large regularization", 100.0, false, false},
		{"negative lambda", -1.0, true, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			W, err := RidgeRegression(X, Y, tt.lambda)

			if tt.expectError {
				if err == nil {
					t.Error("expected error, got nil")
				}
				return
			}

			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			if tt.checkWeights {
				// Check that weights are reasonable
				r, c := W.Dims()
				if r != 2 || c != 1 {
					t.Errorf("expected weights shape (2,1), got (%d,%d)", r, c)
				}

				// For lambda=0, should get exact solution: [1, 2]
				if tt.lambda == 0.0 {
					w0, w1 := W.At(0, 0), W.At(1, 0)
					if math.Abs(w0-1.0) > 0.01 || math.Abs(w1-2.0) > 0.01 {
						t.Errorf("expected weights ~[1, 2], got [%f, %f]", w0, w1)
					}
				}
			}
		})
	}
}

func TestRidgeRegressionEdgeCases(t *testing.T) {
	tests := []struct {
		name        string
		X           *mat.Dense
		Y           *mat.Dense
		lambda      float64
		expectError bool
	}{
		{
			name:        "nil X",
			X:           nil,
			Y:           mat.NewDense(1, 1, []float64{1}),
			lambda:      1.0,
			expectError: true,
		},
		{
			name:        "nil Y",
			X:           mat.NewDense(1, 1, []float64{1}),
			Y:           nil,
			lambda:      1.0,
			expectError: true,
		},
		{
			name:        "mismatched rows",
			X:           mat.NewDense(3, 2, []float64{1, 2, 3, 4, 5, 6}),
			Y:           mat.NewDense(2, 1, []float64{1, 2}),
			lambda:      1.0,
			expectError: true,
		},
		{
			name:        "zero dimensions",
			X:           mat.NewDense(1, 1, []float64{0}),
			Y:           mat.NewDense(1, 1, []float64{0}),
			lambda:      1.0,
			expectError: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			_, err := RidgeRegression(tt.X, tt.Y, tt.lambda)
			if tt.expectError && err == nil {
				t.Error("expected error, got nil")
			}
			if !tt.expectError && err != nil {
				t.Errorf("unexpected error: %v", err)
			}
		})
	}
}

func TestSliceExclude(t *testing.T) {
	M := mat.NewDense(5, 2, []float64{
		1, 2,
		3, 4,
		5, 6,
		7, 8,
		9, 10,
	})

	excluded := sliceExclude(M, 1, 3)
	r, c := excluded.Dims()

	if r != 3 || c != 2 {
		t.Errorf("expected shape (3,2), got (%d,%d)", r, c)
	}

	expected := []float64{1, 2, 7, 8, 9, 10}
	actual := excluded.RawMatrix().Data

	for i, v := range expected {
		if math.Abs(actual[i]-v) > epsilon {
			t.Errorf("at index %d: expected %f, got %f", i, v, actual[i])
		}
	}
}

func TestSliceRange(t *testing.T) {
	M := mat.NewDense(5, 2, []float64{
		1, 2,
		3, 4,
		5, 6,
		7, 8,
		9, 10,
	})

	slice := sliceRange(M, 1, 3)
	r, c := slice.Dims()

	if r != 2 || c != 2 {
		t.Errorf("expected shape (2,2), got (%d,%d)", r, c)
	}

	expected := []float64{3, 4, 5, 6}
	actual := slice.RawMatrix().Data

	for i, v := range expected {
		if math.Abs(actual[i]-v) > epsilon {
			t.Errorf("at index %d: expected %f, got %f", i, v, actual[i])
		}
	}
}

func TestCrossValidate(t *testing.T) {
	// Generate synthetic data: y = 3*x1 + 2*x2 + noise
	X := mat.NewDense(20, 2, []float64{
		1, 1, 1, 2, 1, 3, 1, 4, 1, 5,
		2, 1, 2, 2, 2, 3, 2, 4, 2, 5,
		3, 1, 3, 2, 3, 3, 3, 4, 3, 5,
		4, 1, 4, 2, 4, 3, 4, 4, 4, 5,
	})

	Y := mat.NewDense(20, 1, nil)
	for i := 0; i < 20; i++ {
		y := 3*X.At(i, 0) + 2*X.At(i, 1)
		Y.Set(i, 0, y)
	}

	tests := []struct {
		name        string
		k           int
		lambdas     []float64
		expectError bool
	}{
		{"5-fold CV", 5, []float64{0.001, 0.01, 0.1, 1.0, 10.0}, false},
		{"too many folds", 25, []float64{0.1, 1.0}, true},
		{"nil X", 5, []float64{0.1}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			cv := NewRidgeCV(tt.k, tt.lambdas...)

			var result *CVResult
			var err error

			if tt.name == "nil X" {
				result, err = cv.CrossValidate(nil, Y)
			} else {
				result, err = cv.CrossValidate(X, Y)
			}

			if tt.expectError {
				if err == nil {
					t.Error("expected error, got nil")
				}
				return
			}

			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			if result.W == nil {
				t.Error("expected non-nil weights")
			}

			if result.BestR2 <= 0 {
				t.Errorf("expected positive R², got %f", result.BestR2)
			}

			if result.BestLambda < 0 {
				t.Errorf("expected non-negative lambda, got %f", result.BestLambda)
			}

			t.Logf("Best lambda: %f, R²: %f", result.BestLambda, result.BestR2)
		})
	}
}

func TestPredict(t *testing.T) {
	X := mat.NewDense(3, 2, []float64{
		1, 2,
		3, 4,
		5, 6,
	})
	W := mat.NewDense(2, 1, []float64{2, 3})

	pred := Predict(X, W)
	r, c := pred.Dims()

	if r != 3 || c != 1 {
		t.Errorf("expected shape (3,1), got (%d,%d)", r, c)
	}

	// Expected: [2*1+3*2, 2*3+3*4, 2*5+3*6] = [8, 18, 28]
	expected := []float64{8, 18, 28}
	for i, v := range expected {
		if math.Abs(pred.At(i, 0)-v) > epsilon {
			t.Errorf("at row %d: expected %f, got %f", i, v, pred.At(i, 0))
		}
	}
}

// Benchmark tests
func BenchmarkRidgeRegression(b *testing.B) {
	sizes := []int{10, 100, 500}

	for _, n := range sizes {
		b.Run(fmt.Sprintf("n=%d", n), func(b *testing.B) {
			X := mat.NewDense(n, 10, nil)
			Y := mat.NewDense(n, 1, nil)

			// Fill with random-ish data
			for i := 0; i < n; i++ {
				for j := 0; j < 10; j++ {
					X.Set(i, j, float64(i*j))
				}
				Y.Set(i, 0, float64(i))
			}

			b.ResetTimer()
			for i := 0; i < b.N; i++ {
				_, _ = RidgeRegression(X, Y, 1.0)
			}
		})
	}
}

func BenchmarkCrossValidate(b *testing.B) {
	X := mat.NewDense(100, 10, nil)
	Y := mat.NewDense(100, 1, nil)

	for i := 0; i < 100; i++ {
		for j := 0; j < 10; j++ {
			X.Set(i, j, float64(i*j))
		}
		Y.Set(i, 0, float64(i))
	}

	cv := NewRidgeCV(5, 0.01, 0.1, 1.0, 10.0)

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, _ = cv.CrossValidate(X, Y)
	}
}
