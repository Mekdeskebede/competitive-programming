# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
            
        left = head
        right = head.next
        prev = None
        
        while left and left.next:
            
            if left.val == left.next.val:
                while left and left.next and left.val == left.next.val:
                    left = left.next
                if prev:
                    prev.next = left.next
                    left = left.next
                   
                else:
                    head = left.next
                    left = left.next
                   
            else:
                prev = left
                left = left.next
              
        return head 
            
              
                
            