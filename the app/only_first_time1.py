# -*- coding: utf-8 -*-
"""
Created on Sun May  8 14:09:59 2022

@author: 1
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 01:18:58 2022

@author: 1
"""


# article=''
# print(f'{article} ' )

import input_box_article1
article = input_box_article1.new_article
def back():
    print (f'{input_box_article1.new_article}')
# OR, TAHT CODE LINE BELOW
# article = input("What article in wikipedia you want to scrap ?")

    
#### option to check the languge in order to handle also english articles
import langid
import requests
lng = langid.classify(article)
#('en', -0.19649028778076172)
#print(lng[0])   

if (lng[0]) =='he': 
# https://stackoverflow.com/questions/39142778/python-how-to-determine-the-language
#article = 'רותם סלע' #only for practice
#print('https://he.wikipedia.org/w/index.php?title=' + article + '&action=info')
    url='https://he.wikipedia.org/w/index.php?title=' + article + '&action=info'
elif (lng[0]) =='en':
    url='https://en.wikipedia.org/w/index.php?title=' + article + '&action=info'
#html_text = requests.get('https://he.wikipedia.org/w/index.php?title=%D7%9C%D7%99%D7%A6%D7%9F_%D7%A7%D7%98%D7%9F_%D7%A0%D7%97%D7%9E%D7%93&action=info').text
html_text = requests.get(url).text

filename =  'how_many_' + article + '.txt' #suffix the name of article in the file name
with open(filename, 'w') as file1:
    file1.write(article)
    #file1.write('\n') # new line writln ;-)  
    file1.close()
    
#from os.path import exists as file_exists
#first_time = file_exists(filename)


#import requests
from bs4 import BeautifulSoup
from selenium import webdriver # selenium-2.48.0.dist-info !!!!!!!!!!!! version
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from datetime import date ,timedelta
today = date.today()
#print(today)
yesterday = today - timedelta(days=2) # in late night there's an error trying to do so, because of different time areas, that's why days=2 instead of days=1, i.e. yesterday
d1 = str(yesterday)#.strftime("%YYYY-%mm-%dd")

url = 'https://pageviews.wmcloud.org/pageviews/?project=he.wikipedia.org&platform=all-access&agent=user&redirects=1&start=' +d1 + '&end=' +d1 + '&pages=' + article


driver = webdriver.Chrome("c:/Users/1/Desktop/chromedriver.exe")

driver.set_window_position (-10000,0)#(0,0)#(-10000,0)
driver.get(url)
delay = 2 # seconds - to page to load all elements

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
#driver.quit()
    
html = (driver.page_source)
soup = BeautifulSoup(html, 'lxml')
#a = soup.find('section', 'wrapper')
how_many = soup.find('span', class_ ='hidden-lg').text #WORKS


import ctypes  # An included library with Python install. 
#title_box='את הערך ' + article + ' ראו'
the_digit=""
for i in how_many:
        if i.isdigit():
            the_digit += i
how_many = the_digit

    
title_box='the article "' + article
msg_box ="yesterday were " +  how_many + " people to watch the article."

ctypes.windll.user32.MessageBoxW(0,msg_box ,title_box , 0)

# ----------- write for file how_many yesterday
line =  str(how_many) + ' watched on the '+ d1 + ' .'

with open(filename, 'a') as file1: #a stand for appand file while w is for new each time             
    file1.write('\n') # new line writln ;-)
    file1.write(line)
    file1.close()
    
driver.quit() # since it at driver.set_window_position(-10000,0)
 
