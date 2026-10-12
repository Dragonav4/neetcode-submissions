# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4] Two pointers approach(fast and slow)

        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = dummy

        for i in range(n):
            right = right.next
        # left = left.next       #    l   r
        while(right.next is not None):
            right = right.next #1,2,3,4,5
            left = left.next
        left.next = left.next.next
        return dummy.next


            


        