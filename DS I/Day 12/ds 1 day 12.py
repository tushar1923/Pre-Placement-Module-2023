# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left and not root.right:
            return root
        
        left_branch = self.invertTree(root.left) if root.left else None
        right_branch = self.invertTree(root.right) if root.right else None
        
        root.left = right_branch
        root.right = left_branch
        
        return root