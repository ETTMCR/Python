# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:04:26 2022

@author: 1
"""
# true=1
# while true==1:
#while(True):   
def on_going():
    
    def check(char):
        global key
        key ='ש'
        key =''
        # key = key.encode('utf-8')
        # print(type(key))
        # print((key))
        # key = key.decode('utf-8')
        # print(type(key))
        # print((key))
        #tcdsvuzjyhfknbxgpmera,oi;l.
        
        #tbh tuvc tu,l ta,h vherv' ntus /
        
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
            # elif char == "_":
            #     key = key +  "_"                   
            else:
                return "Unknown status code"
       
    from pynput.keyboard import Key, Controller
    
    keyboard = Controller()
    
    import win32clipboard
    
    #set clipboard data
    
    
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
    
    with keyboard.pressed(Key.ctrl.value): # ctrl+v to paste
        keyboard.press('v')
        keyboard.release('v')
        
    import winsound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
on_going() 