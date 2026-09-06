class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
            self.array[self.size] = n
            self.size += 1
        else :
            self.array[self.size] = n
            self.size += 1

    def popback(self) -> int:
        self.size -= 1
        # self.capacity -= 1
        # print("we poopped ", self.array[(len(self.array) - 1)])
        return self.array[self.size]
 

    def resize(self) -> None:
        self.capacity *= 2
        self.array += [0] * (self.capacity // 2)


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
