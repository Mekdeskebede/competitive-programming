class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1

        r = 0 
        count = 0
        while r < len(chars):
            l = r
            while r + 1 < len(chars) and chars[r] == chars[r+1]:
                r += 1
            num = r - l + 1
            if num > 1:
                chars[count] = chars[r]
                count += 1
                num_str = str(num)
                for n in range(len(num_str)):
                    chars[count] = num_str[n]
                    count += 1
            else:
                chars[count] = chars[r]
                count += 1
            r += 1
        return count
                