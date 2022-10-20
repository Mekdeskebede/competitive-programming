class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in blocks[:k]:
            if i == "W":
                count += 1
        res = count
        l = 0
        for r in range(k, len(blocks)):
            if blocks[l] == "W":
                count -= 1
            if blocks[r] == "W":
                count += 1
            res = min(res,count)
            l += 1
        return res
            
            
        