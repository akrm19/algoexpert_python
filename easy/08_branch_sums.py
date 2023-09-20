# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    totals = []
    branchSumsHelper(root, 0, totals)
    return totals


def branchSumsHelper(root, curr_total, totals):
    if root is None:
        return

    updated_total = root.value + curr_total
    if root.left is None and root.right is None:
        totals.append(updated_total)
        return

    branchSumsHelper(root.left, updated_total, totals)
    branchSumsHelper(root.right, updated_total, totals)
