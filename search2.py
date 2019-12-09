#output the list of reps broken by the the chambers for that specific state
import requests
import json
import string
import numpy as np
import pandas as pd
import search1 
from tkinter import*
from tkinter import messagebox as msg

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def cleanMe(dirtyWord):
    for char in dirtyWord:
        if char in string.punctuation:
            return dirtyWord.replace(char,'')
        else:
            return dirtyWord

'''
def get_district(place):
    districtHouse = [ 'AK', 'DE', 'MT', 'ND', 'SD', 'VT', 'WY', 'GU', 'AS', 'VI', 'MP','PR', 'DC']
    if place in districtHouse:
        return 1
'''

# def main():
def runSearch2(state):
    data = []
    state = cleanMe(state).upper()
    if state not in states:
        msg.showerror("Error","Name Error. Try again.")
        return pd.DataFrame()
    chambers = ['house', 'senate']
    
    for chamber in chambers:
        for member in search1.get(f"/members/{chamber}/{state}/current.json"): 
            # print(member['name'], chamber, state) 
            data.append([member['name'], chamber.upper(), state])
                    
    # Create a dataframe with the components: name, chamber, state, session(not implemented yet).
    # Dataframe columns are name, chamber, and state. The rows are the members
    # print(data)
    df = pd.DataFrame(data, columns= ['Name','Chamber','State'])
    return df 

