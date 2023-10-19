# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        
        while l1:
            list1.append(l1.val)
            l1 = l1.next
            
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        i = len(list1)-1
        j = len(list2)-1
        ans = []
        while i > -1 and j > -1:
            curr = carry + list1[i] + list2[j]
            if curr < 0:
                ans.append(curr)
                carry = 0
            else:
                ans.append(curr%10)
                carry = curr//10
            j-=1
            i-=1
            
        while j >= 0:
            curr = carry + list2[j]
            if curr < 0:
                ans.append(curr)
                carry = 0
            else:
                ans.append(curr%10)
                carry = curr//10
            j -= 1
            
        while i >= 0:
            curr = carry + list1[i]
            if curr < 0:
                ans.append(curr)
                carry = 0
            else:
                ans.append(curr%10)
                carry = curr//10
            i -= 1
        if carry:
            ans.append(carry)
            
        list_ans = ListNode
        tail = list_ans
        for i in range(len(ans)-1,-1,-1):
            tail.next = ListNode(ans[i])
            tail = tail.next 
        
        return list_ans.next
        
        