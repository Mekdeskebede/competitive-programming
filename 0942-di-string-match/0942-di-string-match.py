class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        st = 0
        e = len(s)
        perm = [i for i in range(0,len(s)+1)]
        
        
        for ch in s:
            if ch == "I":
                res.append(perm[st])
                st += 1
            else:
                res.append(perm[e])
                e -= 1
        res.append(perm[st])
        return res
                