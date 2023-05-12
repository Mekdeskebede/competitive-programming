class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        
    def addNum(self, num: int) -> None:
        
        if len(self.left) > len(self.right):
            large = -heapq.heappop(self.left)
            heapq.heappush(self.left,-min(large,num))
            heapq.heappush(self.right,max(large,num))
            
        elif len(self.left) < len(self.right):
            large = heapq.heappop(self.right)
            heapq.heappush(self.left,-min(large,num))
            heapq.heappush(self.right,max(large,num))
        else:
            if not self.left and not self.right:
                heapq.heappush(self.left, -num)
            elif self.left:
                large = -heapq.heappop(self.left)
                heapq.heappush(self.left,-min(large,num))
                heapq.heappush(self.right,max(large,num))
            elif self.right:
                large = heapq.heappop(self.right)
                heapq.heappush(self.left,-min(large,num))
                heapq.heappush(self.right,max(large,num))
                

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        elif len(self.left) < len(self.right):
            return float(self.right[0])
        else:
            return (self.right[0] + (-self.left[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()