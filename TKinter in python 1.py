from tkinter import *

window = Tk()
window.title('Elite GUI Panel')
window.geometry('320x320')
window.configure(bg='#0f172a')   # deep navy background

# ----- Widgets -----
greeting = Label(
    text='Hello',
    fg='#e2e8f0',
    bg='#0f172a',
    font=('Segoe UI', 14, 'bold')
)

button = Button(
    text='Click on me',
    fg='white',
    bg='#2563eb',
    activebackground='#1d4ed8',
    relief='flat',
    padx=10,
    pady=5
)

entry = Entry(
    fg='#111827',
    bg='#e5e7eb',
    width=35,
    relief='flat',
    font=('Segoe UI', 10)
)

greeting.pack(pady=10)
entry.pack(pady=8)
button.pack(pady=8)

frame = Frame(
    master=window,
    relief=RAISED,
    borderwidth=0,
    bg='#1e293b'
)
frame.pack(pady=15, padx=10, fill='x')

label = Label(
    master=frame,
    text='Welcome to your Window',
    fg='#f1f5f9',
    bg='#1e293b',
    font=('Segoe UI', 10)
)
label.pack(pady=6)

textbox = Text(
    fg='#111827',
    bg='#f8fafc',
    height=6,
    width=35,
    relief='flat',
    font=('Consolas', 10)
)
textbox.pack(pady=8)

window.mainloop()