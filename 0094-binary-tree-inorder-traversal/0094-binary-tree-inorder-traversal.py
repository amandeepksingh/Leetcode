# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav = []
        self.dfs(root, trav)
        return trav

    def dfs (self, r, trav): 
        if r is not None:
            self.dfs(r.left, trav)
            trav.append(r.val)
            self.dfs(r.right, trav)
        