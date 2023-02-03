# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        large = ListNode()
        small = ListNode()
        
        less = small
        greater = large
        
        while head:
            
            if head.val >= x:
                large.next = head
                large = large.next
                
            else:
                small.next = head
                small = small.next
                
            head = head.next
            
        large.next = None
        small.next = greater.next

        return less.next
        