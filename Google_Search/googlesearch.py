#Created By Vinoth 26042020 - Source from Youtube Video and stack over flow.
import webbrowser
import sys
import requests,bs4

#webbrowser.open('https://google.com')
if len(sys.argv) != 2:
    print( "ERROR: Please provide keyword in correct format to search it from GOOGLE")
    print("EX:$ python " + sys.argv[0] + " 'Blue Whale'")
    exit()
else:
    print("INFO: Result", sys.argv[1:])
# URL open request for keyword
url_request = requests.get('https://www.google.com/search?q='+''.join(sys.argv[1:]))
url_request.raise_for_status()

#Convert heavy javascript to get python readable links to open in browser

soup = bs4.BeautifulSoup(url_request.text,"html.parser")
linkElements = soup.select('div#main > div > div > div > a')
linkToOpen = min(5, len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://www.google.com'+linkElements[i].get('href'))