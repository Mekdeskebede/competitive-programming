class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.big = big
        self.medium = medium
        self.small = small
        
        self.big_slot = [] 
        self.medium_slot = [] 
        self.small_slot = [] 

    def addCar(self, carType: int) -> bool:
        if carType == 1 and len(self.big_slot) < self.big:
            self.big_slot.append(carType)
            return True
        elif carType == 2 and len(self.medium_slot) < self.medium:
            self.medium_slot.append(carType)
            return True
        elif carType == 3 and len(self.small_slot) < self.small:
            self.small_slot.append(carType)
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)