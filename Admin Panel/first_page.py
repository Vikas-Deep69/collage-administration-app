from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import login_page,LOGIN_PAGE1

class first():
    def __init__(self):
        self.root=Tk()
        self.root.title("Recodir")
        self.root.geometry("1400x800")
        i,j=self.root.size()
       
        # self.root.resizable(False,False)
        self.root.config(bg='#2832C2')
        self.img=Image.open("images/first.png").resize((1400,700))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imglb=Label(self.root,image=self.imgTk,bg="#2832C2")
        self.imglb.place(x=0,y=0)
        self.admin=Button(self.root,text="Admin",fg='#4169e1',bg='white',border=0,font=("JUST Sans",14),width=12,command=self.admin)
        self.admin.place(x=632,y=415)
        self.admin=Button(self.root,text="User",fg='#4169e1',bg='white',border=0,font=("JUST Sans",14),width=12,command=self.user)
        self.admin.place(x=632,y=474)
        self.root.mainloop()
        
    def admin(self):
        self.root.destroy()
        LOGIN_PAGE1.main()        
    def user(self):
        self.root.destroy()
        login_page.main()
        
if __name__=='__main__':
    first()