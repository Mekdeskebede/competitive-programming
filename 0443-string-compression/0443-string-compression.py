class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        ans = []
        l = 0
        while l < len(chars):
            r = l + 1
            count = 1
            while r < len(chars) and chars[r] == chars[l]:
                r += 1
                count += 1
            ans.append(chars[l])
            if count != 1:
                for char in str(count):
                    ans.append(char)
            l = r
        for i in range(len(ans)):
            chars[i] = ans[i]

        return len(ans)