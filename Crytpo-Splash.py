
from ast import Lambda
from logging import root
from msilib import sequence
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from turtle import back, onclick
import tkinter as tk
import sqlite3



#database code

# USER PROFILE DATABASE
connect_userProfile = sqlite3.connect('APP database.db')    # Connecting database file to python file

c = connect_userProfile.cursor()    # Creating database with columns
c.execute("""
    CREATE TABLE IF NOT EXISTS UserProfile(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL)
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS UserContent(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    platform TEXT NOT NULL)
""")







#welcome page

window = Tk()
window.title("Applied Cryptography")
window.geometry('450x400')
a='#940721'
Frame(window,width=450,height=400,bg=a).place(x=0,y=0) 

label1=Label(window,text='WELCOME...',fg='white',bg=a,font=('Calibri (Body)',18,'bold'))
label1.place(x=50,y=80)





def main_page():
        
        
        
        m=Tk()
        m.title('Database page')
        m.geometry('450x400')
  
        b='#9fbdbf'
        Frame(m,width=450,height=400,bg=b).place(x=0,y=0) 
        
        Table=ttk.Treeview(m)
        #naming the columns
        Table['columns']= ("Username","Password","Description")
        
        #formatting  the column
        Table.column('#0', width=120, minwidth=25)
        Table.column("Username", anchor=W,width=120)
        Table.column("Password",anchor=CENTER,width= 80)
        Table.column("Description", anchor=W , width=120)

        #headings

        Table.heading("#0",text="ID",anchor=W)
        Table.heading("Username",text="Username",anchor=W)
        Table.heading("Password",text="Password", anchor=CENTER)
        Table.heading("Description", text="Platform",anchor=W)

        #sample data

        Table.insert(parent='',index='end',iid=0,text="1",values=("Dhinuk","1234","Hi"))

        Table.pack(pady=20)
       
        #buttons

       
        
        button7=Button(m,width= 10,height= 1,text= 'Add',command=addbutton_page, border=0,fg=b,bg = 'white',cursor="hand2")
        button7.place(x=350,y=250) 

        button8=Button(m,width= 10,height= 1,text= 'Modify',command=main_page, border=0,fg=b,bg = 'white',cursor="hand2")
        button8.place(x=350,y=300) 

        button9=Button(m,width= 10,height= 1,text= 'Remove',command=main_page, border=0,fg=b,bg = 'white',cursor="hand2")
        button9.place(x=350,y=350) 


def addbutton_page():
    ap=Tk()
    ap.title('Add')
    ap.geometry('450x400')
    
    b='#9fbdbf'
    Frame(ap,width=450,height=400,bg=b).place(x=0,y=0) 

     # entering username
    def enter(e):
            label11.delete(0, 'end')
    def leave(e):
          if label11.get()=="":
             label11.insert(0, 'Username')
             
    label11=Entry(ap,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label11.place(x=90,y= 110)
    label11.insert(0, 'Username')
    label11.bind("<FocusIn> ",enter)
    label11.bind("<FocusOut> ",leave)
    
    Frame(ap,width=300,height=2,bg='black').place(x=85,y=132)

   

        # entering the password
    def enter(e):
          label12.delete(0, 'end')
    def leave(e):
          if label12.get()=="":
            label12.insert(0, 'Password',)
        
    label12=Entry(ap,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label12.place(x=90,y= 160)
    label12.insert(0, 'Password')
    label12.bind("<FocusIn> ",enter)
    label12.bind("<FocusOut> ",leave)

    Frame(ap,width=300,height=2,bg='black').place(x=85,y=180)
    
    #entering platform

    def enter(e):
        label13.delete(0, 'end')
    def leave(e):
        if label13.get()=="":
            label13.insert(0, ' Platform')
            
    label13=Entry(ap,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label13.place(x=90,y= 210)
    label13.insert(0, ' Platform')
    label13.bind("<FocusIn> ",enter)
    label13.bind("<FocusOut> ",leave)

    Frame(ap,width=300,height=2,bg='black').place(x=85,y=230)
    	
    button6=Button(ap,width= 10,height= 1,text= 'Add', border=0,fg=b,bg = 'white',cursor="hand2")
    button6.place(x=180,y=300) 
        
        
def login_page():
    
               
        lp=Tk()
        lp.title('Login')
        lp.geometry('450x400')
    
        b='#9fbdbf'
        Frame(lp,width=450,height=400,bg=b).place(x=0,y=0) 
        label8=Label(lp,text='Login',fg='white',bg=b, font=('Calibri (Body)',25,'bold'))
        label8.place(x =140,y=30)
        
        # entering username
        def enter(e):
            label9.delete(0, 'end')
        def leave(e):
          if label9.get()=="":
             label9.insert(0, 'Username')
             
        label9=Entry(lp,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
        label9.place(x=90,y= 110)
        label9.insert(0, 'Username')
        label9.bind("<FocusIn> ",enter)
        label9.bind("<FocusOut> ",leave)
    
        Frame(lp,width=300,height=2,bg='black').place(x=85,y=132)

        # entering the password
        def enter(e):
          label10.delete(0, 'end')
        def leave(e):
          if label10.get()=="":
            label10.insert(0, 'Password',)
        
        label10=Entry(lp,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
        label10.place(x=90,y= 160)
        label10.insert(0, 'Password')
        label10.bind("<FocusIn> ",enter)
        label10.bind("<FocusOut> ",leave)
    
        Frame(lp,width=300,height=2,bg='black').place(x=85,y=180)

        #buttons
       
        button5=Button(lp,width= 10,height= 1,text= 'Continue',command=main_page, border=0,fg=b,bg = 'white',cursor="hand2")
        button5.place(x=350,y=300) 
        
        button6=Button(lp,width= 10,height= 1,text= 'Back',command=lp.destroy, border=0,fg=a,bg ='white',cursor="hand2")
        button6.place(x=20,y=300) 
   
        
        

def signup_page():
    
   
    sp=Tk()
    sp.title('Signup page')
    sp.geometry('450x400')
    #background colour for sign up page
    b='#9fbdbf'
    Frame(sp,width=450,height=400,bg=b).place(x=0,y=0) 
    label3=Label(sp,text='Sign Up',fg='white',bg=b, font=('Calibri (Body)',25,'bold'))
    label3.place(x =140,y=30)
    
    #user input- username
    def enter(e):
        label4.delete(0, 'end')
    def leave(e):
        if label4.get()=="":
            label4.insert(0, 'Username')
            
    label4=Entry(sp,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label4.place(x=90,y= 110)
    label4.insert(0, 'Username')
    label4.bind("<FocusIn> ",enter)
    label4.bind("<FocusOut> ",leave)
    
    Frame(sp,width=300,height=2,bg='black').place(x=85,y=132)
    
     #user input- password
    def enter(e):
        label5.delete(0, 'end')
    def leave(e):
        if label5.get()=="":
            label5.insert(0, 'Password',)
            
    label5=Entry(sp,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label5.place(x=90,y= 160)
    label5.insert(0, 'Password')
    label5.bind("<FocusIn> ",enter)
    label5.bind("<FocusOut> ",leave)
    
    Frame(sp,width=300,height=2,bg='black').place(x=85,y=180)
    
    
    
    #user input- confirm password
    def enter(e):
        label6.delete(0, 'end')
    def leave(e):
        if label6.get()=="":
            label6.insert(0, ' Confirm Password')
            
    label6=Entry(sp,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label6.place(x=90,y= 210)
    label6.insert(0, ' Confirm Password')
    label6.bind("<FocusIn> ",enter)
    label6.bind("<FocusOut> ",leave)
    
    Frame(sp,width=300,height=2,bg='black').place(x=85,y=230)
    
    
    #buttons
    
    def hover_effect(e):
        button2["bg"]= "#295154"
    
    def leave_hover_effect(e):
        button2["bg"]="White"  



    button2=Button(sp,width= 10,height= 1,text= 'Continue',command=main_page, border=0,fg=b,bg = 'white',cursor="hand2")
    button2.place(x=350,y=300) 
    button2.bind("<Enter>",hover_effect )
    button2.bind("<Leave>",leave_hover_effect )
    
    button4=Button(sp,width= 10,height= 1,text= 'Back',command=sp.destroy, border=0,fg=a,bg ='white',cursor="hand2")
    button4.place(x=20,y=300) 
   
    
   
    
    
    
        
    
#style for the loading bar in the welcome page
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='blue', background='#210b47')
progress=Progressbar(window,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=1000,mode='determinate',)
    
def Progress_bar():

    label2=Label(window,text='Loading...',fg='white',bg=a, font=('Calibri (Body)',10))
    label2.place(x=20,y=360)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        window.update_idletasks()
        time.sleep(0.02)
        r=r+1
    
    
    signup_page()
   
        
#positioN  of the loading bar    
progress.place(x=-50,y=390)

#login button
def hover_effect(e):
    button1["bg"]= "#295154"
    
def leave_hover_effect(e):
    button1["bg"]="White"  
      
button1=Button(window,width=10,height=1,text='Sign in',command=Progress_bar,border=0,fg=a,bg='white',cursor="hand2")
button1.place(x=360,y=300)
button1.bind("<Enter>",hover_effect )
button1.bind("<Leave>",leave_hover_effect )





#login button
def hover_effect(e):
    button3["bg"]= "#295154"
    
def leave_hover_effect(e):
    button3["bg"]="White"    

button3=Button(window,width= 10,height= 1,text= 'Login',command=login_page, border=0,fg=a,bg ='white',cursor="hand2")
button3.place(x=20,y=300)

button3.bind("<Enter>",hover_effect )
button3.bind("<Leave>",leave_hover_effect )
  

    
    



window.mainloop()
