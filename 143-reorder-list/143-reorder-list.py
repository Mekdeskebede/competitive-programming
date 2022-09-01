# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev2 =  slow.next 
        slow.next = None
        prev = None 
        while prev2:
            temp = prev2.next
           
            prev2.next = prev
            prev = prev2
            prev2 = temp
        
        head2,prev2 = head, prev
          
        
        while prev2:
            
            temp = head2.next
            temp2 = prev2.next
            head2.next = prev2
            prev2.next = temp
            head2 = temp
            prev2 = temp2
       
        
        