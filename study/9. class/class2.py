#%% inheritance test

class A:
    def __init__(self, data = 10) :
        self.data = data
        print("부모 생성자 호출")
        
    def printData(self) :
        print(self.data)
        
    def show(self) :
        print("부모 메소드")
        
    
class B(A) :
    def __init__(self, data, data2) :
        # A.__init__(self, data)
        super().__init__(data)
        # self.data = data
        self.data2 = data2
 
    # Overriding 
    def printData(self) :
        print(self.data, self.data2)
 
    # def printData2(self) :
    #     print(self.data, self.data2)

b = B(30, 20)
b.printData()
        