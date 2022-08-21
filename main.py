from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passwordLetters = [random.choice(letters) for _ in range(nr_letters)]
    passwordSymbols = [random.choice(symbols) for _ in range(nr_symbols)]
    passwordNumbers = [random.choice(numbers) for _ in range(nr_numbers)]

    passwordList = passwordLetters + passwordSymbols + passwordNumbers

    random.shuffle(passwordList)

    password = "".join(passwordList)

    print(password)

    passwordEntry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    inputWebsite = websiteEntry.get()
    inputEmail = emailEntry.get()
    inputPassword = passwordEntry.get()

    if len(inputWebsite) == 0 or len(inputPassword) == 0:
        messagebox.showerror(title="Empty", message="Fill out the fields.")
    else:
        isOk = messagebox.askokcancel(title=inputWebsite, message=f"These are the details entered: \nEmail: {inputEmail}"
                               f"\nPassword: {inputPassword} \nIs it ok to save?")
        if isOk:
            with open("data.txt", "a") as dataFile:
                dataFile.write(f"{inputWebsite} | {inputEmail} | {inputPassword} \n")
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)
emailLabel = Label(text="Website:")
emailLabel.grid(row=2, column=0)
passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3, column=0)

# Entries
websiteEntry = Entry(width=35)
websiteEntry.grid(row=1, column=1, columnspan=2)
websiteEntry.focus()
emailEntry = Entry(width=35)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, "benak.alexander@gmail.com")
passwordEntry = Entry(width=21)
passwordEntry.grid(row=3, column=1)

# Buttons
generatePwdButton = Button(text="Generate Password", command=generate)
generatePwdButton.grid(row=3, column=2)
addButton = Button(text="Add", width=36, command=save)
addButton.grid(row=4, column=1, columnspan=2)


window.mainloop()
