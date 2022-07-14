
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title("Applied Cryptography")
window.geometry('450x400')
a='#940721'
Frame(window,width=450,height=400,bg=a).place(x=0,y=0) 

label1=Label(window,text='WELCOME...',fg='white',bg=a,font=('Calibri (Body)',18,'bold'))
label1.place(x=50,y=80)


def login_page():
        
        lp=Tk()
        lp.title('Login')
        lp.geometry('450x400')
    #background colour for sign up page
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
        lp.mainloop()
         

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
    
    #user input- password
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
    
    label7=Label(sp,text='Already have an account?',fg='white',bg=b, font=('Calibri (Body)',8))
    label7.place(x=140,y=310)
    
    

    #button for sign up
    def hover_effect(e):
        button2["bg"]= "#295154"
    
    def leave_hover_effect(e):
        button2["bg"]="White"  

    button2=Button(sp,width= 20,height= 1,text= 'Sign in', border=0,fg=b,bg = 'white')
    button2.place(x=150,y=275) 
    button2.bind("<Enter>",hover_effect )
    button2.bind("<Leave>",leave_hover_effect )
    
   
    
   
    
    
    
        
    
#style for the loading bar
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
    
    window.destroy()
    signup_page()
   
        
#positioN  of the loading bar    
progress.place(x=-50,y=390)

#get started button
def hover_effect(e):
    button1["bg"]= "#295154"
    
def leave_hover_effect(e):
    button1["bg"]="White"  
      
button1=Button(window,width=20,height=1,text='Get started',command=Progress_bar,border=0,fg=a,bg='white')
button1.place(x=300,y=350)
button1.bind("<Enter>",hover_effect )
button1.bind("<Leave>",leave_hover_effect )

def Progress_bar2():

    label2=Label(window,text='Loading...',fg='white',bg=a, font=('Calibri (Body)',10))
    label2.place(x=20,y=360)
    
    import time
    r=0
    for i in range(100):
        progress1['value']=r
        window.update_idletasks()
        time.sleep(0.02)
        r=r+1
    
    window.destroy()
    login_page()
    

button3=Button(window,width= 5,height= 1,text= 'Login',command=login_page, border=0,fg=a,bg ='white',cursor="hand2")
button3.place(x=275,y=310)
   





    
    

    

window.mainloop()

