# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4] Two pointers approach(fast and slow)

        dummy = ListNode()
        
        if(n == 1 and head.next is None):
            head = None
            return head
        dummy.next = head
        left = dummy
        right = dummy
                    #l   r
        while(n >0 and right is not None): #1,2,3,4,5
            right = right.next
            n-=1
        # left = left.next       #    l   r
        while(right.next is not None):
            right = right.next #1,2,3,4,5
            left = left.next
        if(right.next is None):
            left.next = left.next.next
        return dummy.next


            


        