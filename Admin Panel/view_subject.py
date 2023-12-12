from tkinter import *
from tkinter import messagebox
import database,edit_subject
from tkinter.ttk import Treeview, Scrollbar

class view_subject():
    def __init__(self, frame):
        self.frame1 = frame
        self.lbl=Label(self.frame1,text="SUBJECTS",bg='white',fg='black',border=0,font=("JUST Sans",15))
        self.lbl.place(x=10,y=10)
        # Create a vertical scrollbar
        self.tree_scroll = Scrollbar(frame)
        self.tree_scroll.place(x=1000,y=50)

        self.tr = Treeview(self.frame1, columns=('Degree', 'Course', 'Name', 'Edit', 'Delete'), show="headings", yscrollcommand=self.tree_scroll.set)
        
        self.tree_scroll.config(command=self.tr.yview)  # Link the scrollbar to the Treeview's yview

        self.tr.heading('Degree', text="Degree")
        self.tr.heading('Course', text="Course")
        self.tr.heading('Name', text="Name")
        self.tr.heading('Edit', text="Edit")
        self.tr.heading('Delete', text="Delete")
        data = database.getSubject()
        print('user are', data)
        for i in data:
            self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3], 'Edit', 'Delete'))
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=10, y=50)

    def actions(self, e):
        print("i am e", e)
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'cols {col}')
        gup = (self.tr.item(tt).get('text'),)
        print("i am gup", gup, col)
        if col == '#5':
            res = messagebox.askyesno("Delete", "Do You Really Want to delete this item.")
            if res:
                re = database.delSubject(gup)
                if re:
                    messagebox.showinfo("Success", "Deleted Successfully")
                    view_subject(self.frame1)
                else:
                    messagebox.showwarning('Alert', 'Something went wrong.')    
        if col == '#4':
            for i in self.frame1.winfo_children():
                i.destroy()
            edit_subject.edit_subject(self.frame1,gup)
            
if __name__=="__main__":
    view_subject()