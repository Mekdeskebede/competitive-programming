class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        n = len(word1)
        m = len(word2)
        merge = ""
        
        while ptr1 < n and ptr2 < m:
            
            if word1[ptr1] > word2[ptr2]:
                merge += word1[ptr1]
                ptr1 += 1
            elif word1[ptr1] < word2[ptr2]:
                merge += word2[ptr2]
                ptr2 += 1
            else:
                if word1[ptr1:] > word2[ptr2:]:
                    merge += word1[ptr1]
                    ptr1 += 1
                else:
                    merge += word2[ptr2]
                    ptr2 += 1
                    
        merge += word1[ptr1:]
        merge += word2[ptr2:]
        
        return merge
                        