from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import Add_material,view_material,Add_assignment,view_assignment
class homes():
    def __init__(self):
        self.root=Tk()
        self.root.title("Recodir")
        self.root.geometry("1400x800")
        i,j=self.root.size()
        # self.root.resizable(False,False)
        self.root.config(bg='white')
        # self.root.pack()
        self.frame=Frame(self.root,width=200,height=800,bg='#D3D3D3')
        self.frame.place(x=0,y=0)
        
        self.frame1 = Frame(self.root, width=1200, height=800,bg="white")
        self.frame1.place(x = 200, y = 0)       
        #--------Admin pic------------------------------------------
        self.img=Image.open('images/user1.jpg').resize((25,25))
        try:
            self.imgTk=ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(e)
        self.imgLbl=Label(self.root,image=self.imgTk,bg='#D3D3D3')
        self.imgLbl.place(x=7,y=22)
        
        
        #-------BUTTONS----------------------------------------------
        self.user=Label(self.frame,text='USER',bg='white',font=('JUST Sans',15,'bold')).place(x=40,y=22)  
        # self.dashboard=Button(self.frame,width=30,height=3,pady=7,text='Dashboard',bg='#57a1f8',fg='white',border=1,command=self.Dashboard)
        # self.dashboard.place(x=0,y=100)
        self.add_material=Button(self.frame,width=30,height=3,pady=7,text='Add Material',bg='#57a1f8',fg='white',border=1,command=self.ADD_material)
        self.add_material.place(x=0,y=100)
        self.view_material=Button(self.frame,width=30,height=3,pady=7,text='View Material',bg='#57a1f8',fg='white',border=1,command=self.view_material)
        self.view_material.place(x=0,y=166)
        self.add_assignment=Button(self.frame,width=30,height=3,pady=7,text='Add Assignment',bg='#57a1f8',fg='white',border=1,command=self.Add_assignment).place(x=0,y=232)
        self.view_assignment=Button(self.frame,width=30,height=3,pady=7,text='View Assignment',bg='#57a1f8',fg='white',border=1,command=self.view_assignment).place(x=0,y=298)
        # self.add_teacher=Button(self.frame,width=30,height=3,pady=7,text='Add Teacher',bg='#57a1f8',fg='white',border=1,command=self.Add_Teacher).place(x=0,y=430)
        # self.view_teaher=Button(self.frame,width=30,height=3,pady=7,text='View Teacher',bg='#57a1f8',fg='white',border=1,command=self.view_teacher).place(x=0,y=496)
        #--------------------------------------------------------------
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
          
          
if __name__=='__main__':
    homes()