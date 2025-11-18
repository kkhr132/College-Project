import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

class NeuroFuzzySentiment:
    def __init__(self, num_features, num_rules=5):
        self.num_features = num_features
        self.num_rules = num_rules
        self.centers = np.random.rand(num_rules, num_features)
        self.widths = np.random.rand(num_rules, num_features)
        self.consequents = np.random.rand(num_rules, 3)  # 3 classes: negative, neutral, positive
        self.weights = np.ones(num_rules)

    def gaussian_membership(self, x, center, width):
        return np.exp(-0.5 * ((x - center) / width) ** 2)

    def forward(self, inputs):
        # Fuzzification
        memberships = np.zeros((self.num_rules, self.num_features))
        for i in range(self.num_rules):
            for j in range(self.num_features):
                memberships[i, j] = self.gaussian_membership(inputs[j], self.centers[i, j], self.widths[i, j])

        # Rule firing strengths
        firing_strengths = np.prod(memberships, axis=1) * self.weights

        # Normalization
        total_strength = np.sum(firing_strengths)
        normalized_strengths = firing_strengths / total_strength if total_strength > 0 else np.ones(self.num_rules) / self.num_rules

        # Defuzzification (classification)
        output = np.sum(normalized_strengths[:, np.newaxis] * self.consequents, axis=0)
        return np.argmax(output)  # Return class with highest probability

    def train(self, X, y, epochs=10, lr=0.01):
        for epoch in range(epochs):
            correct = 0
            for i in range(len(X)):
                inputs = X[i]
                target = y[i]

                # Forward pass
                output_class = self.forward(inputs)

                # Compute error (simplified)
                if output_class == target:
                    correct += 1
                else:
                    # Update consequents (simplified gradient descent)
                    memberships = np.zeros((self.num_rules, self.num_features))
                    for r in range(self.num_rules):
                        for j in range(self.num_features):
                            memberships[r, j] = self.gaussian_membership(inputs[j], self.centers[r, j], self.widths[r, j])

                    firing_strengths = np.prod(memberships, axis=1) * self.weights
                    total_strength = np.sum(firing_strengths)
                    normalized_strengths = firing_strengths / total_strength if total_strength > 0 else np.ones(self.num_rules) / self.num_rules

                    for r in range(self.num_rules):
                        # Simplified update
                        self.consequents[r, target] += lr * normalized_strengths[r]
                        self.consequents[r, output_class] -= lr * normalized_strengths[r]

            accuracy = correct / len(X)
            print(f"Epoch {epoch + 1}: Accuracy = {accuracy:.3f}")

# Example usage with hypothetical data
if __name__ == "__main__":
    # Hypothetical movie reviews
    reviews = [
        "This movie is terrible",  # negative
        "I loved this film",       # positive
        "It's okay",               # neutral
        "Worst movie ever",        # negative
        "Amazing story",           # positive
        "Not bad",                 # neutral
        "Horrible acting",         # negative
        "Great cinematography",    # positive
        "Meh",                     # neutral
        "Fantastic",               # positive
    ]
    labels = [0, 2, 1, 0, 2, 1, 0, 2, 1, 2]  # 0: negative, 1: neutral, 2: positive

    # Vectorize
    vectorizer = TfidfVectorizer(max_features=10)
    X = vectorizer.fit_transform(reviews).toarray()
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = NeuroFuzzySentiment(num_features=X.shape[1])
    model.train(X_train, y_train, epochs=20)

    # Test
    correct = 0
    for i in range(len(X_test)):
        pred = model.forward(X_test[i])
        if pred == y_test[i]:
            correct += 1
        print(f"Review: {reviews[i]} | Predicted: {pred} | Actual: {y_test[i]}")

    print(f"Test Accuracy: {correct / len(X_test):.3f}")
