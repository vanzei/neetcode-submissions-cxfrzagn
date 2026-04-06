# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.same(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def same(self, ref, comp):

        if not ref and not comp:
            return True
        
        if ref and comp and ref.val == comp.val:
            return (self.same(ref.left, comp.left) and self.same(ref.right, comp.right))
    
        return False