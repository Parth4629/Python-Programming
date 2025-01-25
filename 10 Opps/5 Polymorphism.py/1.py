class xyz():  
    def websites(self):  
        print("Javatpoint is a website out of many availabe on net.")  
  
    def topic(self):  
        print("Python is out of many topics about technology on Javatpoint.")  
  
    def type(self):  
        print("Javatpoint is an developed website.")  
  
class PQR():  
    def websites(self):  
        print("Pinkvilla is a website out of many availabe on net. .")  
  
    def topic(self):  
        print("Celebrities is out of many topics.")  
  
    def type(self):  
        print("pinkvilla is a developing website.")  
        
P = xyz()  
Q = PQR()  
for domain in (P,Q):  
    domain.websites()  
    domain.topic()  
    domain.type()  