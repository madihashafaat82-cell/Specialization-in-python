import tkinter as tk
import random, string

# Main Window setup
root = tk.Tk()
root.title("Quick Pass")
root.geometry("300x150")

# Password display ke liye label
display = tk.Label(root, text="Click Generate", font=("Courier", 14, "bold"), pady=10)
display.pack()

# Characters ka pool (Short code)
pool = string.ascii_letters + string.digits + "@#$%"

# "GENERATE" Button: Lambda function ke saath (Single Line Logic)
tk.Button(root, text="GENERATE", bg="blue", fg="white", font=("Arial", 10, "bold"),
          command=lambda: display.config(text="".join(random.sample(pool, 12)), fg="green")
          ).pack(pady=20)

root.mainloop()