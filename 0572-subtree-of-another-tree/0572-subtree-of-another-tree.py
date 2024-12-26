# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot == None:
            return True
        if root == None:
            return False 
        if self.compare(root,subRoot):
            return True
        # go deeper 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def compare(self, curr_1, curr_2):
        if curr_1 == None and curr_2 == None:
            return True 
        if curr_1 and curr_2 and curr_1.val == curr_2.val:
            return self.compare(curr_1.right, curr_2.right) and self.compare(curr_1.left, curr_2.left)
        return False 
        
        