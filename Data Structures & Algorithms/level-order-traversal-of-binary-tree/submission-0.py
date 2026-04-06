# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                value = q.popleft()
                if value:
                    q.append(value.left)
                    q.append(value.right)
                    level.append(value.val)
            
            if level:
                res.append(level)
        return res
            
            
