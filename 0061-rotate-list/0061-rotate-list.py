# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k== 0:
            return head
        length = 0
        curr = head
        prev = None
        
        while curr:
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            length += 1

        if length == 0 or k==0:
            return head
        
        k = k%length
        second = k
        first = second
        rotate = ListNode(0,prev)
        curr = prev 
        
        while second:
            curr = curr.next
            second -= 1
            
            
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left = prev
        curr = rotate.next
        
        while curr and first:
            temp = curr.next
            curr.next = left
            left = curr
            curr = temp
            first -= 1
        
        return left
    
            
            
            
        
            
            
            