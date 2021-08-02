from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pymysql 


master3 = Tk()
master3.title('Healthy Faces User Register Page')

canvas = Canvas(master3) 
master3.geometry("470x750")
master3.resizable(0,0)
canvas.pack()

frame_top = Frame(master3, bg='#F59C60')
frame_top.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.05)  
frame_bottom = Frame(master3, bg='#F59C60')
frame_bottom.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.92)

memo = Label(frame_top, bg='#F59C60', text = "FACE RECOGNITION FOR COVID-19", font = "Verdana 15 bold", fg='white')
memo.pack()

#info = StringVar(frame_top)
#info.set("Information")
#info_menu = OptionMenu(frame_top, info, "About Us", "Contact Us")
#info_menu.pack(padx=10, pady=10, side = RIGHT)

#kamera sadece snapShot! alıyor ve dosyaya kaydediyor. Register için yeterli, Login olurken scan lazım...

#def camReg():
#    execfile('Camera4Reg.py')



#videoButtonReg = Button(frame_bottom, text = 'Open the Camera', command=camReg, bd='10', bg='#38BEF3')
#videoButtonReg.pack(pady=75)
cam_label = Label(frame_bottom, bg='#F59C60', text='Camera Shot is MANDATORY !!! \n After filling registration information, \n the camera will open when you perform \n Submit Button',font = 'Verdana 15 bold', fg='red')
cam_label.pack()


username_label = Label(frame_bottom, bg='#F59C60', text='Full Name:')
username_label.pack()
var_username = StringVar()
username = Entry(frame_bottom, bg='#F7CEB2', textvariable=var_username)
username.pack(pady=5)
#username.insert(0, 'Name and Surname')
#username.configure(state=DISABLED)
#def on_click(event):
    #username.configure(state=NORMAL)
    #username.delete(0, END)
#username.bind("<Button-1>", on_click)



gender_label = Label(frame_bottom, bg='#F59C60', text='Select Your Gender:')
gender_label.pack()
combo_box = StringVar()
combo_box=ttk.Combobox(frame_bottom, state = 'readonly', justify = CENTER)
combo_box['values'] = ("Select", "Male", "Female")
combo_box.current(0)
combo_box.pack()

#radioButton = IntVar()
#radioButton.set(0)       
#male = Radiobutton(frame_bottom, text="Male", value=1, variable=radioButton, bg="#F59C60")
#male.pack()
#female = Radiobutton(frame_bottom, text="Female", value=2, variable=radioButton, bg="#F59C60")
#female.pack()

bday_label = Label(frame_bottom, bg='#F59C60', text='Birthdate:')
bday_label.pack()
var_bday = StringVar()
bday = DateEntry(frame_bottom, width=12, background='orange', foreground='black', borderwidth=1, locale="de_DE", textvariable=var_bday)
bday._top_cal.overrideredirect(False)
bday.pack(pady=5)

ID_label = Label(frame_bottom, bg='#F59C60', text='Identification Number:')
ID_label.pack()
var_ID = StringVar()
ID = Entry(frame_bottom, bg='#F7CEB2', textvariable=var_ID)
ID.pack(pady=5)
#ID.insert(0, 'Identification Number')
#ID.configure(state=DISABLED)
#def on_click(event):
    #ID.configure(state=NORMAL)
    #ID.delete(0, END)
#ID.bind("<Button-1>", on_click)

phone_label = Label(frame_bottom, bg='#F59C60', text='Phone Number:')
phone_label.pack()
var_phone = StringVar()
phoneNum = Entry(frame_bottom, bg='#F7CEB2', textvariable=var_phone)
phoneNum.pack(pady=5)
#phoneNum.insert(0, 'Phone Number')
#phoneNum.configure(state=DISABLED)
#def on_click(event):
    #phoneNum.configure(state=NORMAL)
    #phoneNum.delete(0, END)
#phoneNum.bind("<Button-1>", on_click)

password_label = Label(frame_bottom, bg='#F59C60', text='Password:')
password_label.pack()
var_password=StringVar()
password = Entry(frame_bottom, bg='#F7CEB2', textvariable=var_password)
password.pack(pady=5)
#password.insert(0, 'Password')
#password.configure(state=DISABLED)
#def on_click(event):
password.configure(state=NORMAL, show='*')
#password.delete(0, END)   
#password.bind("<Button-1>", on_click)



    
def register_data(): 

     if var_username.get() == "" or combo_box.get() == "Select" or var_bday.get() == "" or var_ID.get() == "" or var_phone.get() == "" or var_password.get() == "":
         messagebox.showerror("Error", "All Fields Are Required")       
     else:
         try:
             con = pymysql.connect(host = "localhost",user = "root", password ="", database = "senior_project")
             cur = con.cursor()
             cur.execute("insert into user (full_name, gender, birthdate, identification, phone, password) values(%s, %s, %s, %s, %s, %s)", 
                              (var_username.get(),
                              combo_box.get(),
                              var_bday.get(),
                              var_ID.get(),
                              var_phone.get(),
                              var_password.get()
                              ))
             con.commit()
             con.close()
             master3.destroy()
             execfile('Camera4Reg.py')


         except Exception as es:
             messagebox.showerror("Error", f"Error due to: {str(es)}")


     
     

submit = Button(frame_bottom, text = 'Submit', command=register_data, bd='12', bg='#38BEF3')
submit.pack(pady=10)














master3.mainloop() 
