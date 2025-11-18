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

# Example for credit scoring
def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

if __name__ == "__main__":
    # Input variables: income, debt, credit_history
    income_universe = np.linspace(0, 100000, 100)
    debt_universe = np.linspace(0, 50000, 100)
    history_universe = np.linspace(0, 1, 100)

    low_income = FuzzySet('low', income_universe, lambda x: triangular_membership(x, 0, 0, 50000))
    high_income = FuzzySet('high', income_universe, lambda x: triangular_membership(x, 50000, 100000, 100000))

    low_debt = FuzzySet('low', debt_universe, lambda x: triangular_membership(x, 0, 0, 25000))
    high_debt = FuzzySet('high', debt_universe, lambda x: triangular_membership(x, 25000, 50000, 50000))

    poor_history = FuzzySet('poor', history_universe, lambda x: triangular_membership(x, 0, 0, 0.5))
    good_history = FuzzySet('good', history_universe, lambda x: triangular_membership(x, 0.5, 1, 1))

    input_vars = {
        'income': [low_income, high_income],
        'debt': [low_debt, high_debt],
        'credit_history': [poor_history, good_history]
    }

    # Output: credit_score (0 low, 1 high)
    score_universe = np.linspace(0, 1, 100)
    low_score = FuzzySet('low_score', score_universe, lambda x: triangular_membership(x, 0, 0, 0.5))
    high_score = FuzzySet('high_score', score_universe, lambda x: triangular_membership(x, 0.5, 1, 1))
    output_var = [low_score, high_score]

    # Rules
    rules = [
        FuzzyRule([ (low_income, 0), (high_debt, 0), (poor_history, 0) ], low_score),
        FuzzyRule([ (high_income, 0), (low_debt, 0), (good_history, 0) ], high_score),
        # Add more rules as needed
    ]

    fis = FuzzyInferenceSystem(input_vars, output_var, rules)

    # Test with sample data
    sample_inputs = [
        {'income': 30000, 'debt': 20000, 'credit_history': 0.3},
        {'income': 70000, 'debt': 10000, 'credit_history': 0.8}
    ]

    for inputs in sample_inputs:
        score = fis.infer(inputs)
        print(f"Credit score for income {inputs['income']}, debt {inputs['debt']}, history {inputs['credit_history']}: {score:.3f}")
