from tkinter import *
from tkinter import messagebox,ttk
from tkinter.ttk import Treeview
from PIL import Image,ImageTk
import database,view_teacher

class edit_teachers:
    def __init__(self,frame,gup):
        self.frame2=frame
        self.gup1=gup
        self.teacher_info = database.getbyusername(gup)

        print(self.teacher_info)
        self.img=Image.open('images/addteacher.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame2,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        
        #----------------ENTRY-----------------
        self.name_entry=Entry(self.frame2,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.name_entry.place(x=583,y=198)
        self.name_entry.insert(0,self.teacher_info[0])
        self.contact_entry=Entry(self.frame2,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.contact_entry.place(x=583,y=236)
        self.contact_entry.insert(0,self.teacher_info[1])
        self.qualification_entry=Entry(self.frame2,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.qualification_entry.place(x=583,y=274)
        self.qualification_entry.insert(0,self.teacher_info[2])
        self.username_entry=Entry(self.frame2,width=16,font=("JUST Sans",12),fg="black",border=0)
        self.username_entry.place(x=583,y=312)
        self.username_entry.insert(0,self.teacher_info[3])
        self.subject=Label(self.frame2,text="Subject",font=("Times New Roman",15),fg="black",bg="white").place(x=415,y=378)
        self.subject_entry=ttk.Combobox(self.frame2,width=16,values=database.getSubjectName(),font=("JUST Sans",11))
        self.subject_entry.place(x=582,y=380)
        self.subject_entry.set(self.teacher_info[4])
        # self.subject_entry.insert(0,self.teacher_info[4])
        
      
        self.Update_button=Button(self.frame2,width=15,text="UPDATE",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.update_teacher).place(x=500,y=410)
        # Function to update the teacher information
    def update_teacher(self):
        new_name = self.name_entry.get()
        new_contact = self.contact_entry.get()
        new_qualification = self.qualification_entry.get()
        new_username = self.username_entry.get()
        new_subject = self.subject_entry.get()
        # new_password=self.password_entry.get()
        # Call your database update function
        success = database.updateTeacher(self.gup1, new_name, new_contact, new_qualification, new_username,new_subject)
        if success:
            # view_teacher.view_teachers(self.frame2)
            messagebox.showinfo("Success", "Teacher information updated successfully.")
            # Refresh the Treeview after updating
            # self.refresh_treeview()
            # self.frame2.destroy()
            for i in self.frame2.winfo_children():
                i.destroy()
            view_teacher.view_teachers(self.frame2)
            
        else:
            messagebox.showwarning("Error", "Failed to update teacher information.")

if __name__ == "__main__":
    edit_teachers()
