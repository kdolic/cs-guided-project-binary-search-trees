"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_BST(root):
    validLeft = True
    validRight = True

    if root.left is not None:
        validLeft = is_valid_BST(root.left)

        if root.value < root.left.value:
            return False
        
    if root.right is not None:
        validRight = is_valid_BST(root.right)

        if root.value > root.right.value:
            return False
    
    if validLeft == True and validRight == True:
        return True
    else: 
        return False


validRootTree = TreeNode(5)
validRootTree.left = TreeNode(3)
validRootTree.right = TreeNode(7)

invalidRootTree = TreeNode(10)
invalidRootTree.left = TreeNode(2)
invalidRootTree.right = TreeNode(8)
invalidRootTree.right.left = TreeNode(6)
invalidRootTree.right.right = TreeNode(12)

invalidTree2 = TreeNode(20)
invalidTree2.left = TreeNode(10)
invalidTree2.left.right = TreeNode(5)
invalidTree2.right = TreeNode(30)

print(f'1st tree is: {is_valid_BST(validRootTree)}')
print(f'2nd tree is: {is_valid_BST(invalidRootTree)}')
print(f'3rd tree is: {is_valid_BST(invalidTree2)}')