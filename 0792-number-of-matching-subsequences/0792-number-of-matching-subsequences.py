class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hash_map = defaultdict(list)
        for word in words:
            hash_map[word[0]].append(word)
        
        count = 0
        for i in range(len(s)):

            if hash_map[s[i]]:
                temp = hash_map[s[i]]
                hash_map[s[i]] = []
                for child in temp:
                    if len(child) == 1:
                        count += 1
                    else:
                        hash_map[child[1]].append(child[1:])
        return count
            