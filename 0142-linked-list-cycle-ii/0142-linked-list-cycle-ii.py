# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hash_set = set()
        
        while head:
            
            if head in hash_set:
                return head
            
            hash_set.add(head)
            head = head.next
            
        return 