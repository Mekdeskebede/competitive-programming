class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set()
        ans = set()
        
        for left in range(len(s)-9):
            dna = s[left:left + 10]
            if dna in visited:
                ans.add(dna)
            visited.add(dna)
        return list(ans)