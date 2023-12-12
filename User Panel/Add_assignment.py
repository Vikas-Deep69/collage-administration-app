from tkinter import *
import database,databaseA
from PIL import Image,ImageTk
from tkinter import messagebox,ttk

class AddAssignment:
    def __init__(self, frame):
        print('add addassignment constructor called')
        self.frame1 = frame
        #------------Add course Label------------------------
        # self.frame1=Frame(self.root,width=1400,height=800,bg="white").place(x=200,y=0)
        # self.add_course=Label(self.frame1,text="ADD ASSIGNMENT",font=("JUST Sans",30,"bold"),fg="black").place(x=350,y=100)
        # self.name=Label(self.frame1,text="Course",font=("JUST Sans",20),fg="black").place(x=400,y=200)
        # self.duration=Label(self.frame1,text="Department",font=("JUST Sans",20),fg="black").place(x=400,y=240)
        # self.cost=Label(self.frame1,text="Subject",font=("JUST Sans",20),fg="black").place(x=400,y=280)
        # self.cost=Label(self.frame1,text="Number",font=("JUST Sans",20),fg="black").place(x=400,y=320)
        #-------------------------------------------------------
        self.img=Image.open('images/addassignment.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame1,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.course_entry=ttk.Combobox(self.frame1,width=17,values=databaseA.getCourseName(),font=("JUST Sans",11))
        self.course_entry.place(x=582,y=208)
        self.department_entry=ttk.Combobox(self.frame1,width=17,values=["CSE/IT"],font=("JUST Sans",11))
        self.department_entry.place(x=582,y=246)
        self.subject_entry=ttk.Combobox(self.frame1,width=17,values=databaseA.getSubjectName(),font=("JUST Sans",11))
        self.subject_entry.place(x=582,y=283)
        self.Number_entry=Entry(self.frame1,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.Number_entry.place(x=582,y=321)
        #--------------------------------------
        
        self.ADD_button=Button(self.frame1,width=15,text="ADD",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.register_assignment).place(x=500,y=364)
        
    def register_assignment(self):
        if self.course_entry.get() and self.department_entry.get() and self.subject_entry.get() and self.Number_entry.get() :
            res = database.registerAssignment((self.course_entry.get(),self.department_entry.get(),self.subject_entry.get(),self.Number_entry.get()))
            if res:
                messagebox.showinfo('Success', 'Details Submitted successfully.')
                AddAssignment(self.frame1)
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Please enter your details.')