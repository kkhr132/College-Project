import numpy as np

class FuzzySet:
    def __init__(self, name, universe, membership_func):
        self.name = name
        self.universe = universe
        self.membership_func = membership_func

    def membership(self, x):
        return self.membership_func(x)

class FuzzyRule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents  # List of (fuzzy_set, input_value)
        self.consequent = consequent  # FuzzySet for output

    def firing_strength(self, inputs):
        strength = 1.0
        for fuzzy_set, input_value in self.antecedents:
            strength *= fuzzy_set.membership(input_value)
        return strength

class FuzzyInferenceSystem:
    def __init__(self, input_vars, output_var, rules):
        self.input_vars = input_vars  # Dict of var_name: list of FuzzySets
        self.output_var = output_var  # List of FuzzySets for output
        self.rules = rules

    def fuzzify(self, inputs):
        fuzzy_inputs = {}
        for var, value in inputs.items():
            fuzzy_inputs[var] = {fs.name: fs.membership(value) for fs in self.input_vars[var]}
        return fuzzy_inputs

    def infer(self, inputs):
        fuzzy_inputs = self.fuzzify(inputs)
        output_strengths = {fs.name: 0.0 for fs in self.output_var}

        for rule in self.rules:
            strength = rule.firing_strength([(self.input_vars[var][0], inputs[var]) for var in self.input_vars])  # Simplified
            for fs in self.output_var:
                if fs.name == rule.consequent.name:
                    output_strengths[fs.name] = max(output_strengths[fs.name], strength)

        # Defuzzification (centroid method)
        output = 0.0
        total = 0.0
        for fs in self.output_var:
            strength = output_strengths[fs.name]
            if strength > 0:
                # Simplified centroid
                center = np.mean(fs.universe)
                output += strength * center
                total += strength
        return output / total if total > 0 else 0.5

# Example for sentiment analysis
def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

if __name__ == "__main__":
    # Input: sentiment score from -1 to 1
    score_universe = np.linspace(-1, 1, 100)

    negative = FuzzySet('negative', score_universe, lambda x: triangular_membership(x, -1, -1, 0))
    neutral = FuzzySet('neutral', score_universe, lambda x: triangular_membership(x, -0.5, 0, 0.5))
    positive = FuzzySet('positive', score_universe, lambda x: triangular_membership(x, 0, 1, 1))

    input_vars = {
        'score': [negative, neutral, positive]
    }

    # Output: sentiment class (0 negative, 1 neutral, 2 positive)
    sentiment_universe = np.linspace(0, 2, 100)
    neg_sent = FuzzySet('negative', sentiment_universe, lambda x: triangular_membership(x, 0, 0, 1))
    neu_sent = FuzzySet('neutral', sentiment_universe, lambda x: triangular_membership(x, 0.5, 1, 1.5))
    pos_sent = FuzzySet('positive', sentiment_universe, lambda x: triangular_membership(x, 1, 2, 2))
    output_var = [neg_sent, neu_sent, pos_sent]

    # Rules
    rules = [
        FuzzyRule([(negative, 0)], neg_sent),
        FuzzyRule([(neutral, 0)], neu_sent),
        FuzzyRule([(positive, 0)], pos_sent),
    ]

    fis = FuzzyInferenceSystem(input_vars, output_var, rules)

    # Test with hypothetical scores
    test_scores = [-0.8, 0.0, 0.7]
    for score in test_scores:
        sentiment = fis.infer({'score': score})
        label = 'negative' if sentiment < 0.67 else 'neutral' if sentiment < 1.33 else 'positive'
        print(f"Sentiment score {score}: {label} ({sentiment:.3f})")
