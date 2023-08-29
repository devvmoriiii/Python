#%% class test 1

class A:
    data = 10
    
    def printData(self) : 
        print(self)
        print(self.data)
    
    def intro() :
        print("A클래스")
        

obj1 = A()
obj2 = A()

obj1.data = 20
print(obj1)
obj1.printData()
print(obj2)
obj2.printData()

A.intro()

#%% class test 

class Car:
    # 여러 메소드에서 공유할 변수 선언
    brand = ""
    color = ""
    price = 0
    
    # 생성자는 외부에서 전달받은 값으로
    # 해당 필드의 객체에 알맞게 초기화하는 목적이 있다
    def __init__(self, brand="", color="", price=0) :
        # 해당 필드의 객체에 전달받은 값들을 각각 초기화한다.
        self.brand = brand
        self.color = color
        self.price = price
    
    def engineStart(self) :
        print(self.brand + "시동 킴")
        
    def engineStop(self) :
        print(self.brand + "시동 끔")
        
momcar = Car("Benz", "yellow", 35000)
daddycar = Car("BMW", "BLue", 15000)
mycar = Car()

# momcar.brand = "Benz"
# momcar.color = "Yellow"
# momcar.price = 350000

momcar.engineStart()  
daddycar.engineStop()  

    