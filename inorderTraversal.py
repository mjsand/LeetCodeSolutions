# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        #handling empty input case
        if root is None:
            return None
        #now we can define our recursive function to solve inorder traversal
        def inOrder(root):
            if root:
                #inorder traversal means visiting the left side first
                #and we add the value(s) to our list
                inOrder(root.left)
                output.append(root.val)
                #now we visit the right side
                inOrder(root.right)
                
        #now we call the recursive function with the original root
        inOrder(root)
        return output