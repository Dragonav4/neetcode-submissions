# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root == None): return None
        q = deque()

        q.append(root)
        while(q):
            temp = q[0].left
            q[0].left = q[0].right
            q[0].right = temp
            currentNode = q.popleft()
            if(currentNode.left != None):
                q.append(currentNode.left)
            if(currentNode.right != None):
                q.append(currentNode.right)
        return root