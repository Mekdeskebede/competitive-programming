# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        added = ListNode()
        tail = added
        
        carry = 0
        while l1 or l2 or carry:
            
            if not l1:
                value1 = 0
            else:
                value1 = l1.val
            if not l2:
                value2 = 0
            else:
                value2 = l2.val
                
            add = value1 + value2 + carry
            
            carry = add//10
            
            tail.next = ListNode(add%10)
            
            tail = tail.next
            if l2:
                l2 = l2.next
            else:
                l2 = None
            if l1:
                l1 = l1.next
            else:
                l1 = None
            
        return added.next
            
            
            