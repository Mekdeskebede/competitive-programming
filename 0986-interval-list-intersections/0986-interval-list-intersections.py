class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        j = 0
        
        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            
            if second_end >= first_start and first_end >= second_start:
                ans.append([max(first_start, second_start), min(first_end, second_end)])
            
            if second_end >= first_end:
                i += 1
            else:
                j += 1
        
        return ans