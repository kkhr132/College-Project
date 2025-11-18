class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"{self.name}({', '.join(self.args)})"

    def __eq__(self, other):
        return self.name == other.name and self.args == other.args

    def __hash__(self):
        return hash((self.name, tuple(self.args)))

class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises  # List of Predicates
        self.conclusion = conclusion  # Predicate

    def __str__(self):
        prem_str = ' ∧ '.join(str(p) for p in self.premises)
        return f"{prem_str} ⇒ {self.conclusion}"

class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Set of Predicates
        self.rules = []  # List of Rules

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def query(self, predicate):
        # Simple forward chaining
        inferred = set()
        while True:
            new_inferences = set()
            for rule in self.rules:
                for fact in self.facts:
                    if self.unify(rule.premises, fact):
                        new_pred = self.substitute(rule.conclusion, fact)
                        if new_pred not in self.facts and new_pred not in inferred:
                            new_inferences.add(new_pred)
            if not new_inferences:
                break
            self.facts.update(new_inferences)
            inferred.update(new_inferences)

        return predicate in self.facts

    def unify(self, premises, fact):
        # Very basic unification for single premise
        if len(premises) == 1:
            prem = premises[0]
            if prem.name == fact.name and len(prem.args) == len(fact.args):
                return True
        return False

    def substitute(self, conclusion, fact):
        # Simple substitution assuming same structure
        return Predicate(conclusion.name, fact.args)

# Example usage
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Facts
    kb.add_fact(Predicate("Human", ["Socrates"]))
    kb.add_fact(Predicate("Human", ["Plato"]))

    # Rule: All humans are mortal
    rule = Rule([Predicate("Human", ["x"])], Predicate("Mortal", ["x"]))
    kb.add_rule(rule)

    # Query
    print("Is Socrates mortal?", kb.query(Predicate("Mortal", ["Socrates"])))
    print("Is Plato mortal?", kb.query(Predicate("Mortal", ["Plato"])))
    print("Is Socrates human?", kb.query(Predicate("Human", ["Socrates"])))
