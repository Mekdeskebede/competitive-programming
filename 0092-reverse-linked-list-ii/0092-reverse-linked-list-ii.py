# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        
        if right == left:
            return head
        
        loop = right-left
        left_head = dummy
        
        while left-1:
            left_head = left_head.next
            left -= 1
            
        right_head = dummy
        
        while right + 1:
            right_head = right_head.next
            right -= 1
        
        prev = right_head
        curr = left_head.next
        left_head.next = None
        
        for i in range(loop+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left_head.next = prev
        
        return dummy.next
            
        
        
        
        
        