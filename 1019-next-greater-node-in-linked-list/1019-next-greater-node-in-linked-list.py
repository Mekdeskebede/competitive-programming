# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        given = []
        stack = []
        res = []
        
        
        while head:
            given.append(head.val)
            res.append(0)
            head = head.next
            
        for i in range(len(given)):
            
            while stack and stack[-1][1] < given[i]:
                indx, val = stack.pop()
                res[indx] = given[i]
                
            stack.append((i,given[i]))
        
        return res
#         while head:
#             second = head.next
#             temp = head.next
            
#             while temp  and temp.val <= head.val:
#                 temp = temp.next
                
#             if temp == None:
#                 stack.append(0)
#             else:
#                 stack.append(temp.val)
                
    
#             head = second
            
        return stack