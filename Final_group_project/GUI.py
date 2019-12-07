from tkinter import*
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import search3
# !!!! here we would import search1 (some file search1.py that brings results for search1 based on the input of last and first name)
# !!!! here we would import search2 (some file search2.py that brings results for search2 based on the input of state's two-letter code)
from search_modules import*


def show_data():
    search_num = choice_var.get()
    if search_num == 3:
        search3.run_search3()
    else:
        results = Tk()
        results.title('  Search Results ')
        results.iconbitmap('small_Logo.ico')
        
        txt_box = Text(results, wrap=WORD).pack()
        txt_box.pack()
        
        if search_num == 1:
            first_name = str(entry_first_name.get())
            last_name = str(entry_last_name.get())
            
            # !!! result = search1.SomeMethod(first_name, last_name)
            # !!! txt_box.insert(END, result)
            
        elif search_num == 2:
            state_code = str(entry_state.get())
            
            # !!! result = search2.SomeMethod(state_code)
            # !!! txt_box.insert(END, result)
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
last_name = StringVar()
first_name = StringVar()
state_code = StringVar()

rd1 = Radiobutton(root, text='1: Search current representative by name', variable=choice_var, value=1)
rd1.grid(row=2, column=0, padx=12, sticky=W)

label1_search1 = Label(root, text="Enter last name: ")
label1_search1.grid(row=2, column=1, sticky=W)

entry_last_name = Entry(root, bg="light grey")
entry_last_name.grid(row=2, column=2, sticky=W)

label2_search1 = Label(root, text="Enter first name: ")
label2_search1.grid(row=3, column=1, sticky=W) 

entry_first_name = Entry(root, bg="light grey")
entry_first_name.grid(row=3, column=2, sticky=W)

rd2 = Radiobutton(root,text='2: Get list of Congressional representatives for a state', variable=choice_var, value=2)
rd2.grid(row=5, column=0, padx=12, sticky=W)

label1_search2 = Label(root, text="Enter two-letter code for state: ")
label1_search2.grid(row=5, column=1, pady=15, sticky=W)

entry_state = Entry(root, justify=LEFT, bg="light grey")
entry_state.grid(row=5, column=2, pady=15, sticky=W) 

rd3 = Radiobutton(root, text='3: Get historical data on average age in Congress', variable=choice_var, value=3)
rd3.grid(row=7, column=0, padx=12, sticky=W)

btn_search = Button(root, text='Search', bg='red', fg='white', command=show_data)
btn_search.grid(row=8, columnspan=3, pady=5)

btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_quit.grid(row=9, columnspan=3, pady=15)

root.mainloop()
