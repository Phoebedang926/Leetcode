# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtracking(root, cursum):
            if not root:
                return False
            cursum += root.val
            
            if not root.left and not root.right:
                return cursum == targetSum
            if backtracking(root.left, cursum):
                return True
            if backtracking(root.right, cursum):
                return True
            return False
        return backtracking(root, 0)
                
                
            
        