# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # approach one
        
#         curr = head
#         length = 0
        
#         while curr:
#             curr = curr.next 
#             length += 1
            
#         mid = length//2
#         curr = head
        
#         while mid:
#             curr = curr.next
#             mid -= 1
        
#         return curr
    
#     approach two

        
#         curr = head
#         arr = []
        
#         while curr:
#             arr.append(curr)
#             curr = curr.next 
            
#         return arr[len(arr)//2]
    
#     approach 3

        fast = head
        slow = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
        return slow
            

        

        