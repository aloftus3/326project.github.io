# ProPublica Search Engine

The ProPublica Search Engine addresses the convenience problem that politicians, educators, political enthusiasts, research institutions, media professionals, and regular citizens may encounter when trying to look for information about current congress members.

## Developer Manual
This section provides information on how to use our application as well as dependencies required to run the program. 

### How To:
1. Download the entire repository in one folder
2. Insert the ProPublica API key into the config.txt file and save
3. Run the GUI.py file (preferrably in Spyder or another python IDE)
4. The user interface will now appear in a separate window
5. Now, there are 3 options presented
    i. Search any congress member from sessions 102 - 116
          a. Select the first button
          b. Enter the congress member first and last name in the corresponding textbox
          c. Select 'search' at the bottom and wait
          d. A new window will present the entered congress member information for each session he/she was in
    ii. Search any U.S. state to find it's current representatives
          a. Select the second button
          b. Enter the 2 letter state code in the corresponding textbox (second one down)
          c. Select 'search' at the bottom of the GUI and wait
          d. A new window will present all the current represenatives for the entered state code
    iii. See a plot of the average ages over time (1993 - 2019)
          a. Select the third button
          b. Select 'search' at the bottom of the GUI and wait
          c. A plot will appear in the output window of your IDE
6. To exit, click the X at the top right of any window or select 'Exit Program' at the bottom of the GUI

### Requirements:
1. Preferrably a python IDE is used to run the scripts
2. The pandas package is installed
3. The matplotlib library is installed
4. The tkinter package is installed
5. numpy is installed


