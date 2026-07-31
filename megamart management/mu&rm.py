users = {
    "admin":{
        "password": "123",
        "role": "admin"
        }
}
def add_user():
        username = input("enter user name-")
        password = input("enter your passsword-")
        role = input("enetr your role (manager/hr/admin/cashier)")
        
        users[username]={
            "password": password, 
            "role": role
        }
        
        print(" user is added succesfull")

def view_user():
    for username,details in users.items():
         print("password- ", details["password"])
         print("role-",details["role"])
         print("username-",username)

def delete_user():
    username = input("enter username to delete- ")
    
        
    if username in users:
            del users[username]
            print("user is delete succesfully")
    else:
            print("user not found")
            
            
def search_user():
    username = input("enter username- ")
    if username in users:
            print("username-",username)
            print("password-",users[username]["password"])
            print("role-",users[username]["role"])
    else:
            print("user not found")
            
def login_user():
    username = input("enter user name-")
    password = input("eneter pass-")
    if username in users and password==users[username]["password"]:
            print("-----LOGIN SUCCESFUL-----")
            print("welcome ", users[username]["role"])
            
            user_role =users[username]["role"]
            if user_role == "admin":
                print("Admin menu")
            elif user_role == "manager":
                print("manager menu")
            elif user_role == "cashier":
                print("cashier menu")
            elif user_role == "hr":
                print("hr menu")
            else:
                print("invalid role")
    
    
    
    
    
while True:
    print("\n-------user management----------\n")
    print("1. add user")
    print("2. view user")
    print("3. delete user")
    print("4. search user")
    print("5. login")
    print("6. exit")
    
    choice = input("enetr choice  ")
    
    if choice =="1":
        add_user()
        
    
    elif choice == "2":
        view_user()
        
    
    elif choice == "3":
        delete_user()
        
    
    elif choice =="4":
        search_user()
         
            
    elif choice == "5":
        login_user()
        
            
    elif choice == "6":
        print("program closed")
        
        break
        
    
        
    
          
        
                     
    
            
            
        
        
