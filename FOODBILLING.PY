#FOOD BILL
class FoodBilling:

    def __init__(self):
        self.menu = {
            1: ("Pizza", 250),
            2: ("Burger", 100),
            3: ("Chilli", 150),
            4: ("Noodle", 280),
            5: ("Momos", 120),
            6: ("Chaap", 300)
        }
        self.order = {}
        self.total = 0

    def show(self):
        print("\n------ Menu ------")
        for key, value in self.menu.items():
            print(key, value[0], "-", value[1])

    def take_order(self):
        while True:
            item = int(input("Enter Your Order (0 to stop): "))
            if item == 0:
                break
            if item in self.menu:
                qnt = int(input("Enter your Quantity: "))
                self.order[item] = self.order.get(item, 0) + qnt
            else:
                print("Invalid Item")

    def generate_bill(self, name, phone):
        print("\n=========== Your Bill ===========")
        print("Customer Name:", name)
        print("Phone No:", phone)
        print("--------------------------------")
        print("Item\tPrice\tQty\tAmount")

        for item, qnt in self.order.items():
            item_name, price = self.menu[item]
            amount = price * qnt
            self.total += amount
            print(f"{item_name}\t{price}\t{qnt}\t{amount}")

        dis = 0
        if self.total > 1000:
            dis = self.total * 0.10

        gst = (self.total - dis) * 0.05
        final_bill = self.total - dis + gst

        print("\n--------------------------------")
        print("Your Total bill is:", self.total)
        print("Discount (10%):", dis)
        print("GST (5%):", gst)
        print("Your Final bill is:", final_bill)


 
fb = FoodBilling()

name = input("Enter Customer Name: ")
phone = input("Enter Phone Number: ")

fb.show()
fb.take_order()
fb.generate_bill(name, phone)