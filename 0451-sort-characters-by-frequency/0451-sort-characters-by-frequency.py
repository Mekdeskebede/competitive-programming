class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = sorted(count.items(), key= lambda x:x[1],reverse = True)
        print(count)
        
        ans = ''
        for val,cnt in count:
            ans += val * cnt
        return ans 