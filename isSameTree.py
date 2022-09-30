# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #first check if their roots are of same or different values
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False

        else:
            if p.val != q.val:
                return False
            #if values are the same we solve with recursion
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)