# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        ans = {}
        length = 0
        
        while head:
            
            while stack and stack[-1][1] < head.val:
                idx, val = stack.pop()
                ans[idx] = head.val
            stack.append([length,head.val])
            head = head.next
            length += 1
        
        res = [0] * length
       
        for key,val in ans.items():
            res[key] = val
        
        return res