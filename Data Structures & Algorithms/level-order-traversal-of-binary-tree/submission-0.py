# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque([root])
        r = []
        while q:
            level = [] 
            l = len(q) # 2
            
            while l !=0:
                node = q.popleft() # 2 3 
                if node.left is not None:
                    q.append(node.left) # 4 
                if node.right is not None:
                    q.append(node.right) # 5
                level.append(node.val) # 2
                l-=1
            r.append(level)
        return r


