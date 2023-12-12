from tkinter import Tk, Toplevel, Entry, Label, Button
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image,ImageTk
import database,view_subject

class edit_subject:
    def __init__(self,frame,gup):
        self.frame2=frame
        self.gup1=gup
        self.teacher_info = database.getbysubject(gup)

        print(self.teacher_info)
    
        self.img=Image.open('images/addsubject.png').resize((1300,650))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.frame2,image=self.imgTk,bg="white")
        self.imgLbl.place(x=-80,y=-80)
        #----------------ENTRY---------------
        self.degree_entry=Entry(self.frame2,width=16,font=("JUST Sans",13),fg="black",border=1)
        self.degree_entry.place(x=582,y=235)
        self.degree_entry.insert(0,self.teacher_info[0])
        self.course_entry=Entry(self.frame2,width=15,font=("JUST Sans",13),fg="black",border=1)
        self.course_entry.place(x=582,y=273)
        self.course_entry.insert(0,self.teacher_info[1])
        self.name_entry=Entry(self.frame2,width=15,font=("JUST Sans",13),fg="black",border=1)
        self.name_entry.place(x=582,y=311)
        self.name_entry.insert(0,self.teacher_info[2])
        #--------------------------------------
        
        self.update_button=Button(self.frame2,width=15,text="UPDATE",bg='#57a1f8',fg='white',border=0,font=("JUST Sans",13),command=self.update_subject).place(x=500,y=355)
        # Function to update the teacher information
    def update_subject(self):
        new_degree = self.degree_entry.get()
        new_course = self.course_entry.get()
        new_name = self.name_entry.get()
        
        # Call your database update function
        success = database.updateSubject(self.gup1, new_degree, new_course, new_name)
        if success:
            messagebox.showinfo("Success", "Teacher information updated successfully.")
            # Refresh the Treeview after updating
           
            for i in self.frame2.winfo_children():
                i.destroy()
            view_subject.view_subject(self.frame2)
            
        else:
            messagebox.showwarning("Error", "Failed to update teacher information.")

if __name__ == "__main__":
    edit_subject()
