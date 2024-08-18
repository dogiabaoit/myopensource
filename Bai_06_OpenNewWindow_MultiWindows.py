from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk      #pip install pillow

root = Tk()
root.geometry("500x600")
root.title("Registration Form")

imge=Image.open("football.jpg")
photo=ImageTk.PhotoImage(imge)

lab = Label(image=photo)
lab.pack()

#Variable
fn=StringVar()
ln=StringVar()
dn=StringVar()
var=StringVar()
var_c1="Java"
var_c2="Python"
radio_var=StringVar()

def printt():
    first=fn.get()
    sec=ln.get()
    dob1=dn.get()
    var1=var.get()
    var2=var_c1
    var3=var_c2
    var4=radio_var.get()

    print(f"Your Fullname is {first} {sec}")
    print(f"Your Age is {dob1}")
    print(f"Your Country is {var1}")
    print(f"Your Prog Language is {var2} {var3}")
    print(f"Your Gender is {var4}")
    #MESSAGEBOX
    tkinter.messagebox.showinfo("Welcome","User is successfully signed up !!!")

def second_window():
    window=Tk()
    window.title("Welcome to second window")
    window.geometry('250x200')
    label_02=Label(window,text="Registration Completed !", relief="solid", font=('arial',12,'bold')).place(x=30,y=70)
    but_01=Button(window,text='Login', width=12, bg='brown', fg='white', command=abt).place(x=80,y=110)
    window.mainloop()

def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("Welcom to DGB study !!!","This is demo for menu fields")

#MENU
menu=Menu(root)
root.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=exit1)

subm2=Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About", command=abt)

#BODY
label_0=Label(root, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
label_0.place(x=90,y=150)

label_1=Label(root,text="FirstName :", width=20,font=("arial",10,"bold"))
label_1.place(x=80,y=230)

entry_1=Entry(root, textvar=ln)
entry_1.place(x=240,y=230)

label_2=Label(root,text="LastName :", width=20,font=("arial",10,"bold"))
label_2.place(x=80,y=260)

entry_2=Entry(root, textvar=fn)
entry_2.place(x=240,y=260)

label_3=Label(root,text="DOB :", width=20,font=("arial",10,"bold"))
label_3.place(x=80,y=290)

entry_3=Entry(root, textvar=dn)
entry_3.place(x=240,y=290)

label_4=Label(root,text="Country :", width=20,font=("arial",10,"bold"))
label_4.place(x=80,y=320)

#DROP LIST - SELECTBOX
list1=['Nepal','India','Canada','Viet Nam']
droplist=OptionMenu(root,var,*list1)
var.set("Select country")
droplist.config(width=15)
droplist.place(x=240,y=320)

#CHECKBOX, RADIO
label_5=Label(root,text="Prog Lang :", width=20,font=("arial",10,"bold"))
label_5.place(x=80,y=350)

c1=Checkbutton(root,text="Java",variable=var_c1).place(x=240,y=350)
c1=Checkbutton(root,text="Python",variable=var_c2).place(x=290,y=350)

label_6=Label(root,text="Gender :", width=20,font=("arial",10,"bold"))
label_6.place(x=80,y=380)

r1=Radiobutton(root,text="Male",variable=radio_var,value="Male").place(x=240,y=380)
r2=Radiobutton(root,text="Female",variable=radio_var,value="Female").place(x=290,y=380)

#BUTTON
b1=Button(root,text="Signup",width=12,bg='brown',fg='white',command=printt)
b1.place(x=150, y=530)

b2=Button(root,text="Quit",width=12,bg='brown',fg='white',command=exit1)
b2.place(x=280, y=530)

b3=Button(root,text="Login",width=12,bg='brown',fg='white',command=second_window)
b3.place(x=208, y=560)


root.mainloop()
