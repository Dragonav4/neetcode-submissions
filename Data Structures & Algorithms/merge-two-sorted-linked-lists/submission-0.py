# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        while(head1 is not None and head2 is not None):

            if(head1.val < head2.val):
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        if(head1 is not None):
            current.next = head1
        else:
            current.next = head2
        return dummy.next


            
