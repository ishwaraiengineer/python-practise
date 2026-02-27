class student:
    def __init__(self,name):
        self.name = name 
    def show(self):
        print("this is my name",self.name)
        
obj=student("lucky")
obj.show()