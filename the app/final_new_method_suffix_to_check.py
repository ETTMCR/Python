# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 02:16:11 2022

@author: 1

"""


def fun_sound():
    import winsound
    
    if first_word_b == first_word_a:
        freq = 500
        dur = 200
        for i in range(0, 5):    
            winsound.Beep(freq, dur)    
    else :
        if first_word_b > first_word_a: 
            # loop iterates 5 times i.e, 5 beeps will be produced.
            freq = 100
            dur = 50
            for i in range(0, 5):    
                winsound.Beep(freq, dur)    
                freq+= 100
                dur+= 50
        else :
            freq = 500
            dur = 50
            for i in range(0, 5):    
                winsound.Beep(freq, dur)    
                freq-= 100
                dur+= 50
        


from os.path import exists as file_exists

# grabbing the name of the article first from the to_check_now_article.txt - NO NEED
# import glob
# for this_file in glob.glob("to_check_now_*.txt"): # how_many_* with suffix, as made in the file final_new_method_suffix.py
#     filename=this_file.split('.')[0]
 
file1 = open('to_check_now.txt', 'r')
Lines = file1.readline().split("\n") #only first line
file1.close()
article= Lines[0]  #why it gives 'article\n' i.e. the \n itself ? - solved = file1.readlines --> readline().split("\n")
#delete to_check_now_{selected_arti}.txt
import os
osCommandString = 'to_check_now.txt'
#os.remove(osCommandString)
if os.path.exists(osCommandString):
    os.remove(osCommandString)

# file1 = f'how_many_{article}.txt'
# with open(file1, 'a') as file1:
#     file1.write(article)
#     #file1.write('\n') # new line writln ;-) 
#     Lines = file1.readline().split("\n")
#     file1.close()
#     #Lines = file1.readline().split("\n")


# if file_exists(eee) : # ofcourse
#     file1 = open(eee, 'r')
#     Lines = file1.readline().split("\n") #only first line
#     article= Lines[0]  #why it gives 'article\n' i.e. the \n itself ? - solved = file1.readlines --> readline().split("\n")
#     # https://www.delftstack.com/howto/python/python-readlines-without-newline/#use-the-strip-and-the-rstrip-methods-to-read-a-line-without-a-newline-in-python
#     file1.close()  #even though it will be open again, just for suer, not to stack in memory    
#      #first line   

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

#heb / eng check 
#### option to check the languge in order to handle also english articles
# import langid
# import requests
# lng = langid.classify(article)
# #('en', -0.19649028778076172)
# #print(lng[0])   

# if (lng[0]) =='he': 
# # https://stackoverflow.com/questions/39142778/python-how-to-determine-the-language
# #article = 'רותם סלע' #only for practice
# #print('https://he.wikipedia.org/w/index.php?title=' + article + '&action=info')
#     url='https://he.wikipedia.org/w/index.php?title=' + article + '&action=info'
# elif (lng[0]) =='en':
#     url='https://en.wikipedia.org/w/index.php?title=' + article + '&action=info'
# #html_text = requests.get('https://he.wikipedia.org/w/index.php?title=%D7%9C%D7%99%D7%A6%D7%9F_%D7%A7%D7%98%D7%9F_%D7%A0%D7%97%D7%9E%D7%93&action=info').text
# html_text = requests.get(url).text

url = 'https://pageviews.wmcloud.org/pageviews/?project=he.wikipedia.org&platform=all-access&agent=user&redirects=1&start=' +d1 + '&end=' +d1 + '&pages=' + article



driver = webdriver.Chrome("c:/Users/1/Desktop/chromedriver.exe")
#driver.minimize_window()
#driver.set_window_size(1, 1)
driver.set_window_position(-10000,0)
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
#ctypes.windll.user32.MessageBoxW(0,msg_box ,'title_box' , 0)

# with open(filename,'a',encoding='utf8') as file1:
#     file1.write(html)
#     file1.write('\n') # new line writln ;-)
#     file1.close()
    
title_box='the article "' + article
msg_box ="yesterday were " +  how_many + " people to watch the article."

ctypes.windll.user32.MessageBoxW(0,msg_box ,title_box , 0)

##### an option to open the article page
#import webbrowser
#webbrowser.open('https://he.wikipedia.org/wiki/' + article) 

# ----------- write for file how_many today
line =  str(how_many) + ' watched on the '+ d1 + ' .'

filename = f'how_many_{article}.txt'
with open(filename, 'a') as file1: #a stand for appand file while w is for new each time             
    file1.write('\n') # new line writln ;-)
    file1.write(line)
    file1.close()

#----------- Using readlines() to compare how_many relative to yesterdy
first_time = True
if  (first_time):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    file1.close()
    # mylist[0][:1]  # get up to the first character in the first item in the list
    #a = Lines[(len(Lines)-2)][:1]
    #b =  Lines[len(Lines)-1][:1]  # get up to the first character in the last item in the list
    a = Lines[(len(Lines)-2)] #last-1 line 
    b = Lines[len(Lines)-1] #last line 
    first_word_a =  a.split()[0]
    first_word_b = b.split()[0]
    first_word_a = first_word_a.replace(",", "") # the number is given as string as ddd,ddd,ddd type of number
    first_word_b = first_word_b.replace(",", "")
    first_word_a = int(float(first_word_a))
    first_word_b = int(float(first_word_b))
    
    #if first_word_b > first_word_a: 
    fun_sound()
    delta = first_word_b-first_word_a
    msg_box ="today were " + str(delta) + " new pepole to watch the article !"
    ctypes.windll.user32.MessageBoxW(0,msg_box ,title_box , 0)
    with open(filename, 'a') as file1: #a stand for appand file while w is for new each time             
        #filename.write('\n') # new line writln ;-)
        file1.write(' ' + msg_box)
        file1.close()
    #end of if first_word_b > first_word_a: 
# end of if not (first_time):
    
driver.quit() # since it at driver.set_window_position(-10000,0)
    