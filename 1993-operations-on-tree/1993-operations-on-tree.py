class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = defaultdict(int)
        self.adj_list = defaultdict(list)
        for i in range(len(parent)):
            self.adj_list[parent[i]].append(i)
        self.depth = len(parent)
        
    def lock(self, num: int, user: int) -> bool:
        if num in self.locked or num > self.depth:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            del self.locked[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        node = num
        while node != -1:
            if node in self.locked:
                return False
            node = self.parent[node]
            
        stack = deque([num])
        lockedDecendant = False
        while stack:
            node = stack.popleft()
            for child  in self.adj_list[node]:
                stack.append(child)
                if child in self.locked:
                    lockedDecendant = True
                    del self.locked[child]
                    
        if lockedDecendant:
            self.locked[num] = user
            return True 
        return False
        
            
            
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)