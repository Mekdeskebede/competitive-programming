# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = ListNode()
        crr = merged
        
        if  list2 == None:
            return list1
        elif  list1 == None:
            return list2
        
        while list1 and list2:
            if list1.val < list2.val:
                crr.next = list1
                list1 = list1.next
            else:
                crr.next = list2
                list2 = list2.next
                
            crr = crr.next
            
        if list1: 
            crr.next = list1
            
        elif list2: 
            crr.next = list2
            
        return merged.next
            
                
            
            