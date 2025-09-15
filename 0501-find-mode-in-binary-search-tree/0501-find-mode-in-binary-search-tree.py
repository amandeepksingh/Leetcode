# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = dict()
        # my_dict = {'a': 10, 'b': 30, 'c': 20}
        self.dfs(root, freq)
        # Find the maximum value
        max_value = max(freq.values())

        # Collect all keys with that maximum value
        max_keys = [key for key, value in freq.items() if value == max_value]
        return max_keys
        
    def dfs(self, root, freq):
        if not root:
            return 
        if root:
            freq[root.val] = freq.get(root.val, 0) + 1
        self.dfs(root.left, freq)
        self.dfs(root.right, freq)
        