from tkinter import Tk, Toplevel, Entry, Label, Button
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image,ImageTk
import database,view_material

class edit_material:
    def __init__(self,frame,gup):
        self.frame2=frame
        print(gup)
        self.teacher_info = database.getbytopic(gup)

        self.img=Image.open('images/addmaterial.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame2,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.course_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.course_entry.place(x=582,y=217)
        self.course_entry.insert(0,self.teacher_info[0])
        self.department_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.department_entry.place(x=582,y=255)
        self.department_entry.insert(0,self.teacher_info[1])
        self.subject_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.subject_entry.place(x=582,y=294)
        self.subject_entry.insert(0,self.teacher_info[2])
        self.topic_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=0)
        self.topic_entry.place(x=582,y=332)
        self.topic_entry.insert(0,self.teacher_info[3])
        #--------------------------------------
        
        self.update_button=Button(self.frame2,width=15,text="UPDATE",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.update_material).place(x=500,y=375)
        # Function to update the teacher information
    def update_material(self):
        new_course = self.course_entry.get()
        new_department = self.department_entry.get()
        new_subject = self.subject_entry.get()
        new_topic = self.topic_entry.get()
        # new_password=self.password_entry.get()
        # Call your database update function
        success = database.updateMaterial(self.teacher_info[3], new_course, new_department, new_subject,new_topic)
        if success:
            # view_teacher.view_teachers(self.frame2)
            messagebox.showinfo("Success", "Teacher information updated successfully.")
            # Refresh the Treeview after updating
            # self.refresh_treeview()
            # self.frame2.destroy()
            for i in self.frame2.winfo_children():
                i.destroy()
            view_material.view_materials(self.frame2)
            
        else:
            messagebox.showwarning("Error", "Failed to update teacher information.")

if __name__ == "__main__":
    edit_material()
