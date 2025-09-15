# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav = []
        self.helper(root, trav)
        return trav
    def helper(self, root, trav):
        if root: 
            self.helper(root.left, trav)
            self.helper(root.right, trav)
            trav.append(root.val)
        