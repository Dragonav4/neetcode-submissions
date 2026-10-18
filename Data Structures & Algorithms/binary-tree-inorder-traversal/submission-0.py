# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left -> current -> right
        res = []
        def dfs(res,root: Optional[TreeNode]):
            if root !=None:
                left = dfs(res,root.left)
                res.append(root.val)
                right = dfs(res,root.right)
            return res
        dfs(res,root)
        return res