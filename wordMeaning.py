from __future__ import print_function
from re import sub
from bs4 import BeautifulSoup
import urllib.request
import sys
from tkinter import *

root = Tk()
root.title('Dictionary')
root.geometry("644x344")

text = ""
i = 0

def printSomething():
    word = entry.get()

def Take_input():
    global text
    global i
    i = 0
    Output.delete("1.0","end")
    word = inputtxt.get("1.0", "end-1c")
    ReqMore.pack()
    try:
        urlpage = urllib.request.urlopen("https://www.dictionary.com/browse/"+ word).read()
        bswebpage = BeautifulSoup(urlpage, features="html.parser")
        results = bswebpage.findAll("span",{'class':"one-click-content css-nnyc96 e1q3nk1v1"})
        toPrint = "Word: "+ word + "\n"
        text = results
        for result in results:
            if (i%5==0 and i!=0):
                break
            toPrint = toPrint + str(i+1) + ". "+ result.text + "\n"
            i+=1
        if i >= len(text):
            ReqMore.pack_forget()
        Output.insert(END, toPrint)
    except:
        Output.insert(END, "Word: "+ word + " not found!")
        ReqMore.pack_forget()


def showMore():
    global text
    global i
    toPrint = ""
    
    if i >= len(text):
        return
    
    while True:
        toPrint = toPrint + str(i+1) + ". "+ text[i].text + "\n"
        i += 1
        if (i%5==0 and i!=5):
            break
        if i >= len(text):
            ReqMore.pack_forget()
            break
    Output.insert(END, toPrint)
        
    
l = Label(text = "Enter your Word: ")
inputtxt = Text(root, height = 4)

Output = Text(root,  height = 10,
            bg = "light cyan")

Display = Button(root, height = 2,
                width = 20,
                text ="Show",
                command = lambda:Take_input())
                
ReqMore = Button(root, height = 2,
                width = 20,
                text ="Show More Definitions ...",
                command = lambda:showMore())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
ReqMore.pack()

mainloop()

