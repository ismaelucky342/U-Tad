from itertools import permutations, combinations
from math import factorial

def generate_permutations(elements):
    """
    Generate all permutations of a given set of elements.
    """
    return list(permutations(elements))

def generate_combinations(elements, r):
    """
    Generate all combinations of a given set of elements of length r.
    """
    return list(combinations(elements, r))

def count_permutations(elements):
    """
    Calculate the total number of permutations of a given set of elements.
    """
    return factorial(len(elements))

def count_combinations(elements, r):
    """
    Calculate the total number of combinations of a given set of elements of length r.
    """
    n = len(elements)
    return factorial(n) // (factorial(r) * factorial(n - r))

# Example usage
if __name__ == "__main__":
    elements = ['A', 'B', 'C']
    r = 2

    print("Permutations:")
    print(generate_permutations(elements))
    print("Total permutations:", count_permutations(elements))

    print("\nCombinations:")
    print(generate_combinations(elements, r))
    print("Total combinations:", count_combinations(elements, r))