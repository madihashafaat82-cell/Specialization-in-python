from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Image')
root.geometry('500x500')

upload = Image.open("image.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root , image=image , height=400 , width=350)
label.place(x =50 , y=0 )
label2 = Label(text='Here is your picture')
label2.place(x=12 , y=30)

root.mainloop()