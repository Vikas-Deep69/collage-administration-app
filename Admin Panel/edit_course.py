from tkinter import Tk, Toplevel, Entry, Label, Button
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image,ImageTk
import database,view_course

class edit_course:
    def __init__(self,frame,gup):
        self.frame2=frame
        self.gup1=gup
        self.teacher_info = database.getbycourse(gup)

        print(self.teacher_info)
        self.img=Image.open('images/addcourse.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame2,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.name_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.name_entry.place(x=582,y=237)
        self.name_entry.insert(0,self.teacher_info[0])
        self.duration_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.duration_entry.place(x=582,y=275)
        self.duration_entry.insert(0,self.teacher_info[1])
        self.cost_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.cost_entry.place(x=582,y=313)
        self.cost_entry.insert(0,self.teacher_info[2])
        #--------------------------------------
        
        self.update_course=Button(self.frame2,width=15,text="UPDATE",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.update_course).place(x=500,y=356)
        # Function to update the teacher information
    def update_course(self):
        new_name = self.name_entry.get()
        new_duration = self.duration_entry.get()
        new_cost = self.cost_entry.get()
               
        # Call your database update function
        success = database.updateCourse(self.gup1, new_name, new_duration, new_cost)
        if success:
            messagebox.showinfo("Success", "Teacher information updated successfully.")
            # Refresh the Treeview after updating
           
            for i in self.frame2.winfo_children():
                i.destroy()
            view_course.view_course(self.frame2)
            
        else:
            messagebox.showwarning("Error", "Failed to update teacher information.")

if __name__ == "__main__":
    edit_course()
