class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        hashMap = defaultdict(int)
        if A[0] == B[0]:
            ans.append(1)
        else:
            ans.append(0)
        hashMap[A[0]] = 1
        hashMap[B[0]] = 1
        for i in range(1,len(A)):
            hashMap[A[i]] = 1
            hashMap[B[i]] = 1
            ans.append((i+1)*2 - len(hashMap)) 
        return ans