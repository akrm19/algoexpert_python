def nodeDepths(root):
    # Write your code here.
    return add_node_depths(root, 0)

def add_node_depths(node, cur_level):
    if node is None:
        return 0

    return cur_level \
        + add_node_depths(node.left, cur_level + 1) \
        + add_node_depths(node.right, cur_level + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
