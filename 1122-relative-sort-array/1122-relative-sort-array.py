class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        freq = Counter(arr1)
        res = []
        for i in arr2:
            if i in freq:
                for _ in range(freq[i]):
                    res.append(i)
                freq.pop(i)
        temp = []       
        for j in freq:
            for _ in range(freq[j]):
                temp.append(j)
        temp.sort()
        res += temp    
        return res