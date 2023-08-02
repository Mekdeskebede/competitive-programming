# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedList = ListNode()
        dummy = sortedList
        newList = []
        for lis in lists:
            temp = []
            while lis:
                temp.append(lis.val)
                lis = lis.next
            newList.append(temp)
        heapq.heapify(newList)
        while newList:
            temp = heapq.heappop(newList)
            print(temp)
            if temp:
                minimum = heapq.heappop(temp)
                dummy.next = ListNode(minimum) 
                dummy = dummy.next
                if temp:
                    heapq.heappush(newList,temp)
        return sortedList.next