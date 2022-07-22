from distutils.cmd import Command
from logging import root
from msilib import sequence
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from turtle import back, onclick
import tkinter as tk
import sqlite3
import bcrypt
# SQLITE was used since it is easy to use and simple enough for this project.


# USER PROFILE DATABASE
# connect_userProfile = sqlite3.connect('User profile.db')    # Connecting database file to python file

# Initiating the database for the application
with sqlite3.connect("PassWordStorageApp.db") as db:
    myCursor = db.cursor()


myCursor.execute("""
    CREATE TABLE IF NOT EXISTS userProfileTable(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL);
""")

# Creating the window
window = Tk()
window.update()
window.title("Password Storage Application")
window.geometry('450x400')

a = '#9fbdbf'
Frame(window, width=450, height=400, bg=a).place(x=0, y=0)
label1 = Label(window,text='WELCOME...', fg='white',bg=a, font=('Calibri (Body)', 18, 'bold'))
label1.place(x=50, y=80)


# Function to create SignUp Page
def signup_page():

    # To create page in same window
    for widget in window.winfo_children():
        widget.destroy()

    b='#9fbdbf'
    Frame(window, width=450,height=400,bg=b).place(x=0,y=0)
    label3 = Label(window,text='Sign Up',fg='white',bg=b, font=('Calibri (Body)',25,'bold'))
    label3.place(x =140,y=30)

    # user input- username
    def enter(e):
        label4.delete(0, 'end')

    def leave(e):
        if label4.get() == "":
            label4.insert(0, 'Username')

    label4=Entry(window,width=30, fg='black', border=0, bg='#9fbdbf',font=('Calibri (Body)',12))
    label4.place(x=90, y=110)
    label4.insert(0, 'Username')
    label4.bind("<FocusIn> ", enter)
    label4.bind("<FocusOut> ", leave)

    Frame(window, width=300, height=2, bg='black').place(x=85, y=132)

    # user input - password
    def enter(e):
        label5.delete(0, 'end')

    def leave(e):
        if label5.get() == "":
            label5.insert(0, 'Password',)


    label5 = Entry(window, width= 30, fg='black', border=0, bg='#9fbdbf', font=('Calibri (Body)', 12))
    label5.place(x=90, y=160)
    label5.insert(0, 'Password')
    label5.bind("<FocusIn> ", enter)
    label5.bind("<FocusOut> ", leave)
    Frame(window, width=300, height=2, bg='black').place(x=85, y=180)

    # user input- confirm password
    def enter(e):
        label6.delete(0, 'end')

    def leave(e):
        if label6.get() == "":
            label6.insert(0, ' Confirm Password')


    label6 = Entry(window, width= 30, fg='black', border=0,bg='#9fbdbf', font=('Calibri (Body)', 12))
    label6.place(x=90,y= 210)
    label6.insert(0, ' Confirm Password')
    label6.bind("<FocusIn> ", enter)
    label6.bind("<FocusOut> ", leave)

    def confirm_password(): # Confirming password
        username = label4.get()
        pass1 = label5.get()
        pass2 = label6.get()
        if pass1 == pass2:
            myCursor.execute("DELETE FROM userProfileTable WHERE id = 1")

            bytePwd = pass1.encode('utf-8')
            # Generate salt
            # Generate a separate salt for each for better security
            my_salt = bcrypt.gensalt()

            # Hash password
            hashed_password = bcrypt.hashpw(bytePwd, my_salt)
            print(hashed_password)
            print("Password validation successful")

            # Inserting user information to the DB
            myCursor.execute("INSERT INTO userProfileTable(id, username,password,salt) VALUES(?,?,?,?)", (1, username, hashed_password, my_salt))
            db.commit()

            main_page()
        else:
            label8 = Label(window, text='Password does not match!', fg='white', bg=b, font=('Calibri (Body)', 10, 'bold'))
            label8.place(x=90, y=250)

    Frame(window,width=300, height=2, bg='black').place(x=85,y=230)


    def hover_effect(e):
        button2["bg"] = "#295154"

    def leave_hover_effect(e):
        button2["bg"] ="White"

    button2=Button(window,width= 10,height= 1,text= 'Continue', command=confirm_password, border=0,fg=b,bg = 'white',cursor="hand2")
    button2.place(x=350,y=300)
    button2.bind("<Enter>",hover_effect )
    button2.bind("<Leave>",leave_hover_effect )

    button4=Button(window,width= 10,height= 1,text= 'Back', command=window.destroy, border=0,fg=a,bg ='white',cursor="hand2")
    button4.place(x=20,y=300)


# Function to display main dashboard
def main_page():
    for widget in window.winfo_children():
        widget.destroy()

    b = '#9fbdbf'
    Frame(window, width=450, height=400, bg=b).place(x=0, y=0)

    # Table creation
    table = ttk.Treeview(window)
    table['columns']= ("Username", "Password", "Description")

    #formatting  the column
    table.column('#0', width=120, minwidth=25)
    table.column("Username", anchor=W,width=120)
    table.column("Password",anchor=CENTER,width= 80)
    table.column("Description", anchor=W , width=120)

    #headings

    table.heading("#0",text="ID",anchor=W)
    table.heading("Username",text="Username",anchor=W)
    table.heading("Password",text="Password", anchor=CENTER)
    table.heading("Description", text="Platform",anchor=W)

    # Sample Data
    table.insert(parent='',index='end',iid=0,text="1",values=("Dhinuk","1234","Hi"))
    table.pack(pady=20)

    # Buttons
    button7 = Button(window,width= 10,height= 1,text= 'Add',command=addbutton_page, border=0,fg=b,bg = 'white',cursor="hand2")
    button7.place(x=350,y=250)

    button8 = Button(window,width= 10,height= 1,text= 'Modify',command=main_page, border=0,fg=b,bg = 'white',cursor="hand2")
    button8.place(x=350,y=300)

    button9 = Button(window,width= 10,height= 1,text= 'Remove',command=main_page, border=0,fg=b,bg = 'white',cursor="hand2")
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

    for widget in window.winfo_children():
        widget.destroy()

    b='#9fbdbf'
    Frame(window,width=450,height=400,bg=b).place(x=0,y=0)
    label8 = Label(window,text='Login',fg='white',bg=b, font=('Calibri (Body)',25,'bold'))
    label8.place(x=140, y=30)

    # entering username
    def enter(e):
        label9.delete(0, 'end')
    def leave(e):
        if label9.get() == "":
            label9.insert(0, 'Username')

    label9=Entry(window,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label9.place(x=90,y= 110)
    label9.insert(0, 'Username')
    label9.bind("<FocusIn> ",enter)
    label9.bind("<FocusOut> ",leave)

    Frame(window,width=300,height=2,bg='black').place(x=85,y=132)

    # entering the password
    def enter(e):
        label10.delete(0, 'end')

    def leave(e):
        if label10.get() == "":
            label10.insert(0, 'Password',)

    label10=Entry(window,width= 30, fg='black', border=0,bg='#9fbdbf',font=('Calibri (Body)',12))
    label10.place(x=90,y= 160)
    label10.insert(0, 'Password')
    label10.bind("<FocusIn> ",enter)
    label10.bind("<FocusOut> ",leave)

    Frame(window,width=300,height=2,bg='black').place(x=85,y=180)

    # Function to validate Login Password
    def PassValidation():
        logname = label9.get()
        userpass = label10.get()
        bytePwd1 = userpass.encode('utf-8')
        # Generate salt
        # Generate a separate salt for each for better security
        mySalt = bcrypt.gensalt()

        # Hash password
        hashedPassword1 = bcrypt.hashpw(bytePwd1, mySalt)

        myCursor.execute("SELECT * FROM userProfileTable")
        check = myCursor.fetchall()
        for i in check:
            if logname == i[0] and hashedPassword1 == i[1]: # Checking DB
                main_page()
            else:
                # Label to print Incorrect password or username
                label4=Label(window,text='Incorrect User Name Or Password',fg='white',bg=b, font=('Calibri (Body)',10,'bold'))
                label4.place(x =90,y=200)
                #buttons

    button5=Button(window,width= 10,height= 1,text= 'Continue',command=PassValidation, border=0,fg=b,bg = 'white',cursor="hand2")
    button5.place(x=350,y=300)

    button6=Button(window, width= 10, height= 1, text= 'Back', command=window.destroy, border=0, fg=a, bg ='white', cursor="hand2")
    button6.place(x=20,y=300)













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