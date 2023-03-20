# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        final = ListNode()
        curr = final
        carry = 0
        
        while l1 or l2:
            if not l1:
                add = carry + l2.val
                l2 = l2.next
            elif not l2:
                add = carry + l1.val
                l1 = l1.next
            else:
                add = carry + l2.val + l1.val
                l1=l1.next 
                l2 = l2.next
            
            curr.next = ListNode(add%10)
            carry = add//10
            curr = curr.next
            
        if carry:
            curr.next = ListNode(carry)
            
        return final.next
        