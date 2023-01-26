class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n = len(skill)
        skill.sort()
        
        left = 1
        right = n-2
        first = skill[0] + skill[n-1]
        chem = skill[0] * skill[n-1]
        
        while left < right:
            
            if skill[left] + skill[right] != first:
                return -1
            
            chem += (skill[left] * skill[right])
            
            left += 1
            right -= 1
            
        return chem
            
            