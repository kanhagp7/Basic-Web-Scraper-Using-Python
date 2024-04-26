import requests
from bs4 import BeautifulSoup
import pandas as pd

#used request module to get the text content of the url

url = 'https://editorial.rottentomatoes.com/guide/essential-movies-to-watch-now/'
req = requests.get(url)
print(req)

# beautifulSoup parses the text content to html format

soup = BeautifulSoup(req.text, 'html.parser')

#Extracted the data from the parsed HTML content using html tags in which the required data is structered.

data = []
h2_tags = soup.find_all('h2')
for tag in h2_tags:
    lst = []
    try: 
        a_tag = tag.find('a')
        title = a_tag.get_text()
        lst.append(title)
    except: continue

    try: 
        year_tag = tag.find('span',class_ = 'subtle start-year')
        year = year_tag.get_text()
        lst.append(year)
    except:
        continue
    try:
        score_tag = tag.find('span',class_ = 'tMeterScore')
        score = score_tag.get_text()
        lst.append(score)
    except:
        continue
    data.append(lst)

# Finally converted the extracted data in the form of dataframe using pandas

df = pd.DataFrame(data, columns=["Movie Name", "Release Year", "Tomato Meter Score"])

df.to_excel('data.xlsx', index = False)
