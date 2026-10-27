/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode ReverseList(ListNode head) {
        var current = head;
        ListNode result = null;
        while (current != null)
        {
        result = new ListNode
        {
            val = current.val,
            next = result,
        };
        current = current.next;
        }
        return result;
    }
}
