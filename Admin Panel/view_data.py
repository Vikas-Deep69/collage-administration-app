from tkinter import *
from tkinter import messagebox
import databaseU,edit_material
from tkinter.ttk import Treeview
import view_material,view_assignment
 
class view_data():
    def __init__(self, frame):
        print("view data")
        self.frame1=frame
        self.frame2=Frame(self.frame1,width=1200,height=700,border=2,bg="white")
        self.frame2.place(x=0,y=100)
        self.material_btn=Button(self.frame1,width=15,text="View Material",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",15),command=self.view_material).place(x=20,y=50)
        self.assigment_btn=Button(self.frame1,width=15,text="View Assignment",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",15),command=self.view_assignment).place(x=200,y=50)
        
    def view_material(self):
        for i in self.frame2.winfo_children():
            i.destroy()
        view_material.view_materials(self.frame2)
    def view_assignment(self):
        for i in self.frame2.winfo_children():
            i.destroy()
        view_assignment.view_assignment(self.frame2)
          
          
if __name__=='__main__':
    homes()
        
        
       