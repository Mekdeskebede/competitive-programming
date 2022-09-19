# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = []
        temp = head
        while temp:
            newList.append(temp.val)
            temp = temp.next
            
        newList.sort()
        
        resList = ListNode()
        right  = resList
        for i in newList:
            right.next = ListNode(i)
            right = right.next
        return resList.next
        
        
        
#         sort = ListNode(0)
       
#         while head:
#             second = head.next
#             temp = sort
            
#             while temp.next and temp.next.val < head.val:
#                 temp = temp.next
                
#             head.next = temp.next
#             temp.next = head
#             head = second
            
#         return sort.next
             