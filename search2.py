#output the list of reps broken by the the chambers for that specific state
import requests
import json
import string
import numpy as np
import pandas as pd
import search1 
from tkinter import*
from tkinter import messagebox as msg

#declare a list of all the state codes
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#define a function that takes out any punctuation of the string passed into it
def cleanMe(dirtyWord):
    for char in dirtyWord:
        if char in string.punctuation:
            return dirtyWord.replace(char,'')
        else:
            return dirtyWord

#define a function to run a congress member search by state
def runSearch2(state):
    data = []
    #clean the passed arg and set to uppercase characters
    state = cleanMe(state).upper()
    #if state is not in the states list, display a messagebox error
    if state not in states:
        msg.showerror("Error","Name Error. Try again.")
        #exit function
        return pd.DataFrame()
    
    #for each chamber in congress
    for chamber in ['house', 'senate']:
        #for each member in the get request
        for member in search1.get(f"/members/{chamber}/{state}/current.json"): 
            #append the member name, chamber, and state to the data list
            data.append([member['name'], chamber.upper(), state])
                    
    # Create a dataframe with the member components
    # Dataframe columns are name, chamber, and state. The rows are the members
    df = pd.DataFrame(data, columns= ['Name','Chamber','State'])
    #return the filled dataframe
    return df 

