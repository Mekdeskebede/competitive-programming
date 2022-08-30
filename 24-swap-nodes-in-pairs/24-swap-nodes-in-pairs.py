# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next):
            return head
        
        tail = ListNode(0,head)
        curr = tail
        
        while curr.next and curr.next.next:
            
            # if count%2:
            temp1 = curr.next
            temp2 = curr.next.next
            temp1.next = temp2.next
            
            curr.next = temp2
            curr.next.next = temp1
            
            curr = curr.next.next
            
            
        return tail.next
                
                
            