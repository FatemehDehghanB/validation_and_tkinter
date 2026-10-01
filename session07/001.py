from tkinter import *
from validation import *


window = Tk()
window.title("استعلام گیری")
window.geometry("400x600")


Label(window, text="phone number").place(x=20, y=20)  # phone
phone = StringVar()
Entry(window).place(x=120, y=20)

Label(window, text="national ID").place(x=20, y=50)  # national id
Entry(window).place(x=120, y=50)

Label(window, text="card number").place(x=20, y=80)  # card number
Entry(window).place(x=120, y=80)

Label(window , text = "plate").place(x=20 , y=110)
Entry(window).place(x=120 , y=110)

Button(window, text="استعلام").place(x=200 , y=180)

window.mainloop()
