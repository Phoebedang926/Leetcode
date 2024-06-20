# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cursum):
            if not root:
                return
            cursum +=root.val
            
            if not root.left and not root.right:
                return cursum == targetSum
            return dfs(root.left, cursum) or dfs(root.right, cursum)
        
        return dfs(root, 0)
            
        
                
                
            
        