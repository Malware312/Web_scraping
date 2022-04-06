from functools import lru_cache
from time import sleep
from os import system
import urllib.request
#import json

@lru_cache

class color:
    red = '\033[1;31m'
    blue = '\033[1;96m'
    end = '\033[m'

def layout(line=color.blue + '~~' * 25 + color.end , msg='Web scraping'):
    print(line)
    print(msg.center(50))
    print(line)
'''
def json():
    with open('request.txt' , 'r') as f:
        text = json.load(f)
        print(text)  
file = ''

if not file:
    json()'''

def clear():
    clen = ''
    if clen == '':
        system('clear')
    if clen == '':
        system('cls')

def analizing_web(): 

    try:
        link = str(input(color.blue + 'Enter the website url:\n... ' + color.end))
        request = urllib.request.urlopen(f'{link}')
        print(request.read())


    except:
        print(color.red + 'Error. Try again ' + color.end)
        sleep(0.8)
        clear()
        layout()
        analizing_web()


clear()
layout()
analizing_web()