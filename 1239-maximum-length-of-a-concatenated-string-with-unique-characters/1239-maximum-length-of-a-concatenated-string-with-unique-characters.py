class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def unique(subseq):
            return len(subseq) == len(set(subseq))
        def backtrack(start, current_subseq):
            nonlocal max_length
            if unique(current_subseq):
                max_length = max(max_length, len(current_subseq))
            for i in range(start, len(arr)):
                backtrack(i + 1, current_subseq + arr[i])
        max_length = 0
        backtrack(0, "")
        return max_length