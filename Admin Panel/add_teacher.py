from tkinter import *
import database, login_page
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
class AddTeacher:
    def __init__(self, frame):
        self.frame1 = frame
        self.frame1.config(bg="white")
        #   #------------Add course Label------------------------
        # # self.frame1=Frame(self.root,width=1400,height=800,bg="white").place(x=200,y=0)
        # self.add_course=Label(self.frame1,text="ADD TEACHER",font=("JUST Sans",30),fg="black").place(x=500,y=100)
        # self.name=Label(self.frame1,text="Name",font=("JUST Sans",20),fg="black").place(x=400,y=200)
        # self.contact=Label(self.frame1,text="Contact",font=("JUST Sans",20),fg="black").place(x=400,y=240)
        # self.qualification=Label(self.frame1,text="Qualification",font=("JUST Sans",20),fg="black").place(x=400,y=280)
        # self.username=Label(self.frame1,text="Username",font=("JUST Sans",20),fg="black").place(x=400,y=320)
        # self.password=Label(self.frame1,text="Password",font=("JUST Sans",20),fg="black").place(x=400,y=360)
        # #-------------------------------------------------------
        self.img=Image.open('images/addteacher.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame1,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        
        #----------------ENTRY-----------------
        self.name_entry=Entry(self.frame1,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.name_entry.place(x=583,y=198)
        self.contact_entry=Entry(self.frame1,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.contact_entry.place(x=583,y=236)
        self.qualification_entry=ttk.Combobox(self.frame1,width=17,values=["Btech","Mtech","PhD"],font=("JUST Sans",11))
        self.qualification_entry.place(x=582,y=274)
        self.qualification_entry.set("select")
        self.username_entry=Entry(self.frame1,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.username_entry.place(x=583,y=312)
        self.password_entry=Entry(self.frame1,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.password_entry.place(x=583,y=350)
        self.subject=Label(self.frame1,text="Subject",font=("Times New Roman",15),fg="black",bg="white").place(x=415,y=378)
        self.subject_entry=ttk.Combobox(self.frame1,width=16,values=database.getSubjectName(),font=("JUST Sans",11))
        self.subject_entry.place(x=582,y=380)
        self.subject_entry.set("select subject")
        
        #--------------------------------------
        
        self.ADD_button=Button(self.frame1,width=15,text="Submit",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.register_teacher).place(x=500,y=410)
        
    def register_teacher(self):
        if self.name_entry.get() and self.contact_entry.get() and self.qualification_entry.get() and self.username_entry.get() and  self.password_entry.get() and self.subject_entry.get():
            print(self.username_entry.get())
            res = database.registerTeacher((self.name_entry.get(), self.contact_entry.get(), self.qualification_entry.get(),self.username_entry.get(),self.password_entry.get(),self.subject_entry.get()))
            if res:
                messagebox.showinfo('Success', 'Details Submitted successfully.')
                AddTeacher(self.frame1)
                # self.register_course()
            else:
                messagebox.showerror('Alert', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Please enter your details.')