# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text = "weather+03079"
url = 'https://google.com/search?q=' + text

print(url)
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result = requests.get(url)

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(requests.get("https://www.google.com/search?q=weather+03079").content)
print(soup.find("div", attrs={'id', 'wob_loc'}).text)
# soup.find.all( h3 ) to grab
# all major headings of our search result,
'''
In [7]: soup = BeautifulSoup(requests.get("https://www.google.com/search?q=weather+london").content)

In [8]: soup.find("div", attrs={'id': 'wob_loc'}).text
Out[8]: 'London, UK'
'''



# heading_object = soup.find_all("div", {"class": "UQt4rd"})  # 'UQt4rd' = what i want

# Iterate through the object
# and print it as a string.
'''for info in heading_object:
    print(info.getText())
    print("------")
    '''