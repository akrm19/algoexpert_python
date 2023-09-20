
def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, tree.value)

def findClosestValueHelper(tree, target, cur_closest):
    # Write your code here.
    if tree is None:
        return cur_closest
    if tree.value == target:
        return target

    existing_dif = abs(target - cur_closest)
    new_diff = abs(target - tree.value)

    if existing_dif > new_diff:
        cur_closest = tree.value

    if target > tree.value:
        return findClosestValueHelper(tree.right, target, cur_closest)
    else:
        return findClosestValueHelper(tree.left, target, cur_closest)

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
