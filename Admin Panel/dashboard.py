from tkinter import *
import database, login_page
from PIL import Image,ImageTk
from tkinter import messagebox,ttk,PhotoImage
import matplotlib.pyplot as plt
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database,time

class Dashboard:
    def __init__(self, master):
        count,count1,count2=0,0,0
        #---------STAFF------------------
        self.master = master
        self.img=Image.open("images/staff.png").resize((240,140))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imglbl=Label(self.master,image=self.imgTk,bg="white")
        self.imglbl.place(x=50,y=70)   
        self.l=Label(self.master,text="Teachers",bg="#FECB5B",fg="black",font=("JUST Sans",13))
        self.l.place(x=180,y=120)
        for i in database.getTeacher():
            count+=1
        count=str(count)
        self.l1=Label(self.master,text=count,bg="#FECB5B",fg="black",font=("JUST Sans",13))
        self.l1.place(x=200,y=150)
        
        
        #--------------Course---------------
        self.img1=Image.open("images/course.png").resize((240,140))
        self.imgTk1=ImageTk.PhotoImage(self.img1)
        self.imglbl1=Label(self.master,image=self.imgTk1,bg="white")
        self.imglbl1.place(x=340,y=70)   
        self.l=Label(self.master,text="Courses",bg="#98FB98",fg="black",font=("JUST Sans",13))
        self.l.place(x=470,y=120)
        for i in database.getCourse():
            count1+=1
        count1=str(count1)
        self.l2=Label(self.master,text=count1,bg="#98FB98",fg="black",font=("JUST Sans",13))
        self.l2.place(x=490,y=150)
        
        
        #-------------------subject------------
        self.img2=Image.open("images/subject.png").resize((240,140))
        self.imgTk2=ImageTk.PhotoImage(self.img2)
        self.imglbl2=Label(self.master,image=self.imgTk2,bg="white")
        self.imglbl2.place(x=625,y=70)   
        self.l=Label(self.master,text="Subjects",bg="#00B4D8",fg="black",font=("JUST Sans",13))
        self.l.place(x=760,y=120)
        for i in database.getSubject():
            count2+=1
        count2=str(count2)
        self.l3=Label(self.master,text=count2,bg="#00B4D8",fg="black",font=("JUST Sans",13))
        self.l3.place(x=780,y=150)
        
        
         #---------bargraph-------------\\
        self.frame2=Frame(self.master,width=1200,height=550,bg="white")
        self.frame2.place(x=0,y=250)
        staff_count, course_count ,subject_count = database.barview()  # Call the function to get the counts

        categories = ['Teachers', 'Courses', 'Subjects']
        values= [int(count), int(count1) ,int(count2)]
        colors = ['lightcoral', '#ffcd5e', '#95ff93', 'lightskyblue']
        # Create a figure and axis for the bar chart
        fig, ax = plt.subplots(figsize=(4,4))
        ax.bar(categories, values, color=colors)
        
        # Add labels and title
        ax.set_xlabel('Names')
        ax.set_ylabel('Values')
        ax.set_title('DATA COUNT')
        # Embed the bar chart in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig,master=self.frame2)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=300,y=10)
        #------------------------------------------------------------
        self.date_time= Label(self.master)
        self.date_time.place(x=1000, y=30)
        self.show_time()
    def show_time(self):
        self.time = time.strftime("%H:%M:%S",)
        self.date = time.strftime('%d/%h/%y')
        set_text = f"  {self.time} \n{self.date}"
        self.date_time.configure(text=set_text, font=("times new roman", 16, "bold"), bd=0, bg="white", fg="#035995")
        self.date_time.after(100, self.show_time)
        
       