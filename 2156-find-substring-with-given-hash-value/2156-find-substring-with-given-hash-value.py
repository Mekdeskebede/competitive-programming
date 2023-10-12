class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        curr_hash = 0
        powers = []
        n = len(s)
        for i in range(k):
            powers.append(pow(power, i, modulo))
        i = 0
        while i < k:
            curr_hash += (ord(s[n - k + i]) - 96) * powers[i]
            i += 1

        index = n - k
        for i in range(n-k-1, -1, -1):
            curr_hash -= (ord(s[i + k]) - 96) * powers[k-1]
            curr_hash = curr_hash * power + (ord(s[i]) - 96)
            curr_hash %= modulo
            if curr_hash % modulo == hashValue:
                index = i

        return s[index:index+k]
        