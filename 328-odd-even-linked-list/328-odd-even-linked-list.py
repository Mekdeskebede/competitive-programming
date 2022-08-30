# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
       
        
        if not head or not head.next or not head.next.next:
            return head
        
        curr_even = head.next
        curr_odd = head
        even_head = head.next
        
        while curr_even and curr_even.next:
            
            curr_odd.next = curr_even.next
            curr_odd = curr_odd.next
            curr_even.next = curr_odd.next
            curr_even = curr_even.next
            
            curr_odd.next = even_head
            
        return head
            