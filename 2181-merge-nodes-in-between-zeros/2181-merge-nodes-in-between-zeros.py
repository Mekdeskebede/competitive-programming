# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = head
        curr = head
        curr = curr.next
        sum = 0
        while curr:
            if curr.val == 0:
                new = new.next
                new.val = sum
                sum = 0
            else:
                sum += curr.val
            curr = curr.next
        new.next = None
        return head.next
            