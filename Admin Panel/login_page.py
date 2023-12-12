from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database,Home_pageU
import customtkinter
class main():
    def __init__(self,):
        super().__init__()
        
        self.root=Tk()
        self.root.title("hello")
        self.root.geometry("1200x800")
        i,j=self.root.size()
        #   self.root.resizable(False,False)
        self.root.config(bg='white')
        #Image
        self.img=Image.open('images/img.jpg').resize((850,550))
        self.imgTk=ImageTk.PhotoImage(self.img)
        self.imgLbl=Label(self.root,image=self.imgTk,bg='white')
        self.imgLbl.place(x=-120,y=20)
      
        #frame
        self.frame=Frame(self.root,width=375,height=700,bg='white')
        self.frame.place(x=750,y=70)
       
        #headings
        self.heading=Label(self.frame,text='Sign in',fg='#57a1f8',bg='white',font=('JUST Sans',30,'bold'))
        self.heading.place(x=0,y=5)
      
        #User entry
        #bind method
        def on_enter(e):
            self.user.delete(0,'end')
        def on_leave(e):
            self.name=self.user.get()
            if self.name=='':
                self.user.insert(0,'Username')
        #entry  
        self.user=Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',15,'bold'))
        self.user.place(x=0,y=110)
        self.user.insert(0,'Username')
        # self.user.config(fg='grey')
        self.user.bind('<FocusIn>',on_enter)
        self.user.bind('<FocusOut>',on_leave)
      
      
        Frame(self.frame,width=300,height=2,bg='black').place(x=0,y=150)
      
        #password
        def on_enter(e):
            self.passwd.delete(0,'end')
        def on_leave(e):
            self.name=self.passwd.get()
            if self.name=='':
              self.passwd.insert(0,'Password')
          
        self.passwd=Entry(self.frame,width=25,fg='black',border=0,bg='white',show='*',font=('Microsoft YaHei UI Light',15,'bold'))
        self.passwd.place(x=0,y=220)
        self.passwd.insert(0,'Password')
        # self.passwd.config(fg='grey')
        self.passwd.bind('<FocusIn>',on_enter)
        self.passwd.bind('<FocusOut>',on_leave)
     
     
        self.img1 = Image.open('images/eye.png').resize((18, 18))
        self.img1Tk = ImageTk.PhotoImage(self.img1)
        # self.img1Lbl = Label(self.frame, image = self.img1Tk)
        # self.img1Lbl.place(x=400,y=200)

        self.img2 = Image.open('images/eye_open.png').resize((20, 20))
        self.img2Tk = ImageTk.PhotoImage(self.img2)
        # self.img2Lbl = Label(self.frame, image = self.img2Tk,bg='black')
        # self.img2Lbl.place(x=400,y=200)

        #------toggle button--------
        self.toggle_btn = Button(self.frame, image=self.img1Tk, width=15,border=0,bg='white', command=self.toggle)
        self.toggle_btn.place(x=275,y=220)
        #--------------------------

        Frame(self.frame,width=300,height=2,bg='black').place(x=0,y=255)

        #Button
        self.btn=Button(self.frame,width=35,pady=7,text='Sign in',bg='#57a1f8',fg='white',font=('JUST Sans',10,'bold'),border=0,command=self.login)
        self.btn.place(x=0,y=320)

        self.root.mainloop()
        #show and hide password button method
    def toggle(self):
        if self.passwd.cget('show') == '':
          self.passwd.config(show='*')
          self.toggle_btn.config(image = self.img1Tk)
        else:
          self.passwd.config(show='')
          self.toggle_btn.config(image=self.img2Tk)
    def login(self):
        print('button is clicked')
        if self.user.get() and self.passwd.get():
            # print(self.userEntry.get(),'data is given')
            
            res = database.loginUser((self.user.get(), self.passwd.get()))
            if res:
                self.root.destroy()
                Home_pageU.homes()
            else:
                messagebox.showerror('Alert', 'Invalid username/password.')
        else:
            print('Enter your details')
            messagebox.showwarning('Alert', 'Please enter your details')
            
if __name__=='__main__':
    main()
    
