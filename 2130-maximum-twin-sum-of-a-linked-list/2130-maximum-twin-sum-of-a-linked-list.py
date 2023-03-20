# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        rev = slow
        prev = None
        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
            
        max_twin = 0
        while prev:
            max_twin = max(max_twin, prev.val+head.val)
            prev = prev.next
            head = head.next
        
        return max_twin
            