# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # REMAKE
        if not root: return True
        low,high = float('-inf'),float('inf')
        q = deque([(root,low,high)])
        while q:
            node,low,high = q.popleft() 
            if not low < node.val < high: return False
            if low < node.val < high:
                if node.left is not None:
                    q.append((node.left,low,node.val)) # 1 
                if node.right is not None:
                    q.append((node.right,node.val,high)) # 3
        return True
            
            
            