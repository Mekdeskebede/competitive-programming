# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        
        intercept = None
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                intercept = fast
                slow = head

                while slow:
                    if slow == intercept:
                        return slow
                    slow = slow.next
                    intercept = intercept.next
                                            
        return
