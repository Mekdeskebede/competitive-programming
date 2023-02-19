# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        oddHead = ListNode()
        evenHead  = ListNode()
        odd= oddHead
        even = evenHead
        indice = 0
        
        while head:
            
            if indice % 2 != 0:
                even.next = ListNode(head.val,None)
                even = even.next
                
            else:
                odd.next = ListNode(head.val,None)
                odd = odd.next
                
            head = head.next
            indice += 1
            
        odd.next = evenHead.next
        
        return oddHead.next
            
            
            