# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxL = 0
        level = 0
        def dfs(cur, level):
            if not cur:
                return self.maxL
            level += 1
            self.maxL = max(self.maxL, level)
            dfs(cur.left, level)
            dfs(cur.right, level)
            return self.maxL
        res = dfs(root, level)
        return res
