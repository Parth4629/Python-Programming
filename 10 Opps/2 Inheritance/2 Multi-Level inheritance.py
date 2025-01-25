class Animal:  
    def speak(self):  
        print("Animal Speaking")  

class Dog(Animal):  
    def bark(self):  
        print("dog barking")  

class Cat(Dog):  
    def eat(self):  
        print("Cat barking") 

class Tiger(Cat):
    def eating(self):
        print("Eating Mass")

d = Tiger()
d.speak() 
d.bark()   
d.eat()
d.eating()


#        Base Class     A
#                       !
#                       !
#                       !
#     intermediatory    B
#          Class        !
#                       !
#                       !
#      Drived Class     C
#                       
#              Multi-leval inheritance
