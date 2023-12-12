from tkinter import Tk, Toplevel, Entry, Label, Button
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image,ImageTk
import database,view_assignment

class edit_assignment:
    def __init__(self,frame,gup):
        self.frame2=frame
        print(gup)
        self.teacher_info = database.getbyassignment(gup)

        self.img=Image.open('images/addassignment.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame2,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.course_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.course_entry.place(x=582,y=208)
        self.course_entry.insert(0,self.teacher_info[0])
        self.department_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.department_entry.place(x=582,y=246)
        self.department_entry.insert(0,self.teacher_info[1])
        self.subject_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.subject_entry.place(x=582,y=283)
        self.subject_entry.insert(0,self.teacher_info[2])
        self.Number_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.Number_entry.place(x=582,y=321)
        self.Number_entry.insert(0,self.teacher_info[3])
        #--------------------------------------
        
        self.update_button=Button(self.frame2,width=15,text="UPDATE",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.update_material).place(x=500,y=364)
        # Function to update the teacher information
    def update_material(self):
        new_course = self.course_entry.get()
        new_department = self.department_entry.get()
        new_subject = self.subject_entry.get()
        new_Number = self.Number_entry.get()
        # new_password=self.password_entry.get()
        # Call your database update function
        success = database.updateAssignment(self.teacher_info[3], new_course, new_department, new_subject,new_Number)
        if success:
            messagebox.showinfo("Success", "Assignment information updated successfully.")
            # Refresh the Treeview after updating
            for i in self.frame2.winfo_children():
                i.destroy()
            view_assignment.view_assignment(self.frame2)
            
        else:
            messagebox.showwarning("Error", "Failed to update assignment information.")

if __name__ == "__main__":
    edit_assignment()
