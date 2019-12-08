#output the list of reps broken by the the chambers for that specific state
import requests
import json
import string
import numpy as np
import pandas as pd

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def get(url):
    with open('config.txt') as handle:
        API_KEY = handle.read().strip()
    headers = {"X-API-KEY": API_KEY}
    url = "https://api.propublica.org/congress/v1" + url
    data = requests.get(url, headers=headers).json()
    return data['results']

def cleanMe(dirtyWord):
    for char in dirtyWord:
        if char in string.punctuation:
            return dirtyWord.replace(char,'')
        else:
            return dirtyWord

def get_state():
    control = True
    while control:
        try:
            temp = input("Enter a state (TX): ")
            #check if empty, check if None, check if it has numbers, check if length is greater than 2
            if temp == '' or temp == None or temp.isdigit() == True or len(temp) > 2:
                temp = input("Enter a state (TX): ")
            #check if it has a number
            elif temp.isalpha() == True:
                new_state = cleanMe(temp)
                control=False
            else:
                new_state = temp
                control = False;
        except:
            print("error")
    return new_state.upper()


def get_district(place):
    districtHouse = [ 'AK', 'DE', 'MT', 'ND', 'SD', 'VT', 'WY', 'GU', 'AS', 'VI', 'MP','PR', 'DC']
    if place in districtHouse:
        return 1

# def main():
def runSearch2():
    data = []
    state = get_state()
    chambers = ['house', 'senate']
    # Put on line 61 "/{chamber}/{state}/{district}/current.json" if we want to implement district
    district = get_district(state)
    
    for chamber in chambers:
        for member in get(f"/{chamber}/{state}/current.json"): 
            # print(member['name'], chamber, state) 
            data.append([member['name'], chamber, state])
                    
    # Create a dataframe with the components: name, chamber, state, session(not implemented yet).
    # Dataframe columns are name, chamber, and state. The rows are the members
    # print(data)
    df = pd.DataFrame(data, columns= ['Name','Chamber','State'])
    print(df)      
                
# if __name__ == '__main__':
#    main()