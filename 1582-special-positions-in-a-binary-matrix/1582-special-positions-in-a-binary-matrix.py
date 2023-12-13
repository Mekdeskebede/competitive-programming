class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ones_rows = defaultdict(int)
        ones_cols = defaultdict(int)
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    ones_rows[row] += 1
                    ones_cols[col] += 1
        ans = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    if ones_rows[row] == 1 and ones_cols[col] == 1:
                        ans += 1
        return ans