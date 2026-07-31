# window
import tkinter as tk 
# root = tk.Tk()
# root.mainloop()

#title
# root = tk.Tk()
# root.title("my first app")
# root.mainloop()

#size
# # root = tk.Tk()
# root.title("my first app")
# root.geometry("500x300")
# root.mainloop()

# bg color
# # root = tk.Tk()
# root.geometry("1000x600")
# root.title("lucky app")
# root.configure(bg="black")
# root.mainloop()

#label
# root = tk.Tk()
# l = tk.Label(root,text="hello lucifer")
# l.pack()
# root.mainloop()

# font
# root = tk.Tk()
# l = tk.Label(root,text = "welcome lucifer",font= ("arial",30))
# l.pack()
# root.mainloop()

#font with color
# root = tk.Tk()
# l = tk.Label(root,text="hyy guys",font=("cursive",30),fg="black",bg="gold")
# l.pack()
# root.mainloop()

#all 
# root = tk.Tk()
# root.title("lucifer app ")
# root.geometry("700x500")
# root.configure(bg="black")
# l = tk.Label(root,text="lucifer welcome back",fg="red",bg="white",font=("cursive",40,"bold"))
# l.pack()
# root.mainloop()

#button
# root = tk.Tk()
# root.title("lucifer")
# root.geometry("1000x700")

# b = tk.Button(root,text="click me")
# b.pack()

# root.mainloop()

# button
# def hello():
#     print("hello lucifer")
    
    
# root = tk.Tk()
# root.title("lucifer")
# root.geometry("1000x700")
# b=tk.Button(root,text = "welcome",command=hello)
# b.pack()
# root.mainloop()

#change a label
# def change_text():
#     l.config(text = "welcome lucifer",fg="darkred",bg="black")
    
# root = tk.Tk()
# root.title("lucifer")
# root.geometry("500x500")

# l=tk.Label(root,text="hello lucifer",font=("arial",20))
# l.pack(pady=20)

# b = tk.Button(root,text="click",command=change_text)
# b.pack()

# root.mainloop()

def practise():
    l.config(text="welcome back king of hell",fg="red",bg="navyblue")
    
root=tk.Tk()
root.title("lucifer")
root.geometry("400x400")
root.configure(bg="black")

l=tk.Label(root,text="hello",font=("arial",30))
l.pack(pady=30)

b=tk.Button(root,text="touch",command=practise)
b.pack()

root.mainloop()
