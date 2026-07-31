import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Complete Tkinter Demo")
root.geometry("900x650")
root.config(bg="#F0F8FF")

# ---------------- MENU ---------------- #
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About",
                      command=lambda: messagebox.showinfo("About", "Tkinter Demo Program"))

# ---------------- HEADER (PACK) ---------------- #
header = tk.Frame(root, bg="navy", height=60)
header.pack(fill="x")

title = tk.Label(
    header,
    text="STUDENT REGISTRATION SYSTEM",
    fg="white",
    bg="navy",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# ---------------- FORM FRAME (GRID) ---------------- #
form = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
form.pack(side="left", padx=20, pady=20)

# Variables
name = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar(value="Male")
city = tk.StringVar()
agree = tk.IntVar()

# Name
tk.Label(form, text="Name").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(form, textvariable=name, width=25).grid(row=0, column=1)

# Age
tk.Label(form, text="Age").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(form, textvariable=age, width=25).grid(row=1, column=1)

# Gender
tk.Label(form, text="Gender").grid(row=2, column=0, sticky="w")

tk.Radiobutton(form, text="Male", variable=gender,
               value="Male").grid(row=2, column=1, sticky="w")

tk.Radiobutton(form, text="Female", variable=gender,
               value="Female").grid(row=3, column=1, sticky="w")

# City
tk.Label(form, text="City").grid(row=4, column=0, sticky="w")

combo = ttk.Combobox(
    form,
    textvariable=city,
    values=["Delhi", "Mumbai", "Jaipur", "Lucknow", "Pune"]
)
combo.grid(row=4, column=1)

# Spinbox
tk.Label(form, text="Semester").grid(row=5, column=0)
spin = tk.Spinbox(form, from_=1, to=8)
spin.grid(row=5, column=1)

# Scale
tk.Label(form, text="Marks").grid(row=6, column=0)
scale = tk.Scale(form, from_=0, to=100, orient="horizontal")
scale.grid(row=6, column=1)

# Checkbox
tk.Checkbutton(
    form,
    text="I Agree",
    variable=agree
).grid(row=7, column=1, sticky="w")

# Text Widget
tk.Label(form, text="Address").grid(row=8, column=0)
address = tk.Text(form, width=20, height=4)
address.grid(row=8, column=1)

# ---------------- FUNCTIONS ---------------- #
def submit():

    if name.get() == "":
        messagebox.showerror("Error", "Enter Name")
        return

    info = f"""
Name : {name.get()}
Age : {age.get()}
Gender : {gender.get()}
City : {city.get()}
Semester : {spin.get()}
Marks : {scale.get()}
Agree : {'Yes' if agree.get() else 'No'}

Address :
{address.get('1.0', tk.END)}
"""

    messagebox.showinfo("Student Information", info)

    student_list.insert(tk.END, name.get())


def clear():

    name.set("")
    age.set("")
    city.set("")
    gender.set("Male")
    agree.set(0)
    address.delete("1.0", tk.END)
    scale.set(0)

# Buttons
tk.Button(form, text="Submit", bg="green", fg="white",
          command=submit).grid(row=9, column=0, pady=10)

tk.Button(form, text="Clear", bg="red", fg="white",
          command=clear).grid(row=9, column=1)

# ---------------- RIGHT PANEL (PLACE) ---------------- #
side = tk.Frame(root, bg="lightyellow", width=250, height=450)
side.place(x=600, y=100)

tk.Label(
    side,
    text="Student List",
    font=("Arial", 14, "bold"),
    bg="lightyellow"
).place(x=60, y=10)

student_list = tk.Listbox(side, width=25, height=15)
student_list.place(x=20, y=50)

# Event
def show_selected(event):
    if student_list.curselection():
        item = student_list.get(student_list.curselection())
        messagebox.showinfo("Selected", item)

student_list.bind("<<ListboxSelect>>", show_selected)

# Footer
footer = tk.Label(
    root,
    text="Tkinter Demo using Pack + Grid + Place",
    bg="gray",
    fg="white"
)
footer.pack(side="bottom", fill="x")

root.mainloop()