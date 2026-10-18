# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # left -> right -> current
        def dfs(res,root: Optional[TreeNode]):
            if root is not None:
                dfs(res,root.left)
                dfs(res,root.right)
                res.append(root.val)
        dfs(res,root)
        return res