def nodeDepths(root):
    # Write your code here.
    stack = [TreeNode(root, 0)]
    total = 0

    while len(stack) > 0:
        cur = stack.pop()
        if cur.node is None:
            continue
        total += cur.depth
        stack.append(TreeNode(cur.node.left, cur.depth + 1))
        stack.append(TreeNode(cur.node.right, cur.depth + 1))

    return total

class TreeNode:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
