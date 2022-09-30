# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #checking case of an empty tree given
        if root is None:
            return 0
        #now we traverse both sides recursively using the function itself
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        #now we return the larger depth value + 1 since the root node counts 
        #for the total depth
        return max(leftDepth, rightDepth)+1