from tkinter import *
from tkinter import messagebox

# ----------------- Data Storage -----------------
accounts = {
    "1001": {"password": "1234", "name": "Khushi", "balance": 5000.0},
    "1002": {"password": "1111", "name": "Rahul", "balance": 8000.0}
}

transactions = []
current_account = ""


# ---------------- Create Account ----------------
def create_account():
    create_win = Toplevel(root)
    create_win.title("Create Account")
    create_win.geometry("400x450")
    create_win.configure(bg="#1f1f1f")

    Label(
        create_win,
        text="Create New Account",
        font=("Arial", 18, "bold"),
        bg="#1f1f1f",
        fg="cyan"
    ).pack(pady=15)

    Label(create_win, text="Account Number", bg="#1f1f1f", fg="white").pack()
    ac_entry = Entry(create_win, font=("Arial", 12))
    ac_entry.pack(pady=5)

    Label(create_win, text="Name", bg="#1f1f1f", fg="white").pack()
    name_entry = Entry(create_win, font=("Arial", 12))
    name_entry.pack(pady=5)

    Label(create_win, text="Password", bg="#1f1f1f", fg="white").pack()
    pass_entry = Entry(create_win, show="*", font=("Arial", 12))
    pass_entry.pack(pady=5)

    Label(create_win, text="Opening Balance", bg="#1f1f1f", fg="white").pack()
    bal_entry = Entry(create_win, font=("Arial", 12))
    bal_entry.pack(pady=5)

    def save_account():
        ac = ac_entry.get().strip()
        name = name_entry.get().strip()
        password = pass_entry.get().strip()
        balance = bal_entry.get().strip()

        if ac == "" or name == "" or password == "" or balance == "":
            messagebox.showerror("Error", "Fill all fields")
            return

        if ac in accounts:
            messagebox.showerror("Error", "Account Already Exists")
            return

        try:
            initial_bal = float(balance)
        except ValueError:
            messagebox.showerror("Error", "Invalid Balance Amount")
            return

        accounts[ac] = {
            "name": name,
            "password": password,
            "balance": initial_bal
        }

        messagebox.showinfo("Success", "Account Created Successfully")
        create_win.destroy()

    Button(
        create_win,
        text="Create Account",
        bg="green",
        fg="white",
        width=18,
        command=save_account
    ).pack(pady=20)


# ---------------- Deposit ----------------
def deposit_money():
    win = Toplevel(root)
    win.title("Deposit Money")
    win.geometry("350x250")
    win.configure(bg="#1f1f1f")

    Label(
        win,
        text="Deposit Money",
        font=("Arial", 18, "bold"),
        bg="#1f1f1f",
        fg="cyan"
    ).pack(pady=15)

    Label(win, text="Enter Amount", bg="#1f1f1f", fg="white").pack()
    amount_entry = Entry(win, font=("Arial", 12))
    amount_entry.pack(pady=10)

    def deposit():
        if amount_entry.get().strip() == "":
            messagebox.showerror("Error", "Enter Amount")
            return

        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Enter a positive amount")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid Amount")
            return

        accounts[current_account]["balance"] += amount
        transactions.append(f"{current_account} : Deposited ₹{amount}")

        messagebox.showinfo(
            "Success",
            f"₹{amount} Deposited Successfully\n\nCurrent Balance = ₹{accounts[current_account]['balance']}"
        )
        win.destroy()

    Button(
        win,
        text="Deposit",
        bg="green",
        fg="white",
        width=15,
        command=deposit
    ).pack(pady=15)


# ---------------- Withdraw ----------------
def withdraw_money():
    win = Toplevel(root)
    win.title("Withdraw Money")
    win.geometry("350x250")
    win.configure(bg="#1f1f1f")

    Label(
        win,
        text="Withdraw Money",
        font=("Arial", 18, "bold"),
        bg="#1f1f1f",
        fg="cyan"
    ).pack(pady=15)

    Label(win, text="Enter Amount", bg="#1f1f1f", fg="white").pack()
    amount_entry = Entry(win, font=("Arial", 12))
    amount_entry.pack(pady=10)

    def withdraw():
        if amount_entry.get().strip() == "":
            messagebox.showerror("Error", "Enter Amount")
            return

        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Enter a positive amount")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid Amount")
            return

        if amount > accounts[current_account]["balance"]:
            messagebox.showerror("Error", "Insufficient Balance")
            return

        accounts[current_account]["balance"] -= amount
        transactions.append(f"{current_account} : Withdrew ₹{amount}")

        messagebox.showinfo(
            "Success",
            f"₹{amount} Withdrawn Successfully\n\nCurrent Balance = ₹{accounts[current_account]['balance']}"
        )
        win.destroy()

    Button(
        win,
        text="Withdraw",
        bg="red",
        fg="white",
        width=15,
        command=withdraw
    ).pack(pady=15)


# ---------------- Balance Enquiry ----------------
def balance_enquiry():
    messagebox.showinfo(
        "Balance",
        f"Account Holder : {accounts[current_account]['name']}\n\nCurrent Balance : ₹{accounts[current_account]['balance']}"
    )


# ---------------- Transaction History ----------------
def transaction_history():
    win = Toplevel(root)
    win.title("Transaction History")
    win.geometry("450x350")
    win.configure(bg="#1f1f1f")

    Label(
        win,
        text="Transaction History",
        font=("Arial", 18, "bold"),
        bg="#1f1f1f",
        fg="cyan"
    ).pack(pady=10)

    listbox = Listbox(win, width=50, height=12, font=("Arial", 11))
    listbox.pack(pady=10)

    found = False
    for item in transactions:
        if item.startswith(current_account):
            listbox.insert(END, item)
            found = True

    if not found:
        listbox.insert(END, "No Transactions Available")


# ---------------- Change Password ----------------
def change_password():
    win = Toplevel(root)
    win.title("Change Password")
    win.geometry("350x300")
    win.configure(bg="#1f1f1f")

    Label(
        win,
        text="Change Password",
        font=("Arial", 18, "bold"),
        bg="#1f1f1f",
        fg="cyan"
    ).pack(pady=15)

    Label(win, text="Old Password", bg="#1f1f1f", fg="white").pack()
    old_entry = Entry(win, show="*", font=("Arial", 12))
    old_entry.pack(pady=5)

    Label(win, text="New Password", bg="#1f1f1f", fg="white").pack()
    new_entry = Entry(win, show="*", font=("Arial", 12))
    new_entry.pack(pady=5)

    def save():
        old = old_entry.get()
        new = new_entry.get()

        if old != accounts[current_account]["password"]:
            messagebox.showerror("Error", "Old Password Incorrect")
            return

        if new.strip() == "":
            messagebox.showerror("Error", "New Password cannot be empty")
            return

        accounts[current_account]["password"] = new
        messagebox.showinfo("Success", "Password Changed Successfully")
        win.destroy()

    Button(
        win,
        text="Save",
        width=15,
        bg="green",
        fg="white",
        command=save
    ).pack(pady=20)


# ---------------- Logout ----------------
def logout(frame):
    global current_account
    current_account = ""
    frame.destroy()
    login_frame.place(relwidth=1, relheight=1)
    account_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------- Dashboard ----------------
def dashboard():
    login_frame.place_forget()

    dashboard_frame = Frame(root, bg="#1f1f1f")
    dashboard_frame.place(relwidth=1, relheight=1)

    Label(
        dashboard_frame,
        text="BANK MANAGEMENT SYSTEM",
        font=("Arial", 20, "bold"),
        bg="#1f1f1f",
        fg="cyan"
    ).pack(pady=20)

    Label(
        dashboard_frame,
        text=f"Welcome {accounts[current_account]['name']}",
        font=("Arial", 16),
        bg="#1f1f1f",
        fg="white"
    ).pack(pady=10)

    Button(
        dashboard_frame,
        text="Create Account",
        width=20,
        font=("Arial", 12),
        command=create_account
    ).pack(pady=5)

    Button(
        dashboard_frame,
        text="Deposit",
        width=20,
        font=("Arial", 12),
        command=deposit_money
    ).pack(pady=5)

    Button(
        dashboard_frame,
        text="Withdraw",
        width=20,
        font=("Arial", 12),
        command=withdraw_money
    ).pack(pady=5)

    Button(
        dashboard_frame,
        text="Balance Enquiry",
        width=20,
        font=("Arial", 12),
        command=balance_enquiry
    ).pack(pady=5)

    Button(
        dashboard_frame,
        text="Transaction History",
        width=20,
        font=("Arial", 12),
        command=transaction_history
    ).pack(pady=5)

    Button(
        dashboard_frame,
        text="Change Password",
        width=20,
        font=("Arial", 12),
        command=change_password
    ).pack(pady=5)

    Button(
        dashboard_frame,
        text="Logout",
        width=20,
        bg="red",
        fg="white",
        font=("Arial", 12),
        command=lambda: logout(dashboard_frame)
    ).pack(pady=20)


# ---------------- Login Logic ----------------
def login():
    global current_account

    ac = account_entry.get().strip()
    pw = password_entry.get().strip()

    if ac in accounts:
        if accounts[ac]["password"] == pw:
            current_account = ac
            dashboard()
        else:
            messagebox.showerror("Error", "Wrong Password")
    else:
        messagebox.showerror("Error", "Account Not Found")


# ---------------- Main Window Setup ----------------
root = Tk()
root.title("Bank Management System")
root.geometry("600x550")
root.configure(bg="#1f1f1f")

login_frame = Frame(root, bg="#1f1f1f")
login_frame.place(relwidth=1, relheight=1)

Label(
    login_frame,
    text="USER LOGIN",
    font=("Arial", 22, "bold"),
    bg="#1f1f1f",
    fg="cyan"
).pack(pady=20)

Label(
    login_frame,
    text="Account Number",
    font=("Arial", 12),
    bg="#1f1f1f",
    fg="white"
).pack()

account_entry = Entry(login_frame, font=("Arial", 12))
account_entry.pack(pady=5)

Label(
    login_frame,
    text="Password",
    font=("Arial", 12),
    bg="#1f1f1f",
    fg="white"
).pack()

password_entry = Entry(login_frame, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

Button(
    login_frame,
    text="Login",
    width=15,
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=login
).pack(pady=20)

root.mainloop()