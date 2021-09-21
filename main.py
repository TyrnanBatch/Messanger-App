import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sys

# I will Put My cursor Here if im alt tabed:

# Create Tk window as 'root'
root = tk.Tk()

# Setting root settings (size, name, extra)
root.geometry('200x250')
root.configure(width=1600, height=900)
root.title('Messenger App')
root.configure(bg='light blue') # '#5e5a5a'

winWidth = root.winfo_reqwidth()
winHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winHeight / 2)
root.geometry("+{}+{}".format(posRight, posDown))

class Contacts():
    def Open(Name):
        print(Name) # Open the thing where they can see last msg and send msgs to person of "Name" - Maybe serch for an id attached to the Name?


def exit():
    sys.exit()


def settings():
    print("Settings")


def MainMenu():
    global root

    for widget in root.winfo_children():
        widget.destroy()

    root.title('Messenger App - Main Menu')

    Space = tk.Label(root, text="", bg='light blue')
    Space.pack()

    MainMenuTitle = tk.Label(root, text="Messenger App" , bg='light blue')
    MainMenuTitle.pack()

    Space = tk.Label(root, text="", bg='light blue')
    Space.pack()

    OpenButton = tk.Button(root, text="Open Messenger", command=MessageMenu)
    OpenButton.pack()

    Space = tk.Label(root, text="", bg='light blue')
    Space.pack()

    SettingsButton = tk.Button(root, text="Settings", command=settings)
    SettingsButton.pack()

    Space = tk.Label(root, text="", bg='light blue')
    Space.pack()

    ExitButton = tk.Button(root, text="Exit", command=exit)
    ExitButton.pack()


def MessageMenu():
    global root

    for widget in root.winfo_children():
        widget.destroy()

    root.title('Messenger App - Messenger')
    root.geometry('500x500')

    message_submit_button = tk.Button(root)
    message_submit_button.grid(row=5, column=3)

    message_entry = tk.Entry(root)
    message_entry.grid(row=5, column=2)

    columns = ('#1')

    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('#1', text='Contacts:')

    # generate sample data
    contacts = ['Bob','Jake','Tin_man']


    # adding data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    # bind the select event
    def item_selected(event):
        for selected_item in tree.selection():
            # dictionary
            item = tree.item(selected_item)
            # list
            record = item['values']
            #
            Contacts.Open(record)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=1, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')


# Main Loop

if __name__ == "__main__":
    MainMenu()

root.mainloop()

