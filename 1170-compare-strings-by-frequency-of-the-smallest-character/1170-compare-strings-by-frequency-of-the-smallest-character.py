class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def countFrequency(string):
            string = list(string)
            string.sort()
            small = 0
            for i in range(len(string)):
                if string[i] != string[0]:
                    break
                else:
                    small += 1
            return small
        
        for i in range(len(queries)):
            queries[i] = countFrequency(queries[i])
        
        for i in range(len(words)):
            words[i] = countFrequency(words[i])
            
        words.sort()
        n = len(words)
        ans = []
        
        for query in queries:
            
            low = 0
            high = n - 1
            
            while low <= high:
                mid = low + (high-low)//2
                if words[mid] < query+1:
                    low = mid + 1
                else:
                    high = mid - 1
            
            ans.append(n-low)
        
        return ans