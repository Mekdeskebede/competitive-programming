class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = []
        self.size = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if self.isFull():
            return False
        else:
            self.queue.insert(0,value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue.pop()
            return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.queue)== 0:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.queue)==self.size:
            return True
        else:
            return False
        
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()