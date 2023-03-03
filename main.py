import tkinter
import os

file_path = "index.json"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
    with open(file_path, "w") as file:
        print("File created")


# Main Menu
main_menu = tkinter.Tk()

add_button = tkinter.Button(main_menu, text="Add")
rev_button = tkinter.Button(main_menu, text="Review")
ind_button = tkinter.Button(main_menu, text="Index")
button0004 = tkinter.Button(main_menu, text="Button 4")

add_button.grid(row=0, column=0, sticky=tkinter.NSEW)
rev_button.grid(row=0, column=1, sticky=tkinter.NSEW)
ind_button.grid(row=1, column=0, sticky=tkinter.NSEW)
button0004.grid(row=1, column=1, sticky=tkinter.NSEW)

main_menu.mainloop()
