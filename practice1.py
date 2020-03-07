
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html=urlopen('http://www.pythonscraping.com/pages/page3.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')
else:
    bs=BeautifulSoup(html.read(),'html.parser')
    print(bs)
    #namelist=bs.find_all('span',class_='green')
    #for name in namelist:
        #print(name.get_text())
    #theprince=bs.find_all(text='the prince')
    #print(len(theprince))
    #for sibling in bs.find('table',{'id':'giftList'},).tr.next_siblings:
        #print(sibling)
        

