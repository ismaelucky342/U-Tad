from itertools import product

class Proposition:
    def __init__(self, name):
        self.name = name

    def evaluate(self, values):
        return values[self.name]

    def __str__(self):
        return self.name


class Not:
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, values):
        return not self.operand.evaluate(values)

    def __str__(self):
        return f"¬{self.operand}"


class And:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return self.left.evaluate(values) and self.right.evaluate(values)

    def __str__(self):
        return f"({self.left} ∧ {self.right})"


class Or:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return self.left.evaluate(values) or self.right.evaluate(values)

    def __str__(self):
        return f"({self.left} ∨ {self.right})"


class Implies:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return not self.left.evaluate(values) or self.right.evaluate(values)

    def __str__(self):
        return f"({self.left} → {self.right})"


class Biconditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, values):
        return self.left.evaluate(values) == self.right.evaluate(values)

    def __str__(self):
        return f"({self.left} ↔ {self.right})"


def truth_table(expression, propositions):

    print(" | ".join(propositions) + " | Result")
    print("-" * (4 * len(propositions) + 10))

    for values in product([False, True], repeat=len(propositions)):
        values_dict = dict(zip(propositions, values))
        result = expression.evaluate(values_dict)
        row = " | ".join(str(values_dict[prop]) for prop in propositions)
        print(f"{row} | {result}")


# Example usage
if __name__ == "__main__":
    # Define propositions
    p = Proposition("P")
    q = Proposition("Q")

    # Define a logical expression: (P ∧ Q) → ¬P
    expression = Implies(And(p, q), Not(p))

    # Print the truth table
    truth_table(expression, ["P", "Q"])