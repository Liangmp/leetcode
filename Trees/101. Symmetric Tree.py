# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.checkSym(root.left, root.right)
    
    def checkSym(self, Left, Right):
        if Left is None and Right is None:
            return True
        if Left and Right and Left.val == Right.val: # check their children
            return self.checkSym(Left.left, Right.right) and self.checkSym(Left.right, Right.left)    
        else:
            return False
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        