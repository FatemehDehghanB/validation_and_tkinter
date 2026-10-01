from session07 import validation
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from session07.validation import card_validator , phone_validator
from session07.validation import nationalid_validator
from session07.validation import plate_validator
window = Tk()
window.title("استعلام گیری")
window.geometry("300x500")

date_list=[]
def estelam():
    try:
        datas={"card number":card_validator(card_num.get()) ,
               "phone number": phone_validator(phone_num.get()) ,
               "national id":nationalid_validator(id_num.get()),
               "plate": plate_validator(plate_num.get())}
        date_list.append(datas)
        print(date_list)
        messagebox.showinfo("saved", "استعلام با موفقیت انجام شد")
        card_num.set("")
        phone_num.set("")
        id_num.set("")
        plate_num.set("")
    except Exception as e:
        messagebox.showinfo("error" ,f"خطا{e}")

Label(window, text="card number"). place(x=20 , y=20)
card_num = StringVar()
Entry(window , textvariable=card_num).place(x=120, y=20)

Label(window, text="national ID").place(x=20 , y=60)
id_num = StringVar()
Entry(window, textvariable= id_num).place(x=120 , y=60)

Label(window, text= "plate number").place(x=20 , y=100)
plate_num = StringVar()
Entry(window , textvariable=plate_num).place(x=120 , y=100)

Label(window , text= "phone number").place(x=20 , y=140)
phone_num = StringVar()
Entry(window , textvariable=phone_num).place(x=120 , y=140)

Button(window, text="استعلام", command=estelam).place(x=150 , y=200)

window.mainloop()