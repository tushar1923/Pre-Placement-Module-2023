# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Logic is, we use the concept of range of values of nodes in left and right sub-tree 
        # for left [-2**31<=root.data<root.data-1] , for right [root.data+1<root.data<=2**31]
        # if condition not satisfied return False

        
        def helper(root,mini,maxi):
            if root is None:
                return True
            if root.val<mini or root.val>maxi:
                return False
            left=helper(root.left,mini,root.val-1)
            right=helper(root.right,root.val+1,maxi)
            if not left or not right:
                return False
            return True
        
                
        return helper(root,-2**31,2**31)