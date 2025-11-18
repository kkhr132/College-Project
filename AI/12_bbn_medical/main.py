import numpy as np

class BayesianNetwork:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, name, parents, cpt):
        self.nodes[name] = {'parents': parents, 'cpt': cpt}
        self.edges[name] = parents

    def get_probability(self, node, evidence):
        parents = self.nodes[node]['parents']
        cpt = self.nodes[node]['cpt']

        key = tuple(evidence[parent] for parent in parents)
        if node in evidence:
            return cpt[key][evidence[node]]
        else:
            return {state: prob for state, prob in enumerate(cpt[key])}

    def infer(self, query, evidence):
        # Simple enumeration for inference
        if query in evidence:
            return 1.0 if evidence[query] else 0.0

        # Compute P(query | evidence) = P(query, evidence) / P(evidence)
        p_query_evidence = self.enumerate_all(self.nodes.keys(), {**evidence, query: 1})
        p_evidence = self.enumerate_all(self.nodes.keys(), evidence)

        return p_query_evidence / p_evidence if p_evidence > 0 else 0

    def enumerate_all(self, variables, evidence):
        if not variables:
            return 1.0

        var = variables[0]
        rest = variables[1:]

        if var in evidence:
            prob = self.get_probability(var, evidence)[evidence[var]]
            return prob * self.enumerate_all(rest, evidence)
        else:
            prob = 0
            for state in [0, 1]:  # Assuming binary variables
                new_evidence = {**evidence, var: state}
                prob += self.get_probability(var, new_evidence)[state] * self.enumerate_all(rest, new_evidence)
            return prob

# Example: Medical diagnosis for a disease
if __name__ == "__main__":
    bn = BayesianNetwork()

    # Nodes: Fever, Cough, Disease
    # P(Disease)
    bn.add_node('Disease', [], {(): [0.1, 0.9]})  # P(Disease=0)=0.1, P(Disease=1)=0.9

    # P(Fever | Disease)
    bn.add_node('Fever', ['Disease'], {(0,): [0.8, 0.2], (1,): [0.3, 0.7]})

    # P(Cough | Disease)
    bn.add_node('Cough', ['Disease'], {(0,): [0.7, 0.3], (1,): [0.2, 0.8]})

    # Infer P(Disease=1 | Fever=1, Cough=1)
    evidence = {'Fever': 1, 'Cough': 1}
    prob_disease = bn.infer('Disease', evidence)
    print(f"P(Disease=1 | Fever=1, Cough=1) = {prob_disease}")

    # Infer P(Disease=1 | Fever=0, Cough=0)
    evidence2 = {'Fever': 0, 'Cough': 0}
    prob_disease2 = bn.infer('Disease', evidence2)
    print(f"P(Disease=1 | Fever=0, Cough=0) = {prob_disease2}")
