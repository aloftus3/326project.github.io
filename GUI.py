from tkinter import*
from tkinter import messagebox as msg
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import search3
import search2
import search1
# !!!! here we would import search1 (some file search1.py that brings results for search1 based on the input of last and first name)
# !!!! here we would import search2 (some file search2.py that brings results for search2 based on the input of state's two-letter code)
from search_modules import*

def main():
    '''This is the main driver to start the whole program of Propublica Sample Searches'''
    
    window = Tk()   # this is the container for GUI 
    
    # customizing the window container
    window.title('   Welcome to ProPublica Sample Searches')
    window.iconbitmap('small_Logo.ico')
    window.geometry('672x600')
    
    # getting the image to be inserted into GUI 
    my_img = ImageTk.PhotoImage(Image.open('GUI_image_.png'))
    
    # creating the instance of the GUI withing the window container
    gui_app = GuiApp(window, my_img)
    
    # activating the GUI window
    window.mainloop()

class GuiApp():
    '''This class is a blueprint for the GUI window'''    
    def __init__(self, parentWindow, topFramePic):
        self.window = parentWindow
        self.topPicture = topFramePic
        self.choice_var = IntVar()
        self.name = StringVar()
        self.state_code = StringVar()

        picture = Label(self.window, image=self.topPicture)
        picture.grid(row=0, columnspan=3, sticky=N)

        label_main = Label(self.window, pady = 10, text='Choose Search Type:', font='Halvetica 16 bold')
        label_main.grid(row=1, columnspan=3)

        rd1 = Radiobutton(self.window, text='1: Search congress member by name (firstname lastname)', variable=self.choice_var, value=1)
        rd1.grid(row=2, column=0, padx=12, sticky=W)

        label1_search1 = Label(self.window, text="\t\tEnter Name: ")
        label1_search1.grid(row=2, column=1, sticky=W)

        entry_name = Entry(self.window, textvariable=self.name, bg="light grey")
        entry_name.grid(row=2, column=2, sticky=W)
        
        label1_eg = Label(self.window, text="   (E.g. Andy Harris)")
        label1_eg.grid(row=3, column=2, sticky=W)

        rd2 = Radiobutton(self.window,text='2: Get list of Congressional representatives for a state', variable=self.choice_var, value=2)
        rd2.grid(row=5, column=0, padx=12, sticky=W)

        label1_search2 = Label(self.window, text="Enter two-letter code for state: ")
        label1_search2.grid(row=5, column=1, pady=15, sticky=W)

        entry_state = Entry(self.window, textvariable=self.state_code, justify=LEFT, bg="light grey")
        entry_state.grid(row=5, column=2, pady=15, sticky=W)
        
        label1_empty = Label(self.window, text="")
        label1_empty.grid(row=6, column=2, sticky=W)

        rd3 = Radiobutton(self.window, text='3: Get historical data on average age in Congress', variable=self.choice_var, value=3)
        rd3.grid(row=7, column=0, padx=12, sticky=W)

        btn_search = Button(self.window, text='Search', bg='red', fg='white', command=self.show_data)
        btn_search.grid(row=9, columnspan=3, pady=5)

        btn_quit = Button(self.window, text="Exit Program", command=self.window.quit)
        btn_quit.grid(row=10, columnspan=3, pady=15)

    def show_data(self):
        '''This method generates the results of the search requested by the user'''
        
        search_num = self.choice_var.get()   #variable to hold the number of the user-chosen search
        
        if search_num == 3:
            search3.run_search3()
                    
        elif search_num == 1:
            name = str(self.name.get())
            result = search1.runSearch1(name)
            if result == None:
                messagebox.showerror("Error","Name Error. Try again.")
                return            
            results = Tk()
            results.title('  Search Results ')
            results.iconbitmap('small_Logo.ico')
            results.resizable(True, True)
            txt_box = Text(results, wrap=WORD)
            txt_box.pack()
                                            
            txt_box.insert(END, result)
               
        elif search_num == 2:
            state_code = str(self.state_code.get())
            result = search2.runSearch2(state_code)
            if result.empty:
                return
            results = Tk()
            results.title('  Search Results ')
            results.iconbitmap('small_Logo.ico')
            results.resizable(True, True)
            txt_box = Text(results, wrap=WORD)
            txt_box.pack()                                            
            txt_box.insert(END, state_code)            
            txt_box.insert(END, result)
        else:
            message = "No input data. Try again."
            msg.showinfo("  Alert!", message)
        

if __name__ == '__main__':
    main()  
    

            