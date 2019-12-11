import search1
import search2
import pandas as pd

#tests the cleanMe function in search 2
def test_cleanme():
	assert search2.cleanMe('.Cory Booker') == 'Cory Booker'
	assert search2.cleanMe(',Cory Booker') == 'Cory Booker'
	return "success"

#tests the main search1 function with Cory Booker
def test_search1():
    assert search1.runSearch1('Cory Booker') ==('Session: ' + '113'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        '\n\tDate of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
			"Party: "+ 'D'+'\n\t' + 
                        "Gender: " + 'M'+ '\n' +
			'Session: ' + '114'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        '\n\tDate of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
			"Party: "+ 'D'+'\n\t' + 
                        "Gender: " + 'M'+ '\n' +
			'Session: ' + '115'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        '\n\tDate of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
			"Party: "+ 'D'+'\n\t' + 
                        "Gender: " + 'M'+ '\n' +
			'Session: ' + '116'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        '\n\tDate of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
			"Party: "+ 'D'+'\n\t' + 
                        "Gender: " + 'M\n')
    return("success")
    
#tests the runSearch2 function in search 2
def test_search2():
    data = [['David Cicilline', 'HOUSE','RI'], ['Jim Langevin', 'HOUSE','RI'],
            ['Sheldon Whitehouse', 'SENATE','RI'],['Jack Reed', 'SENATE','RI']]
    df = pd.DataFrame(data, columns = ['Name', 'Chamber','State']) 
    assert search2.runSearch2('RI').equals(df)
    return ("success")

#print the test results of each test function
if __name__ == '__main__':
	print(test_cleanme())
	print(test_search1())
	print(test_search2())



