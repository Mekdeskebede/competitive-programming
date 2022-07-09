class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        frequency = defaultdict(int)
    
    
        for i in nums:
            frequency[i] +=1

        value_list= list(frequency.values())
        value_list.sort()
        value_list.reverse()
        final=[]
        for i in value_list[:k]:
            for keys, values in frequency.items():
                if  values==i:
                    final.append(keys)
                    del frequency[keys]
                    break

        return final
            
            