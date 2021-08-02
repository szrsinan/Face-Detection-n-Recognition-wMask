from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox

master = Tk()
master.title('Healthy Faces User Login Page')

canvas = Canvas(master)
master.geometry("470x600")
master.resizable(0,0)
canvas.pack()

frame_top = Frame(master, bg='#F59C60')
frame_top.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.05)  
frame_bottom = Frame(master, bg='#F59C60')
frame_bottom.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.92)

memo = Label(frame_top, bg='#F59C60', text = "FACE RECOGNITION FOR COVID-19", font = "Verdana 15 bold", fg='white')
memo.pack()

#info = StringVar(frame_top)
#info.set("Information")
#info_menu = OptionMenu(frame_top, info, "About Us", "Contact Us")
#info_menu.pack(padx=10, pady=10, side = RIGHT)


img = ImageTk.PhotoImage(Image.open("Logo.png"))
panel = Label(frame_bottom, bg='#F59C60', image = img)
panel.pack(fill = "both")


ID_label = Label(frame_bottom, bg='#F59C60', text='Identification Number:')
ID_label.pack()
var_ID = StringVar()
ID = Entry(frame_bottom, bg='#F7CEB2', textvariable=var_ID)
ID.pack(pady=5)

     #username_label = Label(frame_bottom, bg='#F59C60', text='Full Name:')
     #username_label.pack()
     #username = Entry(frame_bottom, bg='#F7CEB2')
     #username.pack(pady=5)
#username.insert(0, 'Name and Surname')
#username.configure(state=DISABLED)
#def on_click(event):
    #username.configure(state=NORMAL)
    #username.delete(0, END)
#username.bind("<Button-1>", on_click)

password_label = Label(frame_bottom, bg='#F59C60', text='Password:')
password_label.pack()
var_password=StringVar()
password = Entry(frame_bottom, bg='#F7CEB2', show='*', textvariable=var_password)
password.pack(pady=5)
#password.insert(0, 'Password')
#password.configure(state=DISABLED)
#def on_click(event):
    #password.configure(state=NORMAL, show='*')
    #password.delete(0, END)   
#password.bind("<Button-1>", on_click)


def login():
    if var_ID.get() == "" or var_password.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else :
        try:
            con = pymysql.connect(host = "localhost", user = "root", password="", database = "senior_project")
            cur = con.cursor()
            cur.execute("select * from user where identification = %s and password = %s", (var_ID.get(), var_password.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid ID number and password")
            else:
                master.destroy()
                execfile('UserPage.py')

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}")


#def user_page():
    #master.destroy()
    #execfile('UserPage.py')
signInButton = Button(frame_bottom, text = 'Sign In', command=login, bd='12', bg='#38BEF3')
signInButton.pack(pady=10)
  
def user_register():
    master.destroy()
    execfile('UserRegister.py')
registerButton = Button(frame_bottom, text = 'Register', command=user_register, bd='10', bg='#38BEF3')
registerButton.pack(pady=5)



   
        




master.mainloop() 
