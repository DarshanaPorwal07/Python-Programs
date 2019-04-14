class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self,z):
        return self.breadth*self.length

a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
obj1=rectangle(0,0)
print("Area of rectangle:",obj.area(obj1))
