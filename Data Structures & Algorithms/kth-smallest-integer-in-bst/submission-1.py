# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        res = self.DFS(stack,root)
        print(stack)
        node = 0
        if len(stack) == k: return stack.pop()

        return stack[k-1]
        
        #LIFO
        #2 # 4
        #1 # 3
        #3 # 2
        #- # 5

    def DFS(self,stack,root: Optional[TreeNode]) -> [int]:
        if root is not None:
            
            left = self.DFS(stack,root.left)
            stack.append(root.val)
            right = self.DFS(stack,root.right)
        return stack