import requests
from datetime import date, timedelta
from xml.etree import ElementTree

URL = 'https://www.finnkino.fi/xml/Schedule'
TODAY = date.today()
spoken_language_iso = ["FI", "SE", "EN"]
# You can also give the "spoken_language_iso" as a parameter when running this script from terminal.
# Access the params with "sys.argv" (also import sys)

for i in range(10):
    try:
        dt = TODAY + timedelta(i)
        params = {'area': '1014', 'dt': dt.strftime('%d.%m.%Y')}
        response = requests.get(url=URL, params=params)
        tree = ElementTree.fromstring(response.content)
        shows = tree.find('Shows').findall('Show')
        n = len(shows)
    except:
        break

    for show in shows:
        spoken = show.find('SpokenLanguage')
        iso = spoken.find('ISOTwoLetterCode').text
        
        if iso in spoken_language_iso:
            page = show.find('EventURL').text
            print(page)
