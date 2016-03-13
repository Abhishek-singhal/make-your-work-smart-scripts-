import urllib
import requests
import urllib.request
url = input("please enter the link: ")
name = input("name of the file: ")
if url[-3:-1] =='jp' or url[-4:-1] == 'jpe':
	print ("downloading your image")
	r = requests.get(url)
	with open(name + ".jpg", "wb") as code:
	    code.write(r.content)
elif url[-3:-1] == 'mp':
	print ("downloading your song")
	r = requests.get(url)
	with open(name + ".mp3", "wb") as code:
	    code.write(r.content)
elif url[-3:-1] == 'mp':
	print ("downloading your video song")
	r = requests.get(url)
	with open(name + ".mp4", "wb") as code:
	    code.write(r.content)
elif url[-3:-1] == 'ex':
	print ("downloading your software")
	r = requests.get(url)
	with open(name + ".exe", "wb") as code:
	    code.write(r.content)