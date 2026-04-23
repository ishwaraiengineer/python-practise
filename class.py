#__init__
class student:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print("i am :",self.name)
        
s1=student("python")
s1.show()