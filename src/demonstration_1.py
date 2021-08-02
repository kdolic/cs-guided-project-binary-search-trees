"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    if root.left is None and root.right is None:
        return 1

    left_depth = 0
    right_depth = 0

    if root.left is not None:
        left_depth = maxDepth(root.left)

    if root.right is not None:
        right_depth = maxDepth(root.right)

    greatest_depth = max(left_depth, right_depth)
    return greatest_depth + 1

root = BinaryTreeNode(5)
root.right = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(4)
root.right.left = BinaryTreeNode(8)
root.left = BinaryTreeNode(12)

print(maxDepth(root))
