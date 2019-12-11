# ProPublica Search Engine #

This program is a group project for INST 326. It implements a graphical user interface(GUI) that uses [the ProPublica Congress API](https://www.propublica.org/datastore/api/propublica-congress-api) to conduct three types of searches regarding members of the United States Congress.
As a GUI plug in to a webpage, the ProPublica Search Engine can be utilized as a convenient tool for fast gathering of information by any user with or without particular technical/programming skills.  

  ![GUI image](https://github.com/aloftus3/326project.github.io/blob/Marzenah_developer/GUI_run_image.png)

## Install ##
To run this program you will need Python3 and the following modules: tkinter, requests, matplotlib, pytest, pandas, and numpy. All six modules can be installed using the provided requirements.txt file by calling a command:

`pip install -r requirements.txt`

You will also need to get your own ProPublica [key](https://www.propublica.org/datastore/api/propublica-congress-api) and save it in a config.txt file that is included as an empty file.

## Run ##
This program is initiated by running the GUI.py file:

`python GUI.py`

## Test ##
Included are unit tests that you can run from test.py file:

`pytest test.py`

## License ##
MIT

