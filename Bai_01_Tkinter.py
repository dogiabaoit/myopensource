from tkinter import *
window=Tk()
window.geometry("300x300")
window.title("Welcome")

label1=Label(window,text="Welcome to Tkinter",fg='blue',bg='yellow',relief="solid",font=("arial",16,"bold")).pack()
#label1=Label(window,text="Welcome to Tkinter",fg='blue',bg='yellow',relief="solid",font=("arial",16,"bold")).place(x=110,y=110)

#label1=Label(window,text="Welcome to Tkinter",fg='blue',bg='yellow',relief="solid",font=("arial",16,"bold"))
#label1.pack(fill=BOTH,padx=2,pady=2,expand=True)
#label1.grid(row=1,column=1)


button1=Button(window,text="Demo",fg='white',bg='brown',relief=GROOVE,font=("arial",12,"bold"))
button1.place(x=110,y=110)                                  #GROOVE , RIDGE , SUNKEN , RAISED
window.mainloop()