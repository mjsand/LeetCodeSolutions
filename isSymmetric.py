# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        #now we define a recursive function to solve the tree search
        def isMirror(left, right):
            #check the cases where left node and right node are both none
            if left is None and right is None:
                return True
            #or when only one of them is
            if left is None or right is None:
                return False
            
            if left.val == right.val:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            else:
                return False
            
        return isMirror(root.left, root.right)
            
            