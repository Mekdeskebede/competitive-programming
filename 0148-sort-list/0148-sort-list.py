# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getMid(head):
            slow , fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left_list, right_list):
            new_list = ListNode()
            dummy = new_list
            while left_list and right_list:
                if left_list.val < right_list.val:
                    dummy.next = ListNode(left_list.val)
                    left_list = left_list.next
                else:
                    dummy.next = ListNode(right_list.val)
                    right_list = right_list.next
                dummy = dummy.next
                    
            if left_list:      
                dummy.next = left_list
            if right_list:
                dummy.next = right_list
            return new_list.next
        
        def mergeSort(head):
    
            if not head or not head.next:
                return head
    
            left = head
            mid = getMid(head)
            right = mid.next
            mid.next = None

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)
        
        return mergeSort(head)

            
        
                    