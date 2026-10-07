# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 0
        while(head):
            nextNode = head.next # 1
            head.next = prev # None
            prev = head # 0
            head = nextNode # 1
        return prev
