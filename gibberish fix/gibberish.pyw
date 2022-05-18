# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:04:26 2022

@author: 1
"""

def on_going():
    
    def check(char):
        global key
        key =''
        # key = key.encode('utf-8')
        # print(type(key))
        # print((key))
        # key = key.decode('utf-8')
        # print(type(key))
        # print((key))
        #tcdsvuzjyhfknbxgpmera,oi;l.
        
        #tbh tuvc tu,l ta,h vherv' ntus / fh t, v-1 nfuki
      
        for char in string_to_iterate:
            if char == 'a':
                 key = key + ('ש')
                
            elif char == 'b':
                key =  key + 'נ'
            elif char == 'c':
                key = key + "ב"
            elif char == 'd':
                key = key + 'ג'
            elif char == 'e':
                key = key +  "ק"          
            elif char == 'f':
                key = key + "כ"            
            elif char == 'g':
                key = key + "ע"            
            elif char == 'h':
                key = key +  "י"            
            elif char == 'i':
                key = key + "ן"            
            elif char == 'j':
                key = key +  "ח"            
            elif char == 'k':
                key = key + "ל"          
            elif char == 'l':
                key = key +  "ך"        
            elif char == 'm':
                key = key +  "צ"  
            elif char == 'n':
                key =  key + 'מ'
            elif char == 'o':
                key = key + "ם"
            elif char == 'p':
                key = key + 'פ'
            elif char == 'q':
                key = key +  "/"          
            elif char == 'r':
                key = key + "ר"            
            elif char == 's':
                key = key + "ד"                     
            elif char == 't':
                key = key + "א"            
            elif char == 'u':
                key = key +  "ו"            
            elif char == 'v':
                key = key + "ה"          
            elif char == 'w':
                key = key +  "'"        
            elif char == 'x':
                key = key +  "ס"  
            elif char == 'y':
                key = key +  "ט"        
            elif char == 'z':
                key = key +  "ז"              
            elif char == ' ':
                key = key +  " "    
            elif char == "/":
                key = key +  "."  
            elif char == ";": 
                key = key +  "ף"    
            elif char == ",":
                key = key +  "ת"                          
            elif char == ".":
                key = key +  "ץ"   
            elif char == "'":
                key = key +  ","  
            elif char == "_":
                key = key +  "_"                  
            elif char == "1":
                key = key +  "1"    
            elif char == "2":
                key = key +  "2"                          
            elif char == "3":
                key = key +  "3"   
            elif char == "4":
                key = key +  "4"  
            elif char == "5":
                key = key +  "5"   
            elif char == "6":
                key = key +  "6"    
            elif char == "7":
                key = key +  "7"                          
            elif char == "8":
                key = key +  "8"   
            elif char == "9":
                key = key +  "9"  
            elif char == "0":
                key = key +  "0"                   
            elif char == "-":
                 key = key +  "-"  
            elif char == "!":
                key = key +  "!"    
            elif char == "@":
                key = key +  "@"                          
            elif char == "#":
                key = key +  "#"   
            elif char == "$":
                key = key +  "$"  
            elif char == "%":
                key = key +  "%"   
            elif char == "^":
                key = key +  "^"    
            elif char == "&":
                key = key +  "&"                          
            elif char == "*":
                key = key +  "*"   
            elif char == '(':
                key = key +  '(' 
            elif char == ')':
                key = key +  ')'  
            elif char == '"':
                 key = key +  '"' 
            elif char == '=':
                 key = key +  '='                  
            elif char == '+':
                 key = key +  '+'                  
            elif char == ':':
                 key = key +  ':'                    
            # elif char == "\":
            #      key = key +  "\" 
            else:
                return "Unknown status code"
         
    
    # copy marked string  # doesn't work while windows app mode
    shell.sendkeys('^c') # you just need to mark the word, and call the keyshort
    time.sleep(.25)

   # get clipboard data     
    win32clipboard.OpenClipboard()
    copied = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    #print (copied)
    
    string_to_iterate = copied
    check(string_to_iterate) # calling function 
    
    #set clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    #win32clipboard.SetClipboardText(str(key))
    win32clipboard.SetClipboardText(key, win32clipboard.CF_UNICODETEXT) #https://geeksqa.com/python-win32clipboard-not-working-for-unicode-characters
    #win32clipboard.SetClipboardText((key))
    
    
    win32clipboard.CloseClipboard()
    #print (key)
    
    # to set focus to the last window, whom the copy string was taken from
    # win32gui.ShowWindow(window_hwnd,5)
    # win32gui.SetForegroundWindow(window_hwnd) #To make last focused app windows active:
    # win32gui.SetActiveWindow(window_hwnd) 

# ctrl+v to paste     # doesn't work while windows app mode, because the window  focus was lost
    time.sleep(0.25)
    shell.sendkeys('^v') 
        
    import winsound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    

    
import win32clipboard
#import time import time import time import time 
import time
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell") 
# import win32gui
# window_hwnd = win32gui.GetForegroundWindow() # this will return a number(the hwnd of active window when it is running)

# change languge # # doesn't work
import py_win_keyboard_layout 
## https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/available-language-packs-for-windows?view=windows-11
# English
#py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409) 
# Hebrew
py_win_keyboard_layout.change_foreground_window_keyboard_layout(-264436723)  # to switch to Heb
 
    
on_going() 
