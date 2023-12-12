from tkinter import *
import database, login_page
from PIL import Image,ImageTk
from tkinter import messagebox,ttk

class AddCourse:
    def __init__(self, frame):
        print('add course constructor called')
        self.frame1 = frame
        #------------Add course Label------------------------
        # self.frame1=Frame(self.root,width=1400,height=800,bg="white").place(x=200,y=0)
        # self.add_course=Label(self.frame1,text="ADD COURSE",font=("Modern Sans",30,"bold"),fg="black").place(x=350,y=100)
        # self.name=Label(self.frame1,text="Name",font=("JUST Sans",20),fg="black").place(x=400,y=200)
        # self.duration=Label(self.frame1,text="Duration",font=("JUST Sans",20),fg="black").place(x=400,y=240)
        # self.cost=Label(self.frame1,text="Cost",font=("JUST Sans",20),fg="black").place(x=400,y=280)
        #-------------------------------------------------------
        self.img=Image.open('images/addcourse.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame1,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.name_entry=Entry(self.frame1,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.name_entry.place(x=582,y=237)
        self.duration_entry=ttk.Combobox(self.frame1,values=["1 YEARS","2 YEARS","3 YEARS","4 YEARS","5 YEARS"],font=("JUST Sans",12),width=15)
        self.duration_entry.set("select years")
        self.duration_entry.place(x=582,y=275)
        self.cost_entry=Entry(self.frame1,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.cost_entry.place(x=582,y=313)
        #--------------------------------------
        
        self.ADD_button=Button(self.frame1,width=15,text="ADD",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.register_course).place(x=500,y=356)
        
    def register_course(self):
        if self.name_entry.get() and self.duration_entry.get() and self.cost_entry.get() :
            # print(self.username_entry.get())
            res = database.registerCourse((self.name_entry.get(), self.duration_entry.get(), self.cost_entry.get()))
            if res:
                messagebox.showinfo('Success', 'Details Submitted successfully.')
                AddCourse(self.frame1)
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Please enter your details.')