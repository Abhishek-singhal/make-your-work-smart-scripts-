import os,re
from os.path import join
def search(name,dire):
    i=0
    for root, dirs, files in os.walk(dire,topdown=True):
        for temp in files:
            m = rx.search(temp)
            if m:
                dest=os.path.join(root, temp)
                print ("found: "+dest[1:])
                i=i+1      
        
    print("total result " +str(i))
try:
    s=input("name of the file : ")
    dire = input("Directory to search in (For Present directory leave blank)")
    if (dire==""):
        dire='.'
    rx = re.compile(s,re.IGNORECASE)    
    search(s,dire)
except:
    print("No such name file exist")
    
