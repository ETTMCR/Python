# -*- coding: utf-8 -*-
"""
Created on Sun May  8 14:36:39 2022

@author: 1
"""

done = False
import tkinter as tk1

#global pad_more
pad_more = 30

root1= tk1.Tk()
root1.iconbitmap('icon/icony.ico')
canvas1 = tk1.Canvas(root1, width = 200, height = 100)
canvas1.pack()

entry1 = tk1.Entry (root1) 
canvas1.create_window(100, 20+pad_more, window=entry1) #place of input box

def getarticle (): 
    global new_article
    new_article = entry1.get()
    # label1 = tk.Label(root, text= float(article)**0.5)
    # canvas1.create_window(100,80+pad_more, window=label1) #place of label to be displeyd
    #print(article)
    done=True
    #import only_first_time1.here 
    root1.destroy()

label2 = tk1.Label(root1, text= "what wikipedia article to be watch ?")    
canvas1.create_window(100,0+pad_more, window=label2)

button1 = tk1.Button(root1,text='OK', command=getarticle)
canvas1.create_window(100,50+pad_more, window=button1)  #place of button


# def rest(article):
#    root.destroy
#    #import only_first_time#(article)
#    #return
#    #root.destroy()

root1.mainloop()

if not done  :
    root1.mainloop()
else:
    quit()


