# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n +=1
            if n == k:
                return cur.val
            cur = cur.right
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
        
#         n = 0
#         stack = []
#         curr = root

#         if not root:
#             return
        
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
            
#             curr  = stack.pop()
#             n +=1
#             if n == k:
#                 return curr.val
            
#             curr = curr.right


        