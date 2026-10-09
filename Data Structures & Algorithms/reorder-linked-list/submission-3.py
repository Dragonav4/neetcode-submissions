# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 4 6 8
        # 2 -> 8 -> 4 -> 6 // 1 change
        # 2 4 6 8 10
        # 2 -> 10 -> 4 -> 8 -> 6 //2 change //5
        #Solution:
        # l=0       r=len(n)
        #   2 ->    10 -> None
        # head.next = 
        current = head
        if not current:
            return

        #10
        #8
        #6
        #4
        #2        
        stack = []
        while current is not None:
            stack.append(current)
            current = current.next
        l=0
        r=len(stack)-1
        while(l < r):
            #0,1,2,3,4
            #2,4,6,8,10
            #4 -> 8 -> 6
            #l2= 6
            #r2= 6
            left = stack[l] # 2, l=1: # 4
            right = stack[r] # 10 r=3: # 8
            nextleft = left.next # 4 # 6
            left.next = right # 2 -> 10! # 8
            right.next = nextleft # 10 -> 4 # 6
            l+=1
            r-=1
        stack[l].next = None



