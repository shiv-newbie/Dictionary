from __future__ import print_function
from re import sub
from bs4 import BeautifulSoup
import urllib.request
import sys

print("")
word = str(sys.argv[1])

print("Word: "+ word)

urlpage = urllib.request.urlopen("https://www.dictionary.com/browse/"+ word).read()
bswebpage = BeautifulSoup(urlpage, features="html.parser")
results = bswebpage.findAll("span",{'class':"one-click-content css-nnyc96 e1q3nk1v1"})
i = 0
for result in results: 
    if (i+1)%5==0:
        print("Do you want more results?[y/n]: ", end="")
        ans = str(input())
        if ans == "n":
            break
    print(str(i+1) + ". "+ result.text)
    i+=1
    
print("Have a nice day :)")
print("") 
