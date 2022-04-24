# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:54:05 2022

@author: 1
"""

# def click_left(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#
# def click_right(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)    
#
# def Scroll_one_up
#     win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x,y, 10, 0)
#
# def Scroll_one_down
#     win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, -1, 0)    
#
# def push_button(self, button):
#     win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
#     #time.sleep(.15)
#     win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)    

# to work without neet the chromedriver.exe
# from requests_html import HTMLSession
# import nest_asyncio
# nest_asyncio.apply()
# session = HTMLSession()
# url = 'https://clickspeedtest.com/'
# session.get(url)
# # r = session.get(url)
# # html_str = r.text 

import win32api, win32con , time

url = 'https://clickspeedtest.com/' #for 5 seconds 
url = 'https://clickspeedtest.com/clicks-per-second.html'
import webbrowser # no need to download the third party chromedriver.exe
webbrowser.open(url, new=1)

# # # ---- generating chrom bot to work with -----------
# # # https://sites.google.com/chromium.org/driver/downloads?authuser=0
# from selenium import webdriver # selenium-2.48.0.dist-info !!!!!!!!!!!! version
# # driver = webdriver.Chrome("c:/chromedriver.exe")
# # driver.get(url)
# #delay = 3 # seconds - to page to load all elements - it is doing it alone, then goes to next code

time.sleep(3)
win32api.keybd_event(0x1B, 0,0,0) # 'esc':0x1B,
time.sleep(.05)
win32api.keybd_event(0x1B,0 ,win32con.KEYEVENTF_KEYUP ,0)

x= 550
y=550
win32api.SetCursorPos((x,y))

# F11 full screen #
win32api.keybd_event(0x7A, 0,0,0) # https://gist.github.com/chriskiehl/2906125 - Python win32api simple Virtual keystroke examples
time.sleep(.05)
win32api.keybd_event(0x7A,0 ,win32con.KEYEVENTF_KEYUP ,0)

# simulate the pressing 0x28 i.e. DOWN "ARROW key" for 10 times
# for i in range(8): #go down to the specific test arae
#     #time.sleep(0.01)
#     win32api.keybd_event(0x28, 0,0,0)
#     time.sleep(0.1)
#     win32api.keybd_event(0x28,0 ,win32con.KEYEVENTF_KEYUP ,0)
    
# how do I make a code run for X amount of seconds    
# https://stackoverflow.com/questions/24374620/python-loop-to-run-for-certain-amount-of-seconds
j=0
win32api.SetCursorPos((x,y))
t_end = time.time() + 5 #for 5 seconds #60 * 15 are equal to 15 min
t_end = time.time() + 2
while time.time() < t_end:
    #click_left(500,500) # in order to save te calls, and make it even more faster
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    j+=1 # it seems that this section not influancing the score
#push_button()

# F11 existing full screen #
win32api.keybd_event(0x7A, 0,0,0) 
time.sleep(.05)
win32api.keybd_event(0x7A,0 ,win32con.KEYEVENTF_KEYUP ,0)

#msgbox
#time.sleep(8)
#import ctypes 
#ctypes.windll.user32.MessageBoxW(0, 'your bot just have made ' + str(j) + 'click in five seconds\nwhich are equivalent to '+ str(j/5) +' Click Per Seconds', "bot CPS score", 1)
#ctypes.windll.user32.MessageBoxW(0, 'your bot just have made ' + str(j) +' Click Per Seconds', "bot CPS score", 1)

#import tkinter # only for using multiple lines by \n
#tkinter.messagebox.showinfo('Text','your bot made ' + str(j) + 'click in five seconds\nwhich are equivalent to '+ str(j/5) +' click in seconds')

