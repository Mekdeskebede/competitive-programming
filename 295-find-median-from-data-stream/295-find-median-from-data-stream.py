class MedianFinder:

    def __init__(self):
        
        self.list = []

    def addNum(self, num: int) -> None:
        self.list.append(num)

    def findMedian(self) -> float:
        self.list.sort()
        n = len(self.list)
        if n and n%2 == 0:
            return (self.list[(n//2)-1 ] + self.list[(n//2)]) /2
        else:
            return self.list[(n//2)]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()