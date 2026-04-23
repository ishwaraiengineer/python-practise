#EMPLOYMENT SYSYTM
class EmployeeManagement:

    def __init__(self):
        self.employees = {}

    # ---------- Employee Features ----------
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            print("Employee ID already exists\n")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        self.employees[emp_id] = {
            "name": name,
            "age": age,
            "department": dept,
            "salary": salary
        }

        print("Employee added successfully\n")

    def view_employees(self):
        if not self.employees:
            print("No employees found\n")
            return

        print("\n------ Employee List ------")
        for emp_id, emp in self.employees.items():
            print(f"ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}")
            print("--------------------------")

    def search_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print("\nEmployee Details")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}\n")
        else:
            print("Employee not found\n")

    def update_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            emp = self.employees[emp_id] 

            print("Leave blank to keep old value")

            name = input("New Name: ")
            age = input("New Age: ")
            dept = input("New Department: ")
            salary = input("New Salary: ")

            if name:
                emp["name"] = name
            if age:
                emp["age"] = int(age)
            if dept:
                emp["department"] = dept
            if salary:
                emp["salary"] = float(salary)

            print("Employee updated successfully\n")
        else:
            print("Employee not found\n")

    def delete_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully\n")
        else:
            print("Employee not found\n")

    # ---------- Extra Features ----------
    def salary_statistics(self):
        if not self.employees:
            print("No data available\n")
            return

        salaries = [emp["salary"] for emp in self.employees.values()]

        print("Total Employees:", len(salaries))
        print("Average Salary:", sum(salaries) / len(salaries))
        print("Highest Salary:", max(salaries))
        print("Lowest Salary:", min(salaries))
        print()


# ---------- Login System ----------
def login():
    USERNAME = "admin"
    PASSWORD = "1234"

    attempts = 3

    while attempts > 0:
        user = input("Enter Username: ")
        pwd = input("Enter Password: ")

        if user == USERNAME and pwd == PASSWORD:
            print("\nLogin Successful\n")
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}\n")

    print("Too many failed attempts. Exiting program.")
    return False


# ---------- Main Program ----------
if login():

    ems = EmployeeManagement()

    while True:
        print("====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Salary Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ems.add_employee()
        elif choice == "2":
            ems.view_employees()
        elif choice == "3":
            ems.search_employee()
        elif choice == "4":
            ems.update_employee()
        elif choice == "5":
            ems.delete_employee()
        elif choice == "6":
            ems.salary_statistics()
        elif choice == "7":
            print("Exiting program")
            break
        else:
            print("Invalid choice\n")