class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        for i in range(m):
            for j in range(n-1,-1,-1):
                if box[i][j]== ".":
                    space = j - 1
                    while space >= 0 and box[i][space] == ".":
                        space -= 1
                    if space >=0  and box[i][space] == "#":
                        box[i][space] = "."
                        box[i][j] = "#"
                    
        return zip(*box[::-1])
                    