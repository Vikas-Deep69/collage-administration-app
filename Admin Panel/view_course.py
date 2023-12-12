from tkinter import *
from tkinter import messagebox
import database,edit_course
from tkinter import ttk
from tkinter.ttk import Treeview
 
class view_course():
    def __init__(self, frame):
        self.frame1=frame
        self.lbl=Label(self.frame1,text="COURSES",bg='white',fg='black',border=0,font=("JUST Sans",15))
        self.lbl.place(x=10,y=10)
        self.tr=Treeview(self.frame1,columns=('Name','Duration','Cost','Edit','Delete'),show="headings")
        self.tr.heading('Name',text="Name")
        self.tr.heading('Duration',text="Duration")
        self.tr.heading('Cost',text="Cost")
        self.tr.heading('Edit',text="Edit")
        self.tr.heading('Delete',text="Delete")
        data = database.getCourse()
        print('user are', data)
        for i in data:
            self.tr.insert('',0,text=i[0],values=(i[1],i[2],i[3],'Edit','Delete'))
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
        if col == '#5':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                re = database.delCourse(gup)
                if re:
                    messagebox.showinfo("Success","Deleted Successfully")
                    view_course(self.frame1)
                    
                else:
                    messagebox.showwarning('Alert', 'Something went wrong.')    
        if col == '#4':
            for i in self.frame1.winfo_children():
                i.destroy()
            edit_course.edit_course(self.frame1,gup)
            
if __name__=="__main__":
    view_course()