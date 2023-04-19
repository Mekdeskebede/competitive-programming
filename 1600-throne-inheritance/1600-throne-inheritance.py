class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inheritance = defaultdict(list)
        self.died = set()
        self.initial = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)

    def death(self, name: str) -> None:
        self.died.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.curr = []
        self.dfs(self.initial)
        return self.curr
    
        
    def dfs(self,node):
        if node not in self.died:
            self.curr.append(node)
        for neighbor in self.inheritance[node]:
            self.dfs(neighbor)
            
            
        
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()