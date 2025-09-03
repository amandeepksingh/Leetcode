# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(l,r):
            if l == None and r == None:
                return True
            if l and r and l.val == r.val:
                return compare(l.right, r.left) and compare(l.left, r.right) 
            else:
                return False
            
        # check if root.left and root.right trees are same 
        l = root.left
        r = root.right 
        if root == None:
            return True 
        return compare(l,r)