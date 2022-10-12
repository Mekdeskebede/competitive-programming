class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        letter = defaultdict()
        for idx, val in enumerate(s):
            letter[val] = idx
        
        count = 0
        stop = 0
        res = []
        for i,char in enumerate(s):
            count += 1
            if letter[char] > stop:
                stop = letter[char]
            if stop == i:
                res.append(count)
                count = 0
        return res
                
            
            