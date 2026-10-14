# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        if p.left == q or p.right == q:
            return p
        
        if q.left == p or q.right == p:
            return q

        def dfs(r, a, b):
            if r is None:
                return None
            
            if r.val < a.val and r.val < b.val:
                return dfs(r.right, a, b)
            
            if r.val > a.val and r.val > b.val:
                return dfs(r.left, a, b)

            return r
        
        return dfs(root, p, q)
        