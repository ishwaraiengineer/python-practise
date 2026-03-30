class parents:
    def __init__(self,fathername,mothername,add,phone):
        self.fathername = fathername
        self.mothername = mothername
        self.add = add
        self.phone = phone
        
    def show(self):
        print("father name is:",self.fathername)
        print("mother name is:",self.mothername)
        print("phone number and add is:",self.add,self.phone)
        
obj = parents("krishan","usha","gamri","987867878")
obj.show()