import re
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
numbers = "1234567890"

def generate_password():
    password = ''.join(random.choice(letters + symbols + numbers) for _ in range(12))
    entry_password.delete(0, tk.END)
    entry_password.insert(tk.END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = re.sub(r'[ /]', '', entry_website.get())
    email = re.sub(r'[ /]', '', entry_email_uname.get())
    password = entry_password.get()

    if len(password) < 6:
        messagebox.showinfo(title="Oops", message="Password should be at least 6 characters long.")
        return

    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        entry_website.delete(0, tk.END)
        entry_email_uname.delete(0, tk.END)
        entry_password.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1, pady=5)

entry_website = tk.Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW", pady=5)

label_email_uname = tk.Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2, pady=5)

entry_email_uname = tk.Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW", pady=5)
entry_email_uname.insert(0, "fGpRd@example.com")

label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3, pady=5)

entry_password = tk.Entry()
entry_password.grid(column=1, row=3, sticky="EW", pady=5)

generate_btn = tk.Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW", pady=5)

add_btn = tk.Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW", pady=5)

window.mainloop()
