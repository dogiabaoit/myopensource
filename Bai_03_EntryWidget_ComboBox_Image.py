from tkinter import *
from PIL import Image,ImageTk      #pip install pillow

root = Tk()
root.geometry("500x600")
root.title("Registration Form")

imge=Image.open("C:/Users/ADMIN/PycharmProjects/GUI/football.jpg")
photo=ImageTk.PhotoImage(imge)

lab = Label(image=photo)
lab.pack()

fn=StringVar()
ln=StringVar()
dn=StringVar()
var=StringVar()

def printt():
    first=fn.get()
    sec=ln.get()
    dob1=dn.get()
    var1=var.get()
    print(f"Your Fullname is {first} {sec}")
    print(f"Your Age is {dob1}")
    print(f"Your Country is {var1}")

    label_5 = Label(root, text=f"Hey! {first} {sec} {dob1} {var1}",fg='green', relief=GROOVE, width=50, font=("arial", 10, "bold"))
    label_5.place(x=10, y=430)

def exit1():
    exit()

label_0=Label(root, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
label_0.place(x=90,y=150)

label_1=Label(root,text="FirstName :", width=20,font=("arial",10,"bold"))
label_1.place(x=80,y=230)

entry_1=Entry(root, textvar=ln)
entry_1.place(x=240,y=230)

label_2=Label(root,text="LastName :", width=20,font=("arial",10,"bold"))
label_2.place(x=80,y=280)

entry_2=Entry(root, textvar=fn)
entry_2.place(x=240,y=280)

label_3=Label(root,text="DOB :", width=20,font=("arial",10,"bold"))
label_3.place(x=80,y=330)

entry_3=Entry(root, textvar=dn)
entry_3.place(x=240,y=330)

label_4=Label(root,text="Country :", width=20,font=("arial",10,"bold"))
label_4.place(x=80,y=380)

list1=['Nepal','India','Canada','Viet Nam']
droplist=OptionMenu(root,var,*list1)
var.set("Select country")
droplist.config(width=15)
droplist.place(x=230,y=380)

b1=Button(root,text="Signup",width=12,bg='brown',fg='white',command=printt)
b1.place(x=150, y=480)

b2=Button(root,text="Quit",width=12,bg='brown',fg='white',command=exit1)
b2.place(x=280, y=480)

root.mainloop()