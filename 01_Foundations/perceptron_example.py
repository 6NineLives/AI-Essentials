"""
Perceptron Example
A minimal, runnable example of a perceptron - the simplest neural network unit.
Demonstrates binary classification using a perceptron built from scratch.
"""

import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    """Simple perceptron classifier"""
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        
    def activation(self, x):
        """Step activation function: returns 1 if x >= 0, else 0"""
        return np.where(x >= 0, 1, 0)
    
    def fit(self, X, y):
        """Train the perceptron"""
        n_samples, n_features = X.shape
        
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Training loop
        for iteration in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                # Calculate linear output
                linear_output = np.dot(x_i, self.weights) + self.bias
                # Apply activation function
                y_predicted = self.activation(linear_output)
                
                # Update weights and bias if prediction is wrong
                update = self.learning_rate * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update
                
        return self
    
    def predict(self, X):
        """Make predictions"""
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation(linear_output)

def generate_linearly_separable_data(n_samples=100):
    """Generate sample data for binary classification"""
    np.random.seed(42)
    
    # Class 0: centered around (2, 2)
    X1 = np.random.randn(n_samples // 2, 2) + np.array([2, 2])
    y1 = np.zeros(n_samples // 2)
    
    # Class 1: centered around (5, 5)
    X2 = np.random.randn(n_samples // 2, 2) + np.array([5, 5])
    y2 = np.ones(n_samples // 2)
    
    # Combine
    X = np.vstack([X1, X2])
    y = np.concatenate([y1, y2])
    
    # Shuffle
    indices = np.random.permutation(n_samples)
    X = X[indices]
    y = y[indices]
    
    return X, y

def plot_decision_boundary(X, y, perceptron):
    """Visualize the decision boundary"""
    plt.figure(figsize=(10, 6))
    
    # Plot data points
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], 
                color='blue', marker='o', label='Class 0', alpha=0.6)
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], 
                color='red', marker='s', label='Class 1', alpha=0.6)
    
    # Plot decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    # Calculate decision boundary line: w1*x1 + w2*x2 + b = 0
    # Solve for x2: x2 = -(w1*x1 + b) / w2
    if perceptron.weights[1] != 0:
        x_boundary = np.array([x_min, x_max])
        y_boundary = -(perceptron.weights[0] * x_boundary + perceptron.bias) / perceptron.weights[1]
        plt.plot(x_boundary, y_boundary, 'g--', linewidth=2, label='Decision Boundary')
    
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Perceptron Binary Classification')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    
    # Save plot
    output_path = '01_Foundations/perceptron_plot.png'
    try:
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        print(f"   Plot saved to: {output_path}")
    except:
        print(f"   Note: Could not save plot (display only)")
    
    plt.show()

def main():
    print("=" * 60)
    print("PERCEPTRON BINARY CLASSIFICATION EXAMPLE")
    print("=" * 60)
    
    # Generate data
    print("\n1. Generating linearly separable data...")
    X, y = generate_linearly_separable_data(100)
    print(f"   Generated {len(X)} samples with 2 features")
    print(f"   Class 0: {np.sum(y == 0)} samples")
    print(f"   Class 1: {np.sum(y == 1)} samples")
    
    # Train perceptron
    print("\n2. Training perceptron...")
    perceptron = Perceptron(learning_rate=0.01, n_iterations=1000)
    perceptron.fit(X, y)
    
    print(f"   Learned weights: [{perceptron.weights[0]:.3f}, {perceptron.weights[1]:.3f}]")
    print(f"   Learned bias: {perceptron.bias:.3f}")
    
    # Make predictions
    print("\n3. Evaluating model...")
    predictions = perceptron.predict(X)
    accuracy = np.mean(predictions == y) * 100
    print(f"   Training Accuracy: {accuracy:.2f}%")
    
    # Test on new samples
    print("\n4. Testing on new samples...")
    X_new = np.array([
        [1.5, 1.5],  # Should be Class 0
        [6.0, 6.0],  # Should be Class 1
        [3.5, 3.5],  # Near boundary
    ])
    predictions_new = perceptron.predict(X_new)
    
    for i, (x, pred) in enumerate(zip(X_new, predictions_new)):
        print(f"   Sample {i+1}: {x} → Class {int(pred)}")
    
    # Visualize
    print("\n5. Creating visualization...")
    plot_decision_boundary(X, y, perceptron)
    
    print("\n" + "=" * 60)
    print("✅ Perceptron example completed!")
    print("\nKey Concept: The perceptron finds a linear decision boundary")
    print("that separates the two classes. This is the foundation of")
    print("neural networks!")
    print("=" * 60)

if __name__ == "__main__":
    main()
