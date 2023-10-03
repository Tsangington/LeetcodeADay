"""
100. Same Tree

Given the roots of two binary trees p and q,
 write a function to check if they are the same or not.

Two binary trees are considered the same if 
they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        
        self.preOrder(p, tree1)
        self.preOrder(q, tree2)

        if tree1 == tree2:
            return True
        return False
        
    def preOrder(self, root, tree):
        if root:
            tree.append(root.val)
        
            self.preOrder(root.left, tree)
            self.preOrder(root.right, tree)
        tree.append(0)