import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        amount=int(entry.get())
        if amount <=0:
            raise ValueError

        denominations= [1000,500,200,100,50]
        result=""

        for d in denominations:
            count=amount//d
            if count>0:
        
                result+=f"{d}: {count}\n"
            amount%=d

        top=tk.Toplevel(root)
        top.title("Denomination Breakdown")
        tk.Label(top,text="Breakdown:",font=("Arial",12,"bold")).pack(pady=5)
        tk.Text(top, height=12, width=30).pack(pady=5)

        output=tk.Text(top, height=12,width=30)
        output.pack(pady=5)
        output.inser(tk.END, result)
    except ValueError:
        messagebox.showerror("Invalid Imput","Please enter a valid positive integer amount.")

root =tk.Tk()
root.title("Denomination Calculator")
root.geometry("300x200")

tk.Label(root, text="Enter Amount:", font=("Arial",10)).pack(pady=5)
entry=tk.Entry(root, width=20)
entry.pack(pady=5)

tk.Button(root, text="Calculator", command=calculate).pack(pady=10)

root.mainloop()
            