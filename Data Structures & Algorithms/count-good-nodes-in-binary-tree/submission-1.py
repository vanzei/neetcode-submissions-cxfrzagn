# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        curMax = root.val
        q = collections.deque()
        q.append([root, -float("inf")])

        while q:
            node, curMax = q.popleft()
            
            if node.val >= curMax:
                res += 1
            if node.left:
                q.append([node.left, max(curMax, node.val)])
            if node.right:
                q.append([node.right, max(curMax, node.val)])

        return res

