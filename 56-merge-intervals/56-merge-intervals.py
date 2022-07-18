class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
       
        merged = []
        check = 0
        for first, second in intervals:
            if check == 0:
                merged.append([first,second])
                check += 1
                continue
            
            elif first <= merged[-1][1]:
                temp = merged[-1]
                
                merged[-1][1]= max(second,temp[1])
                check += 1

            else:
                merged.append([first,second])
                check += 1
                continue
                
           
        return merged