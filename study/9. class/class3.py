#%% inheritance test 2

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
        
    def enginestart(self) :
        print(self.brand + "열쇠로 시동 킴")
        
    def enginestop(self) :
        print(self.brand + "열쇠로 시동 끔")


class SuperCar(Car) :
    def __init__(self, brand, color, price, mode) :
        super().__init__(brand, color, price)
        self.mode = mode
        
    #Overriding
    def enginestart(self) :
        print(self.brand + "음성으로 시동 킴")
         
    def openRoof(self) :
        print("지붕 열림")
        
    def closeRoof(self) :
        print("지붕 닫기")
        
ferrari = SuperCar("ferrari", "red", 35000, "daily") 
ferrari.enginestart()
ferrari.enginestop()
ferrari.openRoof()

#%% class variable

class A :
    seq = 0
    
    def __init__ (self) :
        A.seq += 1
        self.num = A.seq
        
    def test(self) :
        self.seq = 10
        
obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()

obj1.test()
print(obj1.num)
print(obj1.seq)
print(obj2.num)
print(obj3.num)