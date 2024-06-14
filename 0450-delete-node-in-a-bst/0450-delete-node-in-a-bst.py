# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findminNode(root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)   
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                minleaf = findminNode(root.right)
                root.val = minleaf.val
                root.right = self.deleteNode(root.right, minleaf.val)
        return root

        