import requests
from bs4 import BeautifulSoup
r=requests.get("http://static.cricinfo.com/rss/livescores.xml")
soup = BeautifulSoup(r.content,"html.parser")
g_data = soup.find_all("title")
i=0
for item in g_data:
    print(i,item.text)
    i=i+1
    
query =int(input("enter ur match no."))

a = soup.find_all("link")
spam = []
j=0
for link in a:
    spam.insert(j,link.text)
    j=j+1

b=requests.get(spam[query])
q = BeautifulSoup(b.content,"html.parser")
a_data = q.find_all("title")
for item in a_data:
     print(item.text)




