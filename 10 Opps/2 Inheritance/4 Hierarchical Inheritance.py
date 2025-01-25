class Animal:  
    def speak(self):  
        print("Animal Speaking")  

class Dog(Animal):  
    def bark(self):  
        print("dog barking")   

class Tiger(Animal):
    def eating(self):
        print("Eating Mass")

a = Dog()
b = Tiger()

a.speak()
a.bark()
b.speak()
b.eating()

#               --------------A-------------  
#              !              !             !   
#              !              !             !
#              !              !             !
#              !              !             !
#              !              !             !
#              B              C             D
#                  Hierachical Inheritance   
          
