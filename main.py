import tkinter as tk
import random
import time

print("if there are any errors, contact")
time.sleep(5)
root = tk.Tk()
root.title("Mini Shop")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="lightgreen")
def store():
    items = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry", "Blueberry", "Watermelon", "Peach","Kiwi", "Papaya"]

    items_list = tk.Label(root, height=15, width=10, bg="lightgreen", fg="dark green", font=("Helvetica", 15, "bold"), text="Apple\n\nBanana\n\nOrange\n\nGrapes\n\nMango\n\nPineapple\n\nStrawberry\n\nBlueberry\n\nWatermelon\n\nPeach\n\nKiwi\n\nPapaya")
    items_list.place(x=25, y=70)
    Title = tk.Label(root, height=2, width=15, bg="lightgreen", fg="dark green", font=("Helvetica", 25, "bold"), text="Mini Shop")
    Title.place(x=145, y=5)
    prchs = tk.Entry(root, width=20, font=("Helvetica", 15))
    prchs.place(x= 175, y=450)
    prchs.insert(0,"")
    prchs_btn = tk.Button(root, height=2, width=15, bg="dark green", fg="white", font=("Helvetica", 15, "bold"), text="Purchase", command=lambda: purchase())
    prchs_btn.place(x=175, y=500)
    def purchase():
        item = prchs.get().capitalize()
        if item in items:
            confirmation = tk.Label(root, height=2, width=30, bg="lightgreen", fg="dark green", font=("Helvetica", 15, "bold"), text=f"Purchased: {item}")
            confirmation.place(x=150, y=550)
        else:
            error = tk.Label(root, height=2, width=30, bg="lightgreen", fg="red", font=("Helvetica", 15, "bold"), text="Item not available")
            error.place(x=150, y=550)
store()
root.mainloop()
