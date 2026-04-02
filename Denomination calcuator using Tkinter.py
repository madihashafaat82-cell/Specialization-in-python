from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='skyblue')
root.geometry('650x450')

upload = Image.open('app_img.jpg')
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image , bg='skyblue')
label.place(x=180 , y=20)

label1 = Label(root , text="Hi,Welcome to Denomination counter application." , bg='skyblue')
label1.place(relx=0.5 , y=340 , anchor=CENTER)

def msg():
    messagebox.showinfo(
        'Alert','Do you want to calculate the Domination count?'
    )
    topwin()

# FIX: command added
button1 = Button(root , text='Lets get started' , bg='brown' , fg='white', command=msg)
button1.place(x=260 , y=360)

def topwin():
   top = Toplevel(root)
   top.configure(bg='grey')
   top.geometry('600x400')

   # FIX: new widgets defined (previously undefined)
   label2 = Label(top, text="Enter Amount", bg='grey')
   entry = Entry(top)
   btn = Button(top, text="Submit")
   lbl = Label(top, text="Result", bg='grey')

   l1 = Label(top, text="L1", bg='grey')
   l2 = Label(top, text="L2", bg='grey')
   l3 = Label(top, text="L3", bg='grey')

   t1 = Label(top, text="", bg='grey')
   t2 = Label(top, text="", bg='grey')
   t3 = Label(top, text="", bg='grey')

   # FIX: do NOT reuse old label → use label2
   label2.place(x=230 , y=50)
   entry.place(x=200 , y=80)
   btn.place(x=240 , y=120)
   lbl.place(x=140 , y=170)

   l1.place(x=180 , y=200)
   l2.place(x=180 , y=230)
   l3.place(x=180 , y=260)

   t1.place(x=270 , y=200)
   t2.place(x=270 , y=230)
   t3.place(x=270 , y=260)

   # FIX: removed top.mainloop()

root.mainloop()