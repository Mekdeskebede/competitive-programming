# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = ListNode()
        curr = merged
        
        #  recursive function to compare the lists
        def recur(curr,l1,l2):
            
        #  base cae:if one of the lists become empty
            if not l2:
                curr.next = l1
                return
            elif not l1:
                curr.next = l2
                return
            
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            return recur(curr.next,l1,l2)
        
        recur(curr,list1,list2)
        
        return merged.next
            
            
                
        