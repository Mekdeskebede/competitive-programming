# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(-5001)
        while head:
            temp = new
            prev = new
            while temp and temp.val < head.val:
                prev = temp
                temp = temp.next
            prev.next = ListNode(head.val,temp)
            head = head.next
        return new.next
            