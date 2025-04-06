class Node:
    """Class to represent a node in the expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    """Class to generate and evaluate an expression tree."""
    def __init__(self):
        self.root = None

    def build_tree(self, expression):
        """
        Build an expression tree from a postfix expression.
        :param expression: List of tokens in postfix notation.
        """
        stack = []
        for token in expression:
            if token.isdigit():  # Operand
                stack.append(Node(int(token)))
            elif token in "+-*/":  # Operator
                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        self.root = stack.pop()

    def evaluate(self, node=None):
        """
        Evaluate the expression tree.
        :param node: Current node (default is root).
        :return: Result of the evaluation.
        """
        if node is None:
            node = self.root

        # If the node is a leaf, return its value
        if node.left is None and node.right is None:
            return node.value

        # Recursively evaluate left and right subtrees
        left_value = self.evaluate(node.left)
        right_value = self.evaluate(node.right)

        # Apply the operator
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value

    def inorder_traversal(self, node=None):
        """
        Perform an inorder traversal of the tree.
        :param node: Current node (default is root).
        :return: List of values in inorder.
        """
        if node is None:
            node = self.root

        result = []
        if node.left:
            result.extend(self.inorder_traversal(node.left))
        result.append(node.value)
        if node.right:
            result.extend(self.inorder_traversal(node.right))
        return result


# Example usage
if __name__ == "__main__":
    # Postfix expression: 3 4 + 2 * 7 /
    expression = ["3", "4", "+", "2", "*", "7", "/"]

    tree = ExpressionTree()
    tree.build_tree(expression)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Evaluation Result:", tree.evaluate())