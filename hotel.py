
# HOTEL MANAGEMENT SYSTEM


rooms = {}

while True:

    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Add Room")
    print("2. View All Rooms")
    print("3. Book Room")
    print("4. Search Room")
    print("5. Checkout Room")
    print("6. Delete Room")
    print("7. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        room_no = int(input("Enter Room Number: "))

        if room_no in rooms:
            print("Room already exists!")

        else:
            customer_name = input("Enter Customer Name: ")
            room_type = input("Enter Room Type (AC/Non-AC): ")
            rent = float(input("Enter Room Rent: "))
            status = "Booked"

            rooms[room_no] = {
                "customer_name": customer_name,
                "room_type": room_type,
                "rent": rent,
                "status": status
            }

            print("Room Added Successfully!")

    elif choice == "2":

        if not rooms:
            print("No room records found!")

        else:
            print("\n===== ROOM DETAILS =====")

            for room_no, details in rooms.items():

                print(f"""
Room Number   : {room_no}
Customer Name : {details['customer_name']}
Room Type     : {details['room_type']}
Rent          : ₹{details['rent']}
Status        : {details['status']}
""")


    elif choice == "3":

        room_no = int(input("Enter Room Number to Book: "))

        if room_no in rooms:

            if rooms[room_no]["status"] == "Available":

                customer_name = input("Enter Customer Name: ")

                rooms[room_no]["customer_name"] = customer_name
                rooms[room_no]["status"] = "Booked"

                print("Room Booked Successfully!")

            else:
                print("Room already booked!")

        else:
            print("Room not found!")

    
    elif choice == "4":

        room_no = int(input("Enter Room Number to Search: "))

        if room_no in rooms:

            details = rooms[room_no]

            print("\n===== ROOM FOUND =====")
            print("Customer Name :", details["customer_name"])
            print("Room Type     :", details["room_type"])
            print("Rent          : ₹", details["rent"])
            print("Status        :", details["status"])

        else:
            print("Room not found!")

    
    elif choice == "5":

        room_no = int(input("Enter Room Number to Checkout: "))

        if room_no in rooms:

            rooms[room_no]["customer_name"] = "None"
            rooms[room_no]["status"] = "Available"

            print("Checkout Successful!")

        else:
        