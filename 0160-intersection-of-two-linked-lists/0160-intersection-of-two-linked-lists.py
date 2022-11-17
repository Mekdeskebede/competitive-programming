# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashSet = set()
        tempA = headA
        while tempA:
            hashSet.add(tempA)
            tempA = tempA.next
        tempB = headB
        while tempB:
            if tempB in hashSet:
                return tempB
            tempB = tempB.next
        return 
