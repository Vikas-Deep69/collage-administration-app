from tkinter import *
import database, login_page
from PIL import Image,ImageTk
from tkinter import messagebox,ttk

class AddSubject:
    def __init__(self, frame):
        print('add subject constructor called')
        self.frame1 = frame
        #------------Add course Label------------------------
        # self.frame1=Frame(self.root,width=1400,height=800,bg="white").place(x=200,y=0)
        # self.add_course=Label(self.frame1,text="ADD SUBJECT",font=("JUST Sans",30),fg="black").place(x=500,y=100)
        # self.name=Label(self.frame1,text="Degree",font=("JUST Sans",20),fg="black").place(x=400,y=200)
        # self.duration=Label(self.frame1,text="Course",font=("JUST Sans",20),fg="black").place(x=400,y=240)
        # self.cost=Label(self.frame1,text="Name",font=("JUST Sans",20),fg="black").place(x=400,y=280)
        #-------------------------------------------------------
        self.img=Image.open('images/addsubject.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame1,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.degree_entry=ttk.Combobox(self.frame1,width=17,values=["Btech","Mtech"],font=("JUST Sans",11))
        self.degree_entry.place(x=582,y=235)
        self.degree_entry.set("select degree")
        self.course_entry=ttk.Combobox(self.frame1,width=17,values=database.getCourseName(),font=("JUST Sans",11))
        self.course_entry.place(x=582,y=273)
        self.course_entry.set("select course")
        self.name_entry=Entry(self.frame1,width=15,font=("JUST Sans",13),fg="black",border=1)
        self.name_entry.place(x=582,y=311)
        #--------------------------------------
        
        self.ADD_button=Button(self.frame1,width=15,text="ADD",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.register_course).place(x=500,y=355)
        
    def register_course(self):
        if self.degree_entry.get() and self.course_entry.get() and self.name_entry.get() :
            # print(self.username_entry.get())
            res = database.registerSubject((self.degree_entry.get(), self.course_entry.get(), self.name_entry.get()))
            if res:
                messagebox.showinfo('Success', 'Details Submitted successfully.')
                AddSubject(self.frame1)
                # self.register_course()
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Please enter your details.')