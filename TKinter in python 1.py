from tkinter import *
Window = Tk()
Window.title('Sample window')
Window.geometry('300x300')

greeting = Label(text = 'Hello',fg = 'green',bg = 'black')
button = Button(text = 'Click on me',fg = 'green',bg = 'black')
entry = Entry( fg = 'blue',bg = 'black',width = 40)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=Window , relief=RAISED, borderwidth=8)
frame.pack()
label = Label(master=frame,text = 'Welcome to your Window')
label.pack()

textbox = Text(fg = 'green',bg ='white')
textbox.pack()