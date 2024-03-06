from tkinter import *
from tkinter import ttk, font
import getpass
import shutil
import os
import description

# Colors
color1 = "#F9F7F7"
color2 = "#DBE2EF"
color3 = "#3F72AF"
color4 = "#112D4E"


def deleteFolders():
    username = getpass.getuser()
    pathToExotic = fr"C:\Users\{username}\AppData\Local\Exotic"
    if os.path.exists(pathToExotic):
        shutil.rmtree(pathToExotic, ignore_errors=True)
    else:
        print("Path does not exist!")


# Window config
app = Tk()
app.geometry("600x400")
app.resizable(False, False)
app.title("Visual Studio Code Cleaner")
app.configure(bg=color1)
app.iconbitmap("./images/icon1.ico")

# Fonts
interBoldFont = font.Font(family="Inter", size=28, weight="bold")
interRegularFont = font.Font(family="Inter", size=12, weight="normal")

# Title
titleLbl = ttk.Label(master=app, text="Visual Studio Code Cleaner", font=interBoldFont,
                     background=color1, foreground=color4)
titleLbl.grid(row=0, column=0, columnspan=2)

# Center the title label horizontally
app.update_idletasks()
labelWidth = titleLbl.winfo_reqwidth()
appWidth = app.winfo_width()
xPosition = (appWidth - labelWidth) // 2

# Adjust the column weights to make the title label centered
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
titleLbl.grid_configure(sticky="n", padx=xPosition)

# Description
descLbl = ttk.Label(master=app, text=description.descriptionTxt, font=interRegularFont, background=color1,
                    wraplength=570, justify="center")
descLbl.grid(row=1, column=0, columnspan=2, pady=20)  # Added pady for spacing

# Warning label
warningLbl = ttk.Label(master=app, text=description.warningTxt, font=interRegularFont, background=color1,
                       wraplength=570, justify="center", foreground="red")
warningLbl.grid(row=2, column=0, columnspan=2, pady=15)

# Clear button
clearBtn = ttk.Button(master=app, text="Clean", command=deleteFolders)
clearBtn.grid(row=3, column=0, columnspan=2, pady=1)  # Added pady for spacing

# App loop
app.mainloop()
