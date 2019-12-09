
import requests
import string

# This is the get function to initialy connect to API (used in search 2)
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

def get_input():
    control = True
    while control:
        try:
            nameSearch = input("Input Congress Member first and last name:\n")
            #check if empty, check if None
            if nameSearch == '' or nameSearch == None or nameSearch.isdigit() == True:
                nameSearch = input("Input Congress Member first and last name:\n")
            #check if it has a number
            elif nameSearch.isalpha() == True:
                new_name = cleanMe(nameSearch)
                control=False
            else:
                new_name = nameSearch
                control = False;
        except:
            print("error")
            
    #convert to all lower and the begginning of each capitilized
    new_name = new_name.lower().title()
    return new_name
    

def runSearch1(name):
    #get the user input of the congress member they want to search
    #name = get_input()
    name = cleanMe(name)
    name = name.lower().title()

    #create a list of the chambers
    chambers = ['house','senate']
    result = None
    #set testId to None
    ## Many congress members are in many sessions so I did reversed order of 
    ## sessions to only get the latest term
    for session in reversed(range(102,117)):

        #loop through the chambers
        for chamber in chambers:
            
            
            #loop through each get request
            for response in get("/"+str(session)+"/"+chamber+"/members.json"):
                                
                for member in response['members']:
                    if (member['first_name'] +" "+ member['last_name']) == name:
                                                
                        result = ('Session: ' + str(session) +
                        '\n\tFacebook Account: '+ str(member['facebook_account'])+
                        '\n\t' + 'Title: ' + str(member['title'])+'\n\t' +
                        'Date of Birth: ' + str(member['date_of_birth'])+'\n\t' +
                        'Url: ' + str(member['url'])+'\n\t' +
                        'State: '+ str(member['state'])+'\n\t'+
                        "Party: "+ str(member['party'])+'\n\t' + 
                        "Gender: " + str(member['gender']) + '\n' + str(result))
                
    return result