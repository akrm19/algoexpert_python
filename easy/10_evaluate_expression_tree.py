# This is an input class. Do not edit.
import math


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    if tree.left is None and tree.right is None:
        return tree.value

    left = evaluateExpressionTree(tree.left)
    right = evaluateExpressionTree(tree.right)
    operator = tree.value

    if operator is -1:
        return left + right
    elif operator is -2:
        return right - left
    elif operator is -3:
        result = left / right
        return math.floor(result) if result > 0 else math.ceil(result)
    elif operator is -4:
        return left * right

