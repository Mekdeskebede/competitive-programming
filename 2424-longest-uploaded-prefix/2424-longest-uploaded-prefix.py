class LUPrefix:

    def __init__(self, n: int) -> None:
        
        self.pre= list(range(n, -1, -1))
        self.uploads = set()

        
    def upload(self, video: int) -> None:
        
        self.uploads.add(video - 1)
		
        while self.pre[-1] in self.uploads:
            self.pre.pop()
        
    def longest(self) -> int:
        
        return self.pre[-1]
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()