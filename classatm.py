#bank atm account
class BANKACCOUNT:
    def __init__(self, name, bal, username, password, pin):
        self.name = name
        self.bal = bal
        self.username = username
        self.password = password
        self.pin = pin

    def login(self):
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == self.username and pwd == self.password:
            print("Login successful ")
            return True
        else:
            print("Invalid username or password ")
            return False

    def deposit(self, amount):
        user_pin = int(input("Enter PIN: "))
        if user_pin == self.pin:
            self.bal += amount
            print("Deposit:", amount)
        else:
            print("Wrong PIN ")

    def withdrawal(self, amount):
        user_pin = int(input("Enter PIN: "))
        if user_pin == self.pin:
            if amount <= self.bal:
                self.bal -= amount
                print("Withdraw:", amount)
            else:
                print("Insufficient balance ")
        else:
            print("Wrong PIN ")

    def display(self):
        user_pin = int(input("Enter PIN: "))
        if user_pin == self.pin:
            print("Balance:", self.bal)
        else:
            print("Wrong PIN ")


ba = BANKACCOUNT("lucifer", 5000, "lucky", "1234", 7722)


if ba.login():
    ba.deposit(2000)
    ba.withdrawal(1000)
    ba.display()