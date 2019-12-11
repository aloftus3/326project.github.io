import requests
import string
import search2

#This is the get function to initialy connect to API (used in search 2)
def get(url):
    #open the config.txt file which will contain the API key
    with open('config.txt') as handle:
        API_KEY = handle.read().strip()
    headers = {"X-API-KEY": API_KEY}
    #set the url of the API. The 'base' is constant and the rest of the path 
    #will be passed through the function
    url = "https://api.propublica.org/congress/v1" + url
    #call the api request and return the dataset of members
    data = requests.get(url, headers=headers).json()
    return data['results']

    
#define a funstion to run the first search (used in GUI.py)
def runSearch1(name):
    #call the cleanMe() function from search2 and reassign to 
    name = search2.cleanMe(name)
    #set the name to 'First Last' format
    name = name.lower().title()

    
    #set result to an empty string that will represent data for each session
    result = ''
    
    #loop through the reversed order of the sessions
    for session in reversed(range(102,117)):
        #loop through the chambers
        for chamber in ['house','senate']:                        
            #loop through each get request
            for response in get("/"+str(session)+"/"+chamber+"/members.json"):
                #loop through each member                                
                for member in response['members']:
                    #if the first and last name equal the passed name then
                    #add the member information to the result string
                    if (member['first_name'] +" "+ member['last_name']) == name:
                                                
                        result = ('Session: ' + str(session) +
                        '\n\tFacebook Account: '+ str(member['facebook_account'])+
                        '\n\t' + 'Title: ' + str(member['title'])+'\n\t' +
                        'Date of Birth: ' + str(member['date_of_birth'])+'\n\t' +
                        'Url: ' + str(member['url'])+'\n\t' +
                        'State: '+ str(member['state'])+'\n\t'+
                        "Party: "+ str(member['party'])+'\n\t' + 
                        "Gender: " + str(member['gender']) + '\n' + result)
                        
                            
                
    return result