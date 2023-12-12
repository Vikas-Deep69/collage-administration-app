from tkinter import *
from tkinter import messagebox
import databaseU,edit_material
from tkinter.ttk import Treeview
 
class view_materials():
    def __init__(self, frame):
        self.frame1=frame
        self.lbl=Label(self.frame1,text="MATERIAL",bg='white',fg='black',border=0,font=("JUST Sans",15))
        self.lbl.place(x=10,y=10)
        self.tr=Treeview(self.frame1,columns=('Course','Department','Subject','Topic','Edit','Delete'),show="headings")
        self.tr.heading('Course',text="Course")
        self.tr.heading('Department',text="Department")
        self.tr.heading('Subject',text="Subject")
        self.tr.heading('Topic',text="Topic")
        self.tr.heading('Edit',text="Edit")
        self.tr.heading('Delete',text="Delete")
        data = databaseU.getMaterial()
        print('user are', data)
        for i in data:
            self.tr.insert('',0,text=i[0],values=(i[1],i[2],i[3],i[4],'Edit','Delete'))
        self.tr.bind('<Double-Button-1>',self.actions)
        self.tr.place(x = 10, y = 50)
    def actions(self,e):
        print("i am e",e)
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'cols {col}')
        # print(self.tr.item(tt))

        gup = ( self.tr.item(tt).get('text'),)
        print("i am gup",gup, col)
        if col == '#6':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                re = databaseU.delMaterial(gup)
                if re:
                    messagebox.showinfo("Success","Deleted Successfully")
                    view_materials(self.frame1)
                    
                else:
                    messagebox.showwarning('Alert', 'Something went wrong.')    
        if col == '#5':
            for i in self.frame1.winfo_children():
                i.destroy()
            edit_material.edit_material(self.frame1,gup)
