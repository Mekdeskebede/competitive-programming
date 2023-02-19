# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        
        while curr:
            
            if prev and prev.val == curr.val:
                prev.next = curr.next
                
            else:
                temp = curr
                prev = temp
                
            curr = curr.next
            
        return head