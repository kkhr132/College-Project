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
    # Input variables
    income_universe = np.linspace(0, 100000, 100)
    credit_score_universe = np.linspace(0, 1, 100)

    low_income = FuzzySet('low', income_universe, lambda x: triangular_membership(x, 0, 0, 50000))
    medium_income = FuzzySet('medium', income_universe, lambda x: triangular_membership(x, 0, 50000, 100000))
    high_income = FuzzySet('high', income_universe, lambda x: triangular_membership(x, 50000, 100000, 100000))

    low_credit = FuzzySet('low', credit_score_universe, lambda x: triangular_membership(x, 0, 0, 0.5))
    high_credit = FuzzySet('high', credit_score_universe, lambda x: triangular_membership(x, 0.5, 1, 1))

    input_vars = {
        'income': [low_income, medium_income, high_income],
        'credit_score': [low_credit, high_credit]
    }

    # Output: risk (0 low, 1 high)
    risk_universe = np.linspace(0, 1, 100)
    low_risk = FuzzySet('low_risk', risk_universe, lambda x: triangular_membership(x, 0, 0, 0.5))
    high_risk = FuzzySet('high_risk', risk_universe, lambda x: triangular_membership(x, 0.5, 1, 1))
    output_var = [low_risk, high_risk]

    # Rules
    rules = [
        FuzzyRule([ (low_income, 0), (low_credit, 0) ], high_risk),
        FuzzyRule([ (high_income, 0), (high_credit, 0) ], low_risk),
        # Add more rules as needed
    ]

    fis = FuzzyInferenceSystem(input_vars, output_var, rules)

    # Test
    inputs = {'income': 40000, 'credit_score': 0.8}
    risk = fis.infer(inputs)
    print(f"Risk level for income {inputs['income']}, credit score {inputs['credit_score']}: {risk:.3f}")
