import tkinter as tk 
def lucifer():
    name = n.get()
    e.config(text=f"welcome  {name}")
root = tk.Tk()
root.title("greeting")
root.geometry("800x500")

l=tk.Label(root,text="greeting app",font=("arial",20,"bold"))
l.pack(pady=20)

n=tk.Entry(root,font=("arial",20,"bold"))
n.pack(pady=20)

e=tk.Label(root,font=("arial",40))
e.pack(pady=20)

b=tk.Button(root,text=("enter your name and click here "),font=("Arial",14,"bold"),command=lucifer)
b.pack(pady=20)


root.mainloop()