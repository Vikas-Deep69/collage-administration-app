from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import Add_material,view_material,Add_assignment,view_assignment,first_page,time
class homes():
    def __init__(self):
        self.root=Tk()
        self.root.title("Recodir")
        self.root.geometry("1400x800")
        i,j=self.root.size()
        # self.root.resizable(False,False)
        self.root.config(bg='white')
        # self.root.pack()
        self.frame=Frame(self.root,width=200,height=800,bg='#57a1f8')
        self.frame.place(x=0,y=0)
        
        self.frame1 = Frame(self.root, width=1200, height=800,bg="white")
        self.frame1.place(x = 200, y = 0)   
        self.welcome=Label(self.frame1,text="Welcome User!",bg="white",fg='#2832C2',border=0,font=("JUST Sans",25))   
        self.welcome.place(x=20,y=30)     
        #--------Admin pic------------------------------------------
        self.img=Image.open('images/image.png').resize((170,35))
        try:
            self.imgTk=ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(e)
        self.imgLbl=Label(self.root,image=self.imgTk,bg='#57a1f8')
        self.imgLbl.place(x=7,y=22)
        
        
        #-------BUTTONS----------------------------------------------
        # self.user=Label(self.frame,text='USER',bg='#57a1f8',fg="white",font=('JUST Sans',19,'bold')).place(x=50,y=22)  
        # self.dashboard=Button(self.frame,width=30,height=3,pady=7,text='Dashboard',bg='#57a1f8',fg='white',border=1,command=self.Dashboard)
        # self.dashboard.place(x=0,y=100)
        self.add_material=Button(self.frame,width=23,height=3,pady=7,text='Add Material',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.ADD_material)
        self.add_material.place(x=0,y=100)
        self.view_material=Button(self.frame,width=23,height=3,pady=7,text='View Material',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.view_material)
        self.view_material.place(x=0,y=174)
        self.add_assignment=Button(self.frame,width=23,height=3,pady=7,text='Add Assignment',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.Add_assignment).place(x=0,y=248)
        self.view_assignment=Button(self.frame,width=23,height=3,pady=7,text='View Assignment',bg='#57a1f8',fg='white',border=1,font=("JUST Sans",11),command=self.view_assignment).place(x=0,y=322)
        self.logout=Button(self.frame,width=23,height=1,pady=7,text='Logout',bg='#57a1f8',fg='white',border=0,font=("JUST Sans",11),command=self.logout).place(x=-5,y=645)
        
        #-----------REcodir logo------------------------------------------------
        self.img1=Image.open('images/exit.png').resize((27,27))
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
        
    
    # def Dashboard(self):
    #     self.dashboard=Label(self.frame1,text="DASHBoard",font=("JUST Sans",30),fg="black") 
    #     self.dashboard.place(x=20,y=39) 
    def ADD_material(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        Add_material.AddMaterial(self.frame1)            
  
    def view_material(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        view_material.view_materials(self.frame1)

    def Add_assignment(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        Add_assignment.AddAssignment(self.frame1)        
    def view_assignment(self):
        for i in self.frame1.winfo_children():
            i.destroy()
        view_assignment.view_assignment(self.frame1)
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