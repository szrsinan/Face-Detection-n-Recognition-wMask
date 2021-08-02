from os import name
from tkinter import *
import pymysql
import tkinter as tk
from tkinter import ttk

from pymysql.cursors import Cursor

master2 = Tk()
master2.title('Healthy Faces User Page')

canvas = Canvas(master2)
master2.geometry("470x600")
master2.resizable(0,0)
canvas.pack()

frame_top = Frame(master2, bg='#F59C60')
frame_top.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.05)  
frame_bottom = Frame(master2, bg='#F59C60')
frame_bottom.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.92)

memo = Label(frame_top, bg='#F59C60', text = "FACE RECOGNITION FOR COVID-19", font = "Verdana 15 bold", fg='white')
memo.pack()

def fetch_data():
    con = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'senior_project')
    cur = con.cursor()
    cur.execute("select full_name,gender,birthdate,identification,phone,HealthStatus from user")
    rows = cur.fetchall()
    for row in rows:
        fName= row[1]
        username_label = Label(frame_bottom, bg='#F59C60', text='Full Name:',textvariable=fName )
        username_label.pack(pady=10)
        gender= row[2]
        Bdate =row[3]
        id= row[4]
        phone= row[5]
        Health= row[6]
        print("fname = %s,gender = %s,Bdate = %d,id = %s, phone=%s,Health=%s" % \
        (fName, gender, Bdate, id,phone,Health ))

    
    cur.close()
    con.close()
    

gender_label = Label(frame_bottom, bg='#F59C60', text='Gender:')
gender_label.pack(pady=10)

bday_label = Label(frame_bottom, bg='#F59C60', text='Birthdate:')
bday_label.pack(pady=10)

ID_label = Label(frame_bottom, bg='#F59C60', text='Identification Number:')
ID_label.pack(pady=10)

phone_label = Label(frame_bottom, bg='#F59C60', text='Phone Number:')
phone_label.pack(pady=10)

risk_label = Label(frame_bottom, bg='#F59C60', text='Health Status:', font = "Verdana 15 bold", fg='white')
risk_label.pack(pady=80)


def user_login():
    master2.destroy()
    execfile('UserLogin.py')
mainButton = Button(frame_bottom, text = 'Main Page', command=user_login, bd='10', bg='#38BEF3')
mainButton.pack(pady=5)



master2.mainloop() 
