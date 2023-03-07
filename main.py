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

# Add window
def open_add_window():
    add_window = tkinter.Toplevel(main_menu)

    def close_add_window():
        add_window.destroy()
        main_menu.deiconify()

    add_window_close_button = tkinter.Button(
        add_window, text="Close", command=close_add_window)
    add_window_close_button.pack()

    main_menu.withdraw()
    add_window.wait_window()


# Main Menu Buttons
add_button = tkinter.Button(
    main_menu, height=3, width=10, text="Add", command=open_add_window)
rev_button = tkinter.Button(main_menu, height=3, width=10, text="Review")
ind_button = tkinter.Button(main_menu, height=3, width=10, text="Index")
button0004 = tkinter.Button(main_menu, height=3, width=10, text="Button 4")

add_button.grid(row=0, column=0)
rev_button.grid(row=0, column=1)
ind_button.grid(row=1, column=0)
button0004.grid(row=1, column=1)

main_menu.rowconfigure(0, weight=1)
main_menu.rowconfigure(1, weight=1)
main_menu.columnconfigure(0, weight=1)
main_menu.columnconfigure(1, weight=1)

main_menu.mainloop()
