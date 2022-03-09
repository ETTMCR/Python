
# coding: utf-8

# In[1]:


'''
UPGRADES
1. (bareky)reducing check areas, for less CPU resources
2. reset time ? for refreshing resources (does it makes problems doring the game goes on ? )
3. find a way to make the game be faster and than time.sleep(seconds_chosen : factor). the speed up factor
4. shouting down game by pressing a key
5. if i could find a way the make the game refresh (2) , like by music or by when u finsh level, but i checked and the bikes goes on the same area of the finish string
6. making X_pad and Y_pad automaticaly
'''

''' 
IMPORTANT
1.in python.exe and pythonw.exe need to be in: Compatibility --> properties --> change DPI settings -- > both squares need to be marked
because of problem of grabbing (all of ) the screen

2.All coordinates assume a screen resolution of 1920x1080, 
game is played when window * 2
x_pad = top left corner_x-1
y_pad = top left corner_y-1

3. Play area =  x_pad+1, y_pad+1, 796, 825

'''

# Globals
# ------------------
                    
x_pad = 559 #1360 # tear is 801
y_pad = 189 # 880 # tera is 691

from ctypes import windll #https://github.com/ponty/pyscreenshot/issues/25
user32 = windll.user32
user32.SetProcessDPIAware()

import pywinauto
import pynput # easier way controling mouse and keyboard
from pynput.mouse import  Button, Controller
#from pynput.keyboard import Key, Controller
#keyboard = Controller()
mouse = Controller()

# solution-1 : add to code 'from PIL'
#from PIL import ImageGrab # works fine in the jupyter platform, but makes problem in the IDLE platform


#solution-2 : https://pypi.python.org/pypi/pyscreenshot
import pyscreenshot as ImageGrab # works on IDLE platform

'''
Screenshots are incorrectly cropped on high-DPI displays.
Windows returns display geometry data scaled for the DPI, while the actual screenshots are unscaled.
Workaround: Right-click on python.exe, Properties, Compatibility tab, check 'Disable display scaling on high DPI settings'. 
Repeat for pythonw.exe.
Thanks to: https://github.com/ludios/Desktopmagic

Using the following code inside your app makes your app DPI aware on Windows and solves the issue.
This worked for me. Just note that user32.SetProcessDPIAware() needs to be called before pyscreenshot is initially imported.
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

'''

import os
import time
import win32api, win32con
import datetime 

from PIL import ImageOps
from numpy import * #The wildcard * means import everything from the module.
#ImageOps is another PIL module.
#It is used to perform operations (such as grayscaling) on an Image.

'''I'll briefly explain the second for those who aren't familiar with Python.
Our standard import statements loads the module's namespace (a collection of variable names and functions). 
So, to access items in a module's scope, we have to employ the module.attribute sytax.
However, by using a from ___ import statement we inherit the names into our local scope.
Meaning, the module.attribute syntax is no longer needed. 
They are not top level, so we use them as we would any other Python built-in function, like str() or list().
By importing Numpy in this manner, it allows us to simply call array(), instead of numpy.array().
'''

def screenGrab(): 

    box = (559,189,1360,880) # entire coord of the game
    #box = (x_pad,x_pad + 801 ,y_pad, y_pad + 691) 
    im = ImageGrab.grab(box)
    #im.show  ()  
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
    #print('grabbed')
    return im


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #module.attribute = ייחוס
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print ("Click.")          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def awake():
    mousePos(cord.pos_mid_win) #waking game
    leftClick()
    time.sleep(0.01)

def starting():
        
    mousePos(cord.pos_mid_win)
    leftClick()
    mousePos((cord.beavis))
    time.sleep(2) 
    #mousePos((cord.pos_00))
    leftClick() # beavis is selected

class cord: # storing the coordiantes of all we need
    beavis = (690-30,570) 
    pos_file_tab = (15,50)
    pos_new_game = (21,50)
    pos_00 = (0,0)
    pos_mid_win = (450,450)
    pos_spit_car = (75,600) # y axis = 600 for all
    pos_spit_car_again = (1,600)
    pos_spit_snai = (400,600) 
    pos_spit_bikes_up =(530,600) 
    pos_spit_bikes_mid =(545,600) 
    #pos_spit_ap_up = (225 ,600) #14122
    pos_spit_ap_up = (245 ,600) #
    pos_spit_ap_left = (100 ,600) 
    pos_spit_ap_right = (455 ,600)
    pos_spit_bikes_up_again =(90 ,600)
    pos_spit_bikes_down =(575 ,600) # rare
    #pos_spit_bikes_down_again =(580 ,600) # need to be done
    #pos_spit_bikes_mid_again =(580 ,600) # need to be done


def get_gray():
    box = (x_pad + 495, y_pad + 154, x_pad + 521, y_pad + 170)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a )#+ 'a1' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a

# @ means small area to calculate in a.sum

def get_car():
    box = (x_pad + 795,y_pad + 80,x_pad +800,y_pad +82) # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a , 'car' )
    #print (a)
    return a

def get_car_again(): # in  a case the car missed because other things 
    box = (x_pad + 619,y_pad + 110,x_pad + 620,y_pad +111)  # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a , 'car again' )
    #print (a)
    return a

def spit_car():
    GS = get_grn_spit()
    if GS == 159: # this time,checking the sum gray of the object itself, cuase beavis walks there , and with "if not" it will always b true
        print('YERIKA YERUKA!!!!!')
        mousePos(cord.pos_spit_car)    
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    else : 
        mousePos(cord.pos_spit_car)    
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def spit_car_again():
    GS = get_grn_spit()
    if GS == 159: # this time,checking the sum gray of the object itself, cuase beavis walks there , and with "if not" it will always b true
        print('YERIKA YERUKA!!!!!')
        mousePos(cord.pos_spit_car_again)    
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    else : 
        mousePos(cord.pos_spit_car_again)    
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
def get_grn_spit():
    box = (x_pad + 40, y_pad + 620, x_pad + 41, y_pad + 621) # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a )#+ 'a1' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 


def get_ap_up(): # paper airplane moves upwards # @
    #box = (x_pad + 203, y_pad + 420, x_pad + 211, y_pad + 440 ) #7061  V
    box = (x_pad + 203, y_pad + 420, x_pad + 205, y_pad + 440 ) # 3036 # cant be less area
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a ,' ap_up' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_ap_left(): # paper airplane moves upwards
    box = (x_pad + 170, y_pad + 480, x_pad + 185, y_pad + 495 ) # 6725
    #box = (x_pad + 175, y_pad + 480, x_pad + 181, y_pad + 481 ) #606
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a ,'ap_left')
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_ap_right(): # paper airplane moves upwards

    box = (x_pad + 290, y_pad + 455, x_pad + 291, y_pad + 456 )   # @ 
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a, 'ap_right')
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_bikes_up_again(): 
    #box = (x_pad + 320, y_pad + 250, x_pad + 330, y_pad + 260) 820 
    box = (x_pad + 320, y_pad + 250, x_pad + 321, y_pad + 251) # 81 # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a ,'bikes_up_again' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_bikes_down(): 
    #box = (x_pad + 760, y_pad + 325, x_pad + 780, y_pad + 335) # 920
    box = (x_pad + 770, y_pad + 320, x_pad + 771, y_pad + 321) # 79 # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a, 'bikes_down' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_bikes_up(): 
    #box = (x_pad + 760, y_pad + 245, x_pad + 800, y_pad + 260) # 193
    box = (x_pad + 790, y_pad + 245, x_pad + 791, y_pad + 246) #85  # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a,'bikes_up' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_bikes_mid():
    #box = (x_pad + 760, y_pad + 295, x_pad + 800, y_pad + 305)# 1510
    box = (x_pad + 790, y_pad + 295, x_pad + 791, y_pad + 296) # 77 # @
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a ,'bikes_mid' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def get_snai_right(): # coming from right 
    box = (x_pad + 490, y_pad + 140, x_pad + 505, y_pad + 160)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a , 'snai_right' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a

def get_snai_left(): # coming from left 
    box = (x_pad + 280, y_pad + 143, x_pad + 305 , y_pad + 160)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print (a , 'snai_left' )
    #im.save(os.getcwd() + '\seats\seat_1__' + str(int(time.time())) + '.png', 'PNG')    
    #im.show()
    return a 

def spit_snai():
    time.sleep(0.5) # the snai seat a while this point
    mousePos(cord.pos_spit_snai)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.9)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def spit_bikes_mid():
    mousePos(cord.pos_spit_bikes_mid)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.56)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    

def spit_bikes_down():
    mousePos(cord.pos_spit_bikes_down)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.55)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) 

def spit_bikes_up_again():
    mousePos(cord.pos_spit_bikes_up_again)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.65)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   

def spit_bikes_up():
    mousePos(cord.pos_spit_bikes_up)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.65)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    

def spit_ap_up():
    mousePos(cord.pos_spit_ap_up)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.8)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)      

def spit_ap_left():
    mousePos(cord.pos_spit_ap_left)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.45)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   

def spit_ap_right():
    mousePos(cord.pos_spit_ap_right)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.7)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   


def taking_values(): # of the areas into global  var's

    print ('craeting globals in def taking_values')
    global car_CA     
    global snai_left_CA 
    global snai_right_CA
    global car_again_CA 
    #man_CA
    global bikes_up_CA 
    global bikes_mid_CA
    global bikes_up_again_CA 
    global bikes_down_CA 
    global grn_spit_CA 
    global ap_up_CA 
    global ap_left_CA 
    global ap_right_CA 

    #man_CA = get_
    bikes_up_CA = get_bikes_up()
    #print('get_bikes_up was taken')
    time.sleep(.1)
    bikes_mid_CA = get_bikes_mid()
    #print('get_bikes_mid was taken')
    time.sleep(.1)
    bikes_up_again_CA = get_bikes_up_again()
    time.sleep(.1)
    bikes_down_CA = get_bikes_down()
    time.sleep(.1)
    grn_spit_CA = get_grn_spit()
    time.sleep(.1)
    ap_up_CA = get_ap_up()
    time.sleep(.1)
    ap_left_CA = get_ap_left()
    time.sleep(.1)
    ap_right_CA = get_ap_right()
    time.sleep(.1)
    car_CA = get_car()
    time.sleep(.1)
    car_again_CA = get_car_again()
    time.sleep(.1)
    snai_left_CA = get_snai_left()
    time.sleep(.1)
    snai_right_CA = get_snai_right()     
    time.sleep(.1)


def check_areas():

    #''' 
    s1 = get_car()
    if ( (s1 != car_CA)):
        print ('car is coming !')
        spit_car()
    #'''
    
    #'''
    s2 = get_snai_left()
    if s2 != snai_left_CA:
        print ('snai is coming from left!')
        spit_snai()
    #'''  

    #'''
    s3 = get_snai_right()
    if s3 != snai_right_CA:
        print ('snai is coming from right!')
        spit_snai()
    #'''

    #'''
    s4 = get_bikes_mid()
    if s4 != bikes_mid_CA:
        print ('bikes mid!')
        spit_bikes_mid()
    #'''

    #'''
    s5 = get_bikes_up()
    if s5 != bikes_up_CA:
        print ('bikes up!')
        spit_bikes_up()
    #''' 

    #'''
    s7 = get_bikes_up_again()
    if s7 != bikes_up_again_CA:
        print ('bikes up again!')
        spit_bikes_up_again()
    #'''  

    #'''
    s9 = get_bikes_down()
    if s9 != bikes_down_CA:
        print ('bikes_down !')
        spit_bikes_down()
    #''' 
    
    #''' 
    s6 = get_ap_up() # 
    if s6 != ap_up_CA:
        #print ('airplane up!')
        spit_ap_up()
    #''' 


    #'''
    s8 = get_ap_left()
    if s8 != ap_left_CA:
        print ('ap_left !')
        spit_ap_left()
    #''' 

    #'''
    s10 = get_ap_right()
    if s10 != ap_right_CA:
        print ('ap is on the right !')
        spit_ap_right()
    #'''

    #'''
    s11 = get_car_again()
    if s11 != car_again_CA:
        print ('car_again !')
        spit_car_again()
    #'''

def main():
    print ('main')
    #print (car_CA, 'second time')   
    #mone = 0
    while True:
        check_areas()
        #mone += 1 
        #print (mone)

def first():
    awake() 
    mousePos(cord.pos_mid_win) #waking game
    leftClick()
    time.sleep(0.01)
    time.sleep (.1)
    # mousePos(cord.pos_file_tab)
    # leftClick()
    # time.sleep (.2)
    # mousePos(cord.pos_new_game)
    # leftClick()
    # time.sleep (.2)
    starting() 
    print('time.sleep 4 seconds')
    time.sleep(2)
    taking_values() 

first()

#print ('first time car_CA',car_CA ) 


if __name__ == '__main__':
    main()
    
print ('OK code ',datetime.datetime.now().time() ) ## a check for me if the code is OK

