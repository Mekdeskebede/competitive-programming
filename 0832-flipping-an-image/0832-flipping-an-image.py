class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row] = image[row][::-1]
            for i in range(len(image[row])):
                if image[row][i] == 1:
                    image[row][i] = 0
                else:
                    image[row][i] = 1
                    
        return image
                    
        