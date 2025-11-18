import numpy as np

class NeuroFuzzyController:
    def __init__(self, input_dim, output_dim, num_rules):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.num_rules = num_rules
        self.centers = np.random.rand(num_rules, input_dim)
        self.widths = np.random.rand(num_rules, input_dim)
        self.consequents = np.random.rand(num_rules, output_dim)
        self.weights = np.ones(num_rules)

    def gaussian_membership(self, x, center, width):
        return np.exp(-0.5 * ((x - center) / width) ** 2)

    def forward(self, inputs):
        # Fuzzification
        memberships = np.zeros((self.num_rules, self.input_dim))
        for i in range(self.num_rules):
            for j in range(self.input_dim):
                memberships[i, j] = self.gaussian_membership(inputs[j], self.centers[i, j], self.widths[i, j])

        # Rule firing strengths
        firing_strengths = np.prod(memberships, axis=1) * self.weights

        # Normalization
        total_strength = np.sum(firing_strengths)
        if total_strength == 0:
            normalized_strengths = np.ones(self.num_rules) / self.num_rules
        else:
            normalized_strengths = firing_strengths / total_strength

        # Defuzzification
        output = np.sum(normalized_strengths[:, np.newaxis] * self.consequents, axis=0)
        return output

    def train(self, X, y, epochs=100, lr=0.01):
        for epoch in range(epochs):
            for i in range(len(X)):
                inputs = X[i]
                target = y[i]

                # Forward pass
                output = self.forward(inputs)

                # Compute error
                error = target - output

                # Update consequents
                memberships = np.zeros((self.num_rules, self.input_dim))
                for r in range(self.num_rules):
                    for j in range(self.input_dim):
                        memberships[r, j] = self.gaussian_membership(inputs[j], self.centers[r, j], self.widths[r, j])

                firing_strengths = np.prod(memberships, axis=1) * self.weights
                total_strength = np.sum(firing_strengths)
                normalized_strengths = firing_strengths / total_strength if total_strength > 0 else np.ones(self.num_rules) / self.num_rules

                for r in range(self.num_rules):
                    self.consequents[r] += lr * normalized_strengths[r] * error

# Example: Control a simple system (e.g., temperature control)
if __name__ == "__main__":
    # Generate sample data
    X = np.random.rand(100, 2)  # Two inputs: current temp, target temp
    y = X[:, 0] + 0.5 * X[:, 1]  # Simple control output

    controller = NeuroFuzzyController(input_dim=2, output_dim=1, num_rules=5)
    controller.train(X, y, epochs=50)

    # Test
    test_input = np.array([0.5, 0.8])
    output = controller.forward(test_input)
    print(f"Control output for input {test_input}: {output}")
