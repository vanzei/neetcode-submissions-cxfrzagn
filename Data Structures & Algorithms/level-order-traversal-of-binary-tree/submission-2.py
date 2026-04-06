# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])


        res = []

        while q:
            qlen = len(q)

            level = []
            for i in range(qlen):
                value = q.popleft()
                if value:
                    level.append(value.val)
                    q.append(value.left)
                    q.append(value.right)
                    
            if level:
                res.append(level)
        return res
            
