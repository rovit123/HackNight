#!C:\Users\user\AppData\Local\Programs\Python\Python38\python.exe
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox  
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image,ImageTk
import prescription as pr
import cv2
import os
import smtplib
import base64

os.environ["TCL_LIBRARY"] = "C:\Python38\Lib\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\Python38\Lib\\tcl\\tk8.6"

window = Tk()
window.title("PRESCRIBER")
window.iconbitmap("ICON pres.ico")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(),window.winfo_screenheight()-50))
window.resizable(0,0)
def cv():
    img = cv2.cvtColor(pr.templete, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(int(img.shape[1]*(window.winfo_screenheight()/float(img.shape[0]))),window.winfo_screenheight() - 50))
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image= img)
    image_frame.ImageTk = img
    image_frame.configure(image = img)
    showid = image_frame.after(10,show)
left_frame = Frame(window)
image_frame = Label(left_frame)
image_frame.grid(row=0,column=0)
left_frame.grid()
middle_frame = Frame(window,width =0.700,highlightcolor='green',highlightbackground='green',highlightthickness=1,height=window.winfo_screenheight()-50)
name_label = Label(middle_frame,text="Name",font=("Arial",15))
name_label.grid(row=1,column=0)
name_entry = Entry(middle_frame,width=50)
name_entry.grid(row=1,column=1)
age_label = Label(middle_frame,text="Age",font=("Arial",15))
age_label.grid(row=5,column=0)
age_entry = Entry(middle_frame,width=50)
age_entry.grid(row=5,column=1)
gen_label = Label(middle_frame,text="Gender",font=("Arial",15))
gen_label.grid(row=10,column=0)
gen_entry = Entry(middle_frame,width=50)
gen_entry.grid(row=10,column=1)
sl_label = Label(middle_frame,text="Serial",font=("Arial",15))
sl_label.grid(row=15,column=0)
sl_entry = Entry(middle_frame,width=50)
sl_entry.grid(row=15,column=1)
count=0
sm_label = Label(middle_frame,text="Symptoms",font=("Arial",15))
sm_label.grid(row=30,column=0)
sm_entry = Entry(middle_frame,width=50)
sm_entry.grid(row=30,column=1)
dia_label = Label(middle_frame,text="Diagnosis",font=("Arial",15))
dia_label.grid(row=35,column=0)
dia_entry = Entry(middle_frame,width=50)
dia_entry.grid(row=35,column=1)
md_label = Label(middle_frame,text="Medicines",font=("Arial",15))
md_label.grid(row=20,column=0)
md_entry = Entry(middle_frame,width=50)
md_entry.grid(row=20,column=1)
ad_label = Label(middle_frame,text="Advice",font=("Arial",15))
ad_label.grid(row=40,column=0)
ad_entry = Entry(middle_frame,width=50)
ad_entry.grid(row=40,column=1)
sig_label = Label(middle_frame,text="Signature",font=("Arial",15))
sig_label.grid(row=45,column=0)
sig_entry = Entry(middle_frame,width=50)
sig_entry.grid(row=45,column=1)
def save():
        pr.save()
        messagebox.showinfo("information","Saved at location : "+os.getcwd())
b8 = Button(middle_frame, text="   SAVE   ",bg='lightgreen', command=save)
b8.config( height = 4, width = 20)
b8.grid(row=50,column=1)
middle_frame.grid(row=0,column=2,stick=E)
right_frame = Frame(window,highlightcolor='red',highlightbackground='green',highlightthickness=1,height=window.winfo_screenheight()-50)
e = Label(right_frame,text="Doctor Mail ID ",font=("Arial",15))
e.grid(row=1,column=0)
e_entry = Entry(right_frame,width=50)
e_entry.grid(row=1,column=1)
f= Label(right_frame,text="Doctor Password ",font=("Arial",15))
f.grid(row=6,column=0)
f_entry = Entry(right_frame,width=50)
f_entry.config(show='*')
f_entry.grid(row=6,column=1)
g= Label(right_frame,text="Patient Mail ID ",font=("Arial",15))
g.grid(row=11,column=0)
g_entry = Entry(right_frame,width=50)
g_entry.grid(row=11,column=1)
right_frame.grid(row=0,column=2,sticky=N)
def attachments():
    file_path = filedialog.askopenfilename()
    return file_path
def send():
    try:
        msg = MIMEMultipart()
        filename=attachments()
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(e_entry.get(),f_entry.get())
        server.sendmail(e_entry.get(),g_entry.get(),text)
        server.close()
        messagebox.showinfo("information","< MAIL SENT >") 
    except:
        messagebox.showwarning("warning","Mail NOT sent. Try again")  
 
b9 = Button(right_frame, text="   SEND   ",bg='lightgreen', command=send)
b9.config( height = 3, width = 20)
b9.grid(row=20,column=1)
def show():
    pr.name(name_entry.get())
    pr.age(age_entry.get())
    pr.gender(gen_entry.get())
    pr.serial(sl_entry.get())
    pr.symptoms(sm_entry.get())
    pr.diagnosis(dia_entry.get())
    pr.medicine(0,md_entry.get(),'',0,1)
    pr.advice(ad_entry.get())
    pr.signature(sig_entry.get())
    cv()
show()
def guide():
    messagebox.showinfo('HELPER',
        '1.Enter the details of each field. Ex: name,age,advice,etc...\n'
        '2.Click on save button after completion of writing prescription.\n'
        '3.Enter mail and click on send button to select file and send.')
def destroy():
    window.destroy()
menubar = Menu(window)
window.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="Guide", command=guide)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=destroy)
window.mainloop()