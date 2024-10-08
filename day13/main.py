from tkinter import *
from tkinter import messagebox
from password_generator import passwd_generator
import pyperclip
import json
import time

LIGHTEST_PURPLE = "#E5D9F2"
BUTTON_COLOR = "#F5EFFF"


# --------------SHOW 'PASSWORD SAVED'------------------------------------------#
def clear_label():
    alert_label.config(text="")


def show_password_is_saved():
    alert_label.config(text="Password saved successfully!", fg="green")
    alert_label.after(2000, clear_label)


# ---------------Alert about password/email entry changed for copy------------#
def show_email_password_avl_for_copy():
    alert_label.config(text="Copy email/pass from the entries!", fg="green")
    alert_label.after(2000, clear_label)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().lower()
    if len(website) != 0:

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                email, passwd = data[website]["email"], data[website]["passwd"]
                email_usr_entry.delete(0, END)
                email_usr_entry.insert(END, string=email)
                password_entry.delete(0, END)
                password_entry.insert(END, passwd)
                show_email_password_avl_for_copy()
        except KeyError:
            messagebox.showerror(
                title="No credentials avialable for Website",
                message=f"Never saved email/password for '{website}' website",
            )
        except FileNotFoundError:
            messagebox.showerror(
                title="No saved passwords yet!",
                message="Try saving a password for the first time!",
            )
    else:
        messagebox.showerror(title="Oops!", message="Cannot search a black website!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def genrate_passwd():
    generated_passwd = passwd_generator.generate_password()
    pyperclip.copy(generated_passwd)
    password_entry.delete(0, END)
    password_entry.insert(END, generated_passwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwd():
    passwd = password_entry.get()
    email_or_usr = email_usr_entry.get()
    website = website_entry.get().lower()
    new_data = {
        website: {
            "email": email_or_usr,
            "passwd": passwd,
        }
    }
    if len(passwd) != 0 and len(website) != 0 and len(email_or_usr) != 0:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details you have entered:\nEmail:\n    {email_or_usr}\nPassword:\n    {passwd}\nIs this okay to save?",
        )
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
                show_password_is_saved()

    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Personal Password Manager")
window.config(padx=50, pady=50, bg=LIGHTEST_PURPLE)


# ------------------------Lables (Names)-------------------#

website_label = Label(text="Website :", bg=LIGHTEST_PURPLE)
website_label.grid(row=1, column=0)

email_usr_label = Label(text="Email/Username :", bg=LIGHTEST_PURPLE)
email_usr_label.grid(row=2, column=0)

password_label = Label(text="Password :", bg=LIGHTEST_PURPLE)
password_label.grid(row=3, column=0)

alert_label = Label(text="", bg=LIGHTEST_PURPLE, fg="green")
alert_label.grid(row=5, column=1, columnspan=2)

# --------------------Entry (input fields)-----------------#

website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_usr_entry = Entry(width=40)
email_usr_entry.insert(END, string="aryaaggarwal301@gmail.com")
email_usr_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

# ----------------------------Buttons----------------------#

generate_pass_button = Button(
    text="Generate Password", command=genrate_passwd, bg=BUTTON_COLOR, width=13
)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_passwd, width=37, bg=BUTTON_COLOR)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(
    text="Search", command=search_password, bg=BUTTON_COLOR, width=13
)
search_button.grid(row=1, column=2)

# ---------------------------Canvas-------------------------#

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=LIGHTEST_PURPLE)
lock_img = PhotoImage(
    file="/home/aryan/Desktop/python/PublicPythonLearning/day13/logo.png"
)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
window.mainloop()
