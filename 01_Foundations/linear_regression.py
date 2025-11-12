"""
Linear Regression Example
A minimal, runnable example demonstrating linear regression from scratch and with scikit-learn.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def generate_sample_data(n_samples=100):
    """Generate sample data for linear regression"""
    np.random.seed(42)
    X = np.random.rand(n_samples, 1) * 10  # Features between 0 and 10
    y = 2.5 * X + 3 + np.random.randn(n_samples, 1) * 2  # y = 2.5x + 3 + noise
    return X, y

def linear_regression_from_scratch(X, y):
    """Implement linear regression using normal equation: w = (X^T X)^-1 X^T y"""
    # Add bias term (column of ones)
    X_with_bias = np.c_[np.ones((X.shape[0], 1)), X]
    
    # Normal equation: w = (X^T X)^-1 X^T y
    weights = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y
    
    return weights

def predict(X, weights):
    """Make predictions using learned weights"""
    X_with_bias = np.c_[np.ones((X.shape[0], 1)), X]
    return X_with_bias @ weights

def main():
    print("=" * 60)
    print("LINEAR REGRESSION EXAMPLE")
    print("=" * 60)
    
    # Generate data
    print("\n1. Generating sample data...")
    X, y = generate_sample_data(100)
    print(f"   Generated {len(X)} samples")
    print(f"   True relationship: y ≈ 2.5x + 3 (with noise)")
    
    # Method 1: From scratch
    print("\n2. Training linear regression from scratch...")
    weights_scratch = linear_regression_from_scratch(X, y)
    predictions_scratch = predict(X, weights_scratch)
    mse_scratch = mean_squared_error(y, predictions_scratch)
    
    print(f"   Learned equation: y = {weights_scratch[1][0]:.2f}x + {weights_scratch[0][0]:.2f}")
    print(f"   Mean Squared Error: {mse_scratch:.2f}")
    
    # Method 2: Using scikit-learn
    print("\n3. Training with scikit-learn...")
    model = LinearRegression()
    model.fit(X, y)
    predictions_sklearn = model.predict(X)
    mse_sklearn = mean_squared_error(y, predictions_sklearn)
    r2 = r2_score(y, predictions_sklearn)
    
    print(f"   Learned equation: y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}")
    print(f"   Mean Squared Error: {mse_sklearn:.2f}")
    print(f"   R² Score: {r2:.3f}")
    
    # Make predictions on new data
    print("\n4. Making predictions on new data...")
    X_new = np.array([[5.0], [7.5]])
    predictions_new = model.predict(X_new)
    
    for x_val, y_pred in zip(X_new, predictions_new):
        print(f"   Input: {x_val[0]:.1f} → Prediction: {y_pred[0]:.2f}")
    
    # Visualization
    print("\n5. Creating visualization...")
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.5, label='Training Data')
    plt.plot(X, predictions_sklearn, 'r-', linewidth=2, label='Fitted Line')
    plt.scatter(X_new, predictions_new, color='green', s=100, marker='*', 
                label='New Predictions', zorder=5)
    plt.xlabel('X (Feature)')
    plt.ylabel('y (Target)')
    plt.title('Linear Regression Example')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot
    output_path = '01_Foundations/linear_regression_plot.png'
    try:
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        print(f"   Plot saved to: {output_path}")
    except:
        print(f"   Note: Could not save plot (display only)")
    
    plt.show()
    
    print("\n" + "=" * 60)
    print("✅ Linear Regression example completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
