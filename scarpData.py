import re
import requests
import bs4
from urllib import request
info=[]
regex_class=re.compile("zero-z-index")
res=requests.get('http://www.imdb.com/list/ls070201583/')
soup=bs4.BeautifulSoup(res.text)
soupName=soup.find_all("img",{"class":regex_class})
print(len(soupName))
for var in soupName:
    #if(len(str(var.get('src')))):
    request.urlretrieve(var.get('src'),var.get('alt'))