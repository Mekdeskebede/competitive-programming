class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        prefix_1 = []
        prefix_2 = []
        ans = []
        for i in range(len(security)):
            if i == 0:
                prefix_1.append(0)
                prefix_2.append(0)
            else:
                if security[i-1] >= security[i]:
                    prefix_1.append(prefix_1[-1] + 1)
                else:
                    prefix_1.append(0)
                
                if security[-i-1] <= security[-i]:
                    prefix_2.append(prefix_2[-1] + 1)
                else:
                    prefix_2.append(0)
        print(prefix_1)
        prefix_2.reverse()
        print( prefix_2)
        
        for i in range(len(prefix_1)):
            if prefix_1[i] >= time and prefix_2[i] >= time:
                ans.append(i)
                
        return ans
                
            
