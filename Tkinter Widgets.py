from tkinter import *
from PIL import Image, ImageTk

# ----------------- Window Setup -----------------
root = Tk()
root.title('My Image Viewer')
root.geometry('550x500')  # thoda wider for nice spacing
root.configure(bg='#f0f0f0')  # soft background color

# ----------------- Load and Resize Image -----------------
# Correct path + resize
upload = Image.open(r"C:\Users\User\Desktop\Codingal\Specialization in python\image.jpg")
upload = upload.resize((400, 400))  # larger image, but fits nicely
image = ImageTk.PhotoImage(upload)

# ----------------- Image Label -----------------
label = Label(root, image=image, bd=2, relief=RIDGE)  # border for subtle styling
label.place(x=75, y=50)  # center horizontally in 550 width window

# ----------------- Text Label -----------------
label2 = Label(root, text='Here is your picture', font=('Helvetica', 16, 'bold'),
               bg='#f0f0f0', fg='#333333')  # soft text color
label2.place(x=150, y=20)  # above image, centered-ish

# ----------------- Optional: Footer Label -----------------
label3 = Label(root, text='Created with Python Tkinter', font=('Arial', 10),
               bg='#f0f0f0', fg='#666666')
label3.place(x=180, y=470)  # bottom of window

# ----------------- Run Window -----------------
root.mainloop()