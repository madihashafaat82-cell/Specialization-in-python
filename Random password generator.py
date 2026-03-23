from tkinter import *

window = Tk()
window.title('My Website')
window.geometry('700x700')

# 1. Greeting Label
greeting = Label(window, text='This is the website in which you enter a password and then win rewards.')
greeting.pack(pady=20)

# 2. Input Label
Label(window, text="Niche apna password likhein:").pack()

# 3. Password Entry (Jahan user likhega)
password_entry = Entry(window, show='*')
password_entry.pack(pady=10)

# 4. Result dikhane ke liye ek khali Label
result_label = Label(window, text="")
result_label.pack(pady=10)

# 5. Button (Abhi is par click karne se kuch nahi hoga kyunke function nahi hai)
submit_btn = Button(window, text="Win Reward!")
submit_btn.pack()

window.mainloop()