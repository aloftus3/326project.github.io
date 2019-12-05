from tkinter import*
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import search3
from search_modules import*

def show_data():
    search_num = choice_var.get()
    if search_num == 3:
        search3.run_search3()
    else:
        results = Tk()
        results.title('  Search Results ')
        results.iconbitmap('small_Logo.ico')
        results.geometry('580x580')
        txt_box = Text(results, width=500, height=350, wrap=WORD).grid(row=1)

        if search_num == 2:
            pass

        elif search_num == 1:
            pass

        else:
            pass

root = Tk()
root.title('   Welcome to ProPublica Sample Searches')
root.iconbitmap('small_Logo.ico')

root.geometry('672x580')

my_img = ImageTk.PhotoImage(Image.open('GUI_image_.png'))
picture = Label(image=my_img)
picture.grid(row=0, columnspan=3, sticky=N)

label_main = Label(root, pady = 10, text='Choose search type', font='Halvetica 16 bold')
label_main.grid(row=1, columnspan=3)

choice_var = IntVar()

rd1 = Radiobutton(root, text='1: Search current representative by name', variable=choice_var, value=1)
rd1.grid(row=2, column=0, padx=12, sticky=W)
label1_search1 = Label(root, text="Enter last name: ").grid(row=2, column=1, sticky=W)
entry_last_name = Entry(root, bg="light grey").grid(row=2, column=2, sticky=W)
label2_search1 = Label(root, text="Enter first name: ").grid(row=3, column=1, sticky=W)
entry_state = Entry(root, bg="light grey").grid(row=3, column=2, sticky=W)

rd2 = Radiobutton(root,text='2: Get list of Congressional representatives for a state', variable=choice_var, value=2)
rd2.grid(row=5, column=0, padx=12, sticky=W)
label1_search2 = Label(root, text="Enter two-letter code for state: ").grid(row=5, column=1, pady=15, sticky=W)
entry_state = Entry(root, justify=LEFT, bg="light grey").grid(row=5, column=2, pady=15, sticky=W)

rd3 = Radiobutton(root, text='3: Get historical data on average age in Congress', variable=choice_var, value=3)
rd3.grid(row=7, column=0, padx=12, sticky=W)

btn_search = Button(root, text='Search', bg='red', fg='white', command=show_data)
btn_search.grid(row=8, columnspan=3, pady=5)

btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_quit.grid(row=9, columnspan=3, pady=15)

root.mainloop()
