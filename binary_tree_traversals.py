# Binary Tree Traversals

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Recursive Solutions
""" Inorder Traversal:
        1. Left Subtree
        2. Root 
        3. Right Subtree
"""
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

""" Preorder Traversal:
    1. Root
    2. Left Subtree
    3. Right Subtree
    """
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

""" Postorder Traversal:
    1. Left Subtree
    2. Right Subtree
    3. Root
    """
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)
