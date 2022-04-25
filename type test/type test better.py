# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:43:37 2022

@author: 1
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:39:16 2022


"""    
url='https://cpstest.org/typing-speed-test/1-minute.php'

def full_screen ():
    win32api.keybd_event(0x7A, 0,0,0) 
    time.sleep(.05)
    win32api.keybd_event(0x7A,0 ,win32con.KEYEVENTF_KEYUP ,0)
#%%
#import requests
from bs4 import BeautifulSoup
from selenium import webdriver # selenium-2.48.0.dist-info !!!!!!!!!!!! version
import win32api, win32con,time

driver = webdriver.Chrome("c:/chromedriver.exe")
driver.get(url)

# F11 entering  full screen #
#full_screen () #there is a bug when you hit the F11, than the test is already stating
#%%
 
#import time
time.sleep(5)
word_count=0

html = (driver.page_source) 
soup = BeautifulSoup(html, 'lxml')
#print(soup)
supa = soup.find('section',attrs={'id' : 'word-section'})#.text
supa = supa.find_all('span')#.text
#https://html-cleaner.com/
#print(supa)
#print(str(supa))
eee=(str(supa))
#print (eee)

#%% spliting into words
new_set = eee.replace('<span>', '')
new_set = new_set.replace('[<span class="current-word">', '')
new_set = new_set.replace('</span>', '')
new_set = new_set.replace(',', '')
new_set = new_set.replace(']', '')
#print(new_set.split())
v=new_set.split()
#print(v[0])

#%% main action of test
t_end = time.time() + 60 * 1 # are equal to 1 min

#while (time.time() < t_end) and not word_count>=350 : # maximum length of test is 350 words

for x in range(len(v)):
#for x in v:
    word_count+=1
    #print(how_many) 
    
    # a better way will be a loop over the span section under the <section id="word-section">
    element = driver.find_element_by_id("typebox") #WORKS - inputting the word in the text box
    element.send_keys(v[x])  #WORKS
    element.send_keys("\ue00D") #WORKS - push space button

# F11 exiting  full screen #
#full_screen ()

#%% # scraping how much it takes
#<h5 id="timer" class="mb-0">Timer : <span>0:00</span></h5>
html = (driver.page_source) 
soup = BeautifulSoup(html, 'lxml')
#how_many = soup.find_all('section', id_='word-section') #doesn't work
second_took = soup.find('h5', class_='mb-0').text

import ctypes 
t=second_took.replace('Timer : 0:','')
ctypes.windll.user32.MessageBoxW(0,'It took only ' + str(60-int(t))+ ' seconds', "Better Bot WPB score", 1)