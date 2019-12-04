###### Initial connection to Propublica  #######
#Right now can be tested with 'Cory Booker' or
#any congress member in the 116th session

import requests
import json
import string

# This is the get function he set up in class
def get(url):
    headers = {"X-API-KEY": "WWSGHLJjWxC2m9tznYILCKy1xtmkvnxxdo8nEBt8"}
    url = "https://api.propublica.org/congress/v1" + url
    data = requests.get(url, headers=headers).json()
    return data['results']

def cleanMe(dirtyWord):
    for char in dirtyWord:
        if char in string.punctuation:
            return dirtyWord.replace(char,'')
        else:
            return dirtyWord

def get_input():
    control = True
    while control:
        try:
            nameSearch = input("Input Congress Member first and last name: ")
            #check if empty, check if None
            if nameSearch == '' or nameSearch == None or nameSearch.isdigit() == True:
                nameSearch = input("Input Congress Member first and last name: ")
            #check if it has a number
            elif nameSearch.isalpha() == True:
                new_name = cleanMe(nameSearch)
                control=False
            else:
                new_name = nameSearch
                control = False;
        except:
            print("error")
    return new_name.capitalize()
    

def main():
    #get the user input of the congress member they want to search
    name = get_input()


    #create a list of all the congressional sessions
    #right now only looking at session 116 (yr. 2019)
    session = [116]

    #create a list of the chambers
    chambers = ['house','senate']


    #loop through the sessions
    for s in session:

        #loop through the chambers
        for chamber in chambers:

            #loop through each get request
            for member in get("/"+str(s)+"/"+chamber+"/members.json"):

                for m in member['members']:

                    if (m['first_name'] +" "+ m['last_name']) == name:

                        #just for testing
                        print('Facebook Account: '+ str(m['facebook_account']))
                        print('Url: ' + str(m['url']))
                        print('State: '+ str(m['state']))
                        print("In Office: "+ str(m['in_office']))
                    
if __name__ == '__main__':
    main()

