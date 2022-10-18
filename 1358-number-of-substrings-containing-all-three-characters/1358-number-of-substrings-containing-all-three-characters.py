class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        left = 0
        counter = {}
        res = 0
        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] += 1
            else:
                counter[s[right]] = 1
            while len(counter) == 3:
                res += len(s) - right
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
        return res
                
            # if len(counter) == 3:
            #     ans += len(s) - left