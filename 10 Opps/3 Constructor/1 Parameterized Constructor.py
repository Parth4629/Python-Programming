class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
p1 = Employee("John", 101)  
p2 = Employee("David", 102)  
   
  
p1.display()  
  
p2.display() 