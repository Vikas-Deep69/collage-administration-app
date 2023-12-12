from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database,login_page,view_teacher, add_course,add_teacher,view_course,add_subject,view_subject,Home_pageU,dashboard,view_data,first_page,time
from tkinter import ttk
from tkinter.ttk import Treeview

class homes():
    def __init__(self):
        self.root=Tk()
        self.root.title("Recodir")
        self.root.geometry("1400x800")
        i,j=self.root.size()
        # self.root.resizable(False,False)
        self.root.config(bg='white')
        self.frame=Frame(self.root,width=200,height=800,bg='#57a1f8')
        self.frame.place(x=0,y=0)
        
        self.frame1 = Frame(self.root, width=1200, height=800,bg="white")
        self.frame1.place(x = 200, y = 0) 
        self.welcome=Label(self.frame1,text="Welcome Admin!",bg="white",fg='#2832C2',border=0,font=("JUST Sans",25))   
        self.welcome.place(x=20,y=30)  
        #--------recodir pic------------------------------------------
        self.img=Image.open('images/image.png').resize((170,35))
        try:
            self.imgTk=ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(e)
        self.imgLbl=Label(self.root,image=self.imgTk,bg='#57a1f8')
        self.imgLbl.place(x=7,y=22)
        
        
        #-------BUTTONS----------------------------------------------
        self.dashboard=Button(self.frame,width=23,height=3,pady=7,text='Dashboard',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.Dashboard)
        self.dashboard.place(x=0,y=100)
        self.add_course=Button(self.frame,width=23,height=3,pady=7,text='Add Course',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.Add_Course)
        self.add_course.place(x=0,y=166)
        self.view_course=Button(self.frame,width=23,height=3,pady=7,text='View Course',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.view_course)
        self.view_course.place(x=0,y=232)
        self.add_subject=Button(self.frame,width=23,height=3,pady=7,text='Add Subject',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.Add_Subject).place(x=0,y=298)
        self.view_subject=Button(self.frame,width=23,height=3,pady=7,text='View Subject',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.view_subject).place(x=0,y=364)
        self.add_teacher=Button(self.frame,width=23,height=3,pady=7,text='Add Teacher',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.Add_Teacher).place(x=0,y=430)
        self.view_teaher=Button(self.frame,width=23,height=3,pady=7,text='View Teacher',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.view_teacher).place(x=0,y=496)
        self.view_data=Button(self.frame,width=23,height=3,pady=7,text='View User Data',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.view_data).place(x=0,y=562)
        self.logout=Button(self.frame,width=23,height=3,pady=7,text='Logout',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.logout).place(x=-5,y=630)
        self.img1=Image.open('images/exit.png').resize((27,27))
        #--------------------------------------------------------------
        try:
            self.imgTk1=ImageTk.PhotoImage(self.img1)
        except Exception as e:
            print(e)
        self.imgLbl1=Label(self.root,image=self.imgTk1,bg='#57a1f8')
        self.imgLbl1.place(x=20,y=650)
        #--------------------------------------------------------------
        self.date_time= Label(self.frame1)
        self.date_time.place(x=1000, y=30)
        self.show_time()
        
        self.root.mainloop()
        
    
    def Dashboard(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        dashboard.Dashboard(self.frame1)      
    def Add_Teacher(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        add_teacher.AddTeacher(self.frame1)               
  
    def view_teacher(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        view_teacher.view_teachers(self.frame1)
            
    def Add_Course(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        add_course.AddCourse(self.frame1)
        
    def view_course(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        view_course.view_course(self.frame1)   
         
    def Add_Subject(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        add_subject.AddSubject(self.frame1)    
    
    def view_subject(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        view_subject.view_subject(self.frame1) 
    def another(self):
        self.root.destroy()
        Home_pageU.homes()
    def view_data(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        view_data.view_data(self.frame1)  
    def logout(self):
        self.root.destroy()
        first_page.first()
    def show_time(self):
        self.time = time.strftime("%H:%M:%S",)
        self.date = time.strftime('%d/%h/%y')
        set_text = f"  {self.time} \n{self.date}"
        self.date_time.configure(text=set_text, font=("times new roman", 16, "bold"), bd=0, bg="white", fg="#035995")
        self.date_time.after(100, self.show_time)
if __name__=='__main__':
    homes()