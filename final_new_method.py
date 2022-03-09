# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 13:03:22 2022

@author: 1
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:49:55 2022

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
filename = 'how_many.txt' # option - suffix the name of article in the file name
first_time = False
if file_exists(filename) : 
    file1 = open(filename, 'r')
    Lines = file1.readline().split("\n") #only first line
    article= Lines[0]  #why it gives 'article\n' i.e. the \n itself ? - solved = file1.readlines --> readline().split("\n")
    # https://www.delftstack.com/howto/python/python-readlines-without-newline/#use-the-strip-and-the-rstrip-methods-to-read-a-line-without-a-newline-in-python
    file1.close()  #even though it will be open again, just for suer, not to stack in memory    
     #first line   
else: #first time to be created
    article = input("What article in wikipedia you want to scrap ?")
    with open(filename, 'w') as file1:
        file1.write(article)
        #file1.write('\n') # new line writln ;-)  
        file1.close()
    first_time = file_exists(filename)


#import requests
from bs4 import BeautifulSoup
from selenium import webdriver # selenium-2.48.0.dist-info !!!!!!!!!!!! version
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# ---- generating relevant url for today -----------
from datetime import date ,timedelta
today = date.today()
#print(today)
yesterday = today - timedelta(days=2)
d1 = str(yesterday)#.strftime("%YYYY-%mm-%dd")
#print(d1)
#article = 'ליצן קטן נחמד'
#article = 'פוטין'
#url = 'https://pageviews.wmcloud.org/pageviews/?project=he.wikipedia.org&platform=all-access&agent=user&redirects=1&start=2022-03-02&end=2022-03-02&pages=' + article
#url = 'https://pageviews.wmcloud.org/pageviews/?project=he.wikipedia.org&platform=all-access&agent=user&redirects=1&start=' +str(d1) + '&end=' +str(d1) + '&pages=' + article
url = 'https://pageviews.wmcloud.org/pageviews/?project=he.wikipedia.org&platform=all-access&agent=user&redirects=1&start=' +d1 + '&end=' +d1 + '&pages=' + article

# ---- generating chrom bot to scrap from -----------

driver = webdriver.Chrome("c:/Users/1/Desktop/chromedriver.exe")
#driver.minimize_window()
#driver.set_window_size(1, 1)
driver.set_window_position(-10000,0) # hiding free view
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

# -------- msg_box of how many yesterday
import ctypes  # An included library with Python install. 
#title_box='את הערך ' + article + ' ראו'
the_digit=""
for i in how_many:
        if i.isdigit():
            the_digit += i
how_many = the_digit

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

with open(filename, 'a') as file1: #a stand for appand file while w is for new each time             
    file1.write('\n') # new line writln ;-)
    file1.write(line)
    file1.close()

#----------- Using readlines() to compare how_many relative to yesterdy
if not (first_time):
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
    msg_box ="yesterday were " + str(delta) + " new pepole to watch the article !"
    ctypes.windll.user32.MessageBoxW(0,msg_box ,title_box , 0)
    with open(filename, 'a') as file1: #a stand for appand file while w is for new each time             
        #filename.write('\n') # new line writln ;-)
        file1.write(' ' + msg_box)
        file1.close()
    #end of if first_word_b > first_word_a: 
# end of if not (first_time):
    
driver.quit() # since it at driver.set_window_position(-10000,0)
    