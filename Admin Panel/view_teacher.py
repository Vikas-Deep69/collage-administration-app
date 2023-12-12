from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database,login_page,edit_teacher
from tkinter import ttk
from tkinter.ttk import Treeview

class view_teachers():
    def __init__(self, frame):
        self.frame1 = frame
        self.lbl = Label(self.frame1, text="TEACHERS", bg='white', fg='black', border=0, font=("JUST Sans", 15))
        self.lbl.place(x=10, y=10)

        # Create a Treeview widget 
        self.tr = Treeview(self.frame1, columns=('Name', 'Contact', 'Qualification', 'Username', 'Subject', 'Edit', 'Delete'),show="headings")
        self.tr.heading('Name', text="Name")
        self.tr.heading('Contact', text="Contact")
        self.tr.heading('Qualification', text="Qualification")
        self.tr.heading('Username', text="username")
        self.tr.heading('Edit', text="Edit")
        self.tr.heading('Delete', text="Delete")
        self.tr.heading('Subject', text="Subject")

        # Create a horizontal scrollbar
        h_scrollbar = Scrollbar(self.frame1, orient='horizontal', command=self.tr.xview)
        self.tr.configure(xscrollcommand=h_scrollbar.set)

        # Place Treeview and Scrollbar
        self.tr.place(x=10, y=50, width=1200)  
        h_scrollbar.place(x=10, y=50 + self.tr.winfo_height(), width=self.tr.winfo_width())

        # Populate Treeview
        data = database.getTeacher()
        for i in data:
            self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[6], 'Edit', 'Delete'))

        self.tr.bind('<Double-Button-1>', self.actions)

    def actions(self, e):
        print("i am e", e)
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'cols {col}')
        gup = (self.tr.item(tt).get('text'),)
        print("i am gup", gup, col)
        if col == '#7':
            res = messagebox.askyesno("Delete", "Do You Really Want to delete this item.")
            if res:
                re = database.delTeacher(gup)
                if re:
                    messagebox.showinfo("Success", "Deleted Successfully")
                    view_teachers(self.frame1)
                else:
                    messagebox.showwarning('Alert', 'Something went wrong.')
        if col == '#6':
            print('edit is called')
            for i in self.frame1.winfo_children():
                i.destroy()
            edit_teacher.edit_teachers(self.frame1, gup)

if __name__ == "__main__":
    view_teachers()

