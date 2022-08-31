# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
       
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
             
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
            
        
        
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
            
#         left = None
        
#         while slow:
#             temp = slow.next
#             slow.next = left
#             left = slow 
#             slow = temp
            