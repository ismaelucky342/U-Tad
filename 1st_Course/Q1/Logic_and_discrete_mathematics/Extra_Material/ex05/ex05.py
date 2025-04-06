class DecisionTreeNode:
    def __init__(self, proposition=None, yes_branch=None, no_branch=None):
        """
        Initialize a node in the decision tree.
        :param proposition: The logical proposition or question at this node.
        :param yes_branch: The child node if the answer to the proposition is 'yes' (True).
        :param no_branch: The child node if the answer to the proposition is 'no' (False).
        """
        self.proposition = proposition
        self.yes_branch = yes_branch
        self.no_branch = no_branch

    def is_leaf(self):
        """
        Check if the node is a leaf (i.e., has no children).
        :return: True if the node is a leaf, False otherwise.
        """
        return self.yes_branch is None and self.no_branch is None


class DecisionTree:
    def __init__(self, root=None):
        """
        Initialize the decision tree.
        :param root: The root node of the decision tree.
        """
        self.root = root

    def solve(self, node=None):
        """
        Solve the decision tree by traversing it based on user input.
        :param node: The current node to evaluate (defaults to the root node).
        :return: The final answer at a leaf node.
        """
        if node is None:
            node = self.root

        while not node.is_leaf():
            answer = input(f"{node.proposition} (yes/no): ").strip().lower()
            if answer == 'yes':
                node = node.yes_branch
            elif answer == 'no':
                node = node.no_branch
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")
        
        return node.proposition


# Example Usage
if __name__ == "__main__":
    # Construct a sample decision tree
    leaf1 = DecisionTreeNode(proposition="You should take an umbrella.")
    leaf2 = DecisionTreeNode(proposition="You don't need an umbrella.")
    leaf3 = DecisionTreeNode(proposition="You should wear a jacket.")
    leaf4 = DecisionTreeNode(proposition="You don't need a jacket.")

    node2 = DecisionTreeNode(proposition="Is it raining?", yes_branch=leaf1, no_branch=leaf2)
    node3 = DecisionTreeNode(proposition="Is it cold?", yes_branch=leaf3, no_branch=leaf4)

    root = DecisionTreeNode(proposition="Is the weather bad?", yes_branch=node2, no_branch=node3)

    tree = DecisionTree(root=root)

    # Solve the decision tree
    print("Decision Tree Solver")
    result = tree.solve()
    print(f"Result: {result}")