# class TreeNode:
#     def __init__(left=None,right=None,val=0):
#         self.left = left
#         self.right = right
#         self.val = val

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx =0
        def dfs(root: TreeNode) -> int:
            if not root: return 0
            left_h = dfs(root.left)
            right_h = dfs(root.right)
            self.maxx = max(self.maxx,left_h+right_h)
            return 1 + max(left_h, right_h)
        dfs(root)
        return self.maxx