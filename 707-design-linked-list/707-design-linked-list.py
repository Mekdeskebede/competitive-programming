class MyLinkedList:

    def __init__(self):
        self.linkedList = []

    def get(self, index: int) -> int:
        
        if index >= len(self.linkedList):
            return -1
        else:
            
            return self.linkedList[index] 
             
    def addAtHead(self, val: int) -> None:
        if self.linkedList:
            self.linkedList.insert(0,val)
        else:
            self.linkedList.append(val)
        

    def addAtTail(self, val: int) -> None:
        self.linkedList.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.linkedList):
            return
        elif index == len(self.linkedList):
            self.linkedList.append(val)
            return
        self.linkedList.insert(index,val)
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= len(self.linkedList):
            return
        self.linkedList.pop(index)
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)