from tkinter import*
from PIL import Image,ImageTk
from Course import courseClass
from Student import StudentClass
from result import resultClass
from Report import ReportClass
from tkinter import messagebox
import os
from tkinter import*
from PIL import Image, ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox,ttk
import os

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")


        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")



        title=Label(self.root,text="Student Result Managment System",
        padx=10,compound=LEFT,image=self.logo_dash,
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
         
        #====Menu====
        M_Frame=LabelFrame(self.root,text="Menus",font=("time new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("foudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_Student=Button(M_Frame,text="Student",font=("foudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_Student).place(x=240,y=5,width=200,height=40)
        btn_Result=Button(M_Frame,text="Result",font=("foudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_View=Button(M_Frame,text="View",font=("foudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_Report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="logout",font=("foudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("foudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)
       

       #========content========
        self.bg_img=Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=900,height=350)

        #=========update=======
        self.lbl_course=Label(self.root,text="Totle Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b86")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_Student=Label(self.root,text=" Totle Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad")
        self.lbl_Student.place(x=710,y=530,width=300,height=100)

        self.lbl_Result=Label(self.root,text="Totle Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0E8503")
        self.lbl_Result.place(x=1020,y=530,width=300,height=100)
# clock=======
        self.lbl=Label(self.root,text="\nShashi kant",font=("Book Antiqua","25","bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,height=450,width=350)
    
        self.working()

       #======footer========
        title=Label(self.root,text=" SRMS-Student Result Managment System \nContact Us for any Technical Issue: 6201534525",
        font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        self.update_details()

    def update_details(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
             cur.execute("SELECT * FROM course")
             cr=cur.fetchall()
             self.lbl_course.config(text=f"Totle Course\n[ {str(len(cr))} ]")
            
             cur.execute("SELECT * FROM student")
             cr=cur.fetchall()
             self.lbl_Student.config(text=f"Totle students\n[ {str(len(cr))} ]")

             cur.execute("SELECT * FROM result")
             cr=cur.fetchall()
             self.lbl_Result.config(text=f"Totle Resluts\n[ {str(len(cr))} ]")




             self.lbl_course.after(200,self.update_details)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        

        self.Clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="Clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def Clock_image(self,hr,min_,sec_):
        Clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(Clock)
  
  #clock image======
        
        bg = Image.open(r"D:\Project Python\images\c.png")
        bg = bg.resize((300,300), Image.Resampling.LANCZOS)
        Clock.paste(bg,(50,50))
        Clock.save("Clock_new.png")

        origin=200,200
 #clock Hour line image=======
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
#clock min line image=======
        
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
#clock sec line image=======
        
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)

        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        Clock.save("Clock_new.png")

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseClass(self.new_win)
        
    def add_Student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_Report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
        os.system('python "D:/Project Python/images/clock.py"')


    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            
    


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()