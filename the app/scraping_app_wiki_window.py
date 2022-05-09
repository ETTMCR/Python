# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:23:39 2022

@author: 1
"""

"""
to be improved
* to be on tray
* to excel all txt files
* managing time of check - GUI check box, and even more beutiful toggle button
* without using chromedriver.exe
* single file for the scraping
* tooltip https://www.codegrepper.com/code-examples/whatever/tkinter+tooltip
"""

import glob
import os
import webbrowser

from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
#from tkinter import messagebox as showinfo




root = Tk()
root.title(' how many Wiki app')
#root.title('Wikiepdia platgorm to check how many people have watch specific article')
root.geometry('{}x{}'.format (380, 500))#(410, 450))
root.resizable(height = 0, width = 0)

# import tkinter as tk
# root = tk.Tk()

root.iconbitmap('icon/icony.ico')
#root.iconphoto(False, PhotoImage(file='icon/OOjs_UI_icon_logo-wikipedia.ico'))

# create all of the main containers
center = Frame(root, bg='gray2', width=590, height=590, padx=3, pady=3) # withou tgl button

# layout all of the main containers
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=0)

center.grid(row=1, sticky="nsew") # ORG nsew

# create the center black line widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue4', width=295, height=590, padx=25, pady=50)
ctr_right = Frame(center, bg='blue2', width=295, height=590, padx=25, pady=50)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_right.grid(row=0, column=4, sticky="ns")

# create right sub widgets
ctr_right.grid_rowconfigure(1, weight=1)
ctr_right.grid_columnconfigure(0, weight=1)

right_0 = Frame(ctr_right, bg='yellow', width=295, height=194)
right_1 = Frame(ctr_right, bg='red', width=295, height=194)
right_2 = Frame(ctr_right, bg='purple', width=295, height=194)
right_3 = Frame(ctr_right, bg='blue', width=295, height=194)
right_4 = Frame(ctr_right, bg='blue', width=295, height=194)
# right_5 = Frame(ctr_right, bg='blue', width=295, height=194)

right_0.grid(row=0, column=0, sticky="ew")
right_1.grid(row=1, column=0, sticky="ew")
right_2.grid(row=2, column=0, sticky="ew")
right_3.grid(row=3, column=0, sticky="ew") 
right_4.grid(row=4, column=0, sticky="ew") 
# right_5.grid(row=5, column=0, sticky="ew") 



#
def build_listbox():
#

# Creates Listbox of existing subjects, from .txt files in directory of program
    global subjects
    subjects = Listbox(ctr_left,
                       width=20,
                       height=20) #how many rows in the list to be set 
    for this_file in glob.glob("how_many*.txt"): # how_many_* with suffix, as made in the file final_new_method_suffix.py
        splited=this_file.split('.')[0]
        subjects.insert(0, splited[9:])
        
    subjects.grid(column=0, row=0, sticky="e")
    subjects.anchor='center'
    #myTip = Hovertip(subjects,'Double click to check')
    #myTip = CreateToolTip(subjects,'Double click to check')
    # tip = ListboxToolTip(subjects, ["Hello", "world"])
    text = Label(ctr_left, text=f"There are {subjects.size()} articles", bg='yellow',padx=0,pady=0,font = ("Helvetica", 10, 'bold'))
    #text = Label(root, text=f"There are {subjects.size()} articles to be checked", bg='yellow')
    text.place(x=0,y=-20)
    #subjects.tag_configure('tag-right', justify='right')

def about():
    ttl ='about'
    msg = 'Managing the how_many txt files \n elirantal1985@gmail.com'

    showinfo(
        title=ttl,
        message=msg,
        #detail = askquestion,
        icon = 'info') # to ensure that indexed item is selected
    
    # MsgBox = messagebox.askquestion (ttl,msg,icon = 'question') 

def exitme():
    # import sys
    #sys.exit()
    ttl ='EXIT'
    msg = 'Do you want to exit the program ? '

    MsgBox = messagebox.askquestion (ttl,msg,icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()
        raise SystemExit
    else:
        return

def open_folder():
    path =  os.getcwd()
    os.startfile(path)

def Heb_Eng_check(selected_arti):
    #### option to check the languge in order to handle also english articles
    import langid # very big directory
    lng = langid.classify(selected_arti)
    #('en', -0.19649028778076172)
    #print(lng[0])   
    if (lng[0]) =='he': 
        global lang_is
        lang_is='Heb'
        #url='https://he.wikipedia.org/w/index.php?title=' + article + '&action=info'
    else:
        lang_is='Eng'
        #url='https://en.wikipedia.org/w/index.php?title=' + article + '&action=info'
    
def new_article():    
    ttl ='adding new article'
    #msg = f'Do you want to add this article {selected_arti} to be checked ? '
    msg = 'Do you want to add a new article to be checked ? '

    # showinfo(
    #     title=ttl,
    #     message=msg,
    #     #detail = askquestion,
    #     icon = 'question') # to ensure that indexed item is selected
    
    MsgBox = messagebox.askquestion (ttl,msg,icon = 'question') 
    if MsgBox == 'yes':
        import only_first_time1 # py file
        #import input_box_article1
        build_listbox() #refresh the listbox
    else:
        return

def exe_file(selected_arti):

    # save selected_arti in new part in memory / to_check_now.txt file
    filename = 'to_check_now.txt' # f'to_check_now_{selected_arti}.txt' -  NO NEED !
    with open(filename, 'w') as file1:
        file1.write(selected_arti)
        #file1.write('\n') # new line writln ;-)  
        file1.close()
    # call final_new_method_suffix need to read that file first line
    import final_new_method_suffix_to_check
    
def open_file(selected_arti):
# open the how_many_{selected_arti}.txt, then you can edit, and watch entire history
    # showinfo(
    #     title='Information',
    #     message=selected_arti) # to ensure that indexed item is selected
    
    ttl =f'open how_many_{selected_arti}'
    msg = f'Do you want to open this file: how_many_{selected_arti}.txt ? '
    
    MsgBox = messagebox.askquestion (ttl,msg,icon = 'question') 
    if MsgBox == 'yes':
        osCommandString = f'notepad.exe how_many_{selected_arti}'
        os.system(osCommandString)
    else:
        return


def delete_file(selected_arti):
    ttl =f'delete how_many_{selected_arti}'
    msg = f'Do you want to delete this file: how_many_{selected_arti}.txt ? '

    MsgBox = messagebox.askquestion (ttl,msg,icon = 'warning')
    if MsgBox == 'yes':
        osCommandString = f'how_many_{selected_arti}.txt'
        #os.remove(osCommandString)
        if os.path.exists(osCommandString):
            os.remove(osCommandString)
            subjects.delete(selected_indices)
            build_listbox()
        else:
            print("The file does not exist")
        # remove from listbox
    else:
        return
 
def open_article(selected_arti):
    # in the {selected_arti} in the default browser
    ttl =f'open wiki article {selected_arti}'
    msg = f'Do you want to open the article {selected_arti} in the internet browser? '

    MsgBox = messagebox.askquestion (ttl,msg,icon = 'question')
    if MsgBox == 'yes':
        #global selected_arti
        Heb_Eng_check(selected_arti)
        if lang_is == 'Heb' :
            a_website = f'https://he.wikipedia.org/wiki/{selected_arti}'
        else: # lang_is == 'Eng'
            a_website = f'https://en.wikipedia.org/wiki/{selected_arti}'
            
        try:
            # Open url in a new page (“tab”) of the default browser, if possible
            webbrowser.open_new_tab(a_website) # webbrowser.open(a_website, 2)
        finally:
            # Open url in a new window of the default browser, if possible
            webbrowser.open_new(a_website) # webbrowser.open(a_website, 1)
    else:
        return    

my_menu = Menu(root)
root.config(menu=my_menu)

fileMenu = Menu(my_menu)
fileMenu.add_command(label="open folder" ,command=open_folder )

fileMenu.add_command(label="Exit",  command= exitme)
fileMenu.add_separator()
fileMenu.add_command(label="About", command=about)
my_menu.add_cascade(label="File", menu=fileMenu)

# editMenu = Menu(menu)
# my_menu.add_cascade(label="Edit", menu=editMenu)

## icon to main menu 
##https://stackoverflow.com/questions/38567830/is-it-possible-to-have-icon-in-tkinter-menubar-in-python
# import os
# root.MyImage,root.dictImg={},{}
# root.ypath=os.path.dirname(__file__)
# #root.ypath=os.path.abspath(__file__) #'D:\ET\MINE\תיכנות\python\scraping app\the app' #path
# #root.ypath="C:\Users\1\Desktop"
# root.dictImg[0]='img0.png' #png
# root.MyImage['Option'] =PhotoImage(file=root.ypath+os.sep+root.dictImg[0])
# root.my_menu.fileMenu.wierdones.add_command(label='Option',image=root.MyImage['Option'],compound='left')


build_listbox()

# this should be in the file_new_method of checking new article
# from tkinter import simpledialog
# root.withdraw()
# # the input dialog
# USER_INP = simpledialog.askstring(title="new article",
#                                   prompt="What article in wikipedia you want to scrap ?")

# Creates a "add article" button
btn_add_article = Button(right_3,
                      text='Add new article',
                      command=lambda: new_article(),
                      width=20,
                      height=3)
btn_add_article.grid(column=0, row=0, sticky="e")

# Creates an "open file" button
btn_open_file = Button(right_1,
                    text='Open "how_many_XYX.txt"',
                    command=lambda: open_file(selected_arti),
                    width=20,
                    height=3)
btn_open_file.grid(column=0, row=0, sticky="e")


# Creates an "open article" button
btn_open_article = Button(right_2,
                    text='Open article web page',
                    command=lambda: open_article(selected_arti),
                    width=20,
                    height=3)
btn_open_article.grid(column=0, row=0, sticky="e")

# Creates a button for deleting the subject in the Listbox
btn_delete_file = Button(right_4,
                        text='Delete article file',
                        command=lambda: delete_file(selected_arti),
                        #accelerator="Ctrl+Q",
                        width=20,
                        height=3)
btn_delete_file.grid(column=0, row=0, sticky="e")

#Bind the Keyboard shortcut Key
#btn_delete_file.bind('<Control-d>',delete_file(selected_arti))
btn_delete_file.bind('<Control-d>', lambda event: delete_file(selected_arti))

# Creates a button for execute the file in the Listbox
btn_exe_file = Button(right_0,
                        text='Check how many watch',
                        command=lambda: exe_file(selected_arti),
                        width=20,
                        height=3)
btn_exe_file.grid(column=0, row=0, sticky="e")

# Creates a button for 
# btn_ = Button(right_5,
#                         text='to be continue',
#                         command=lambda: exe_file(selected_arti),
#                         width=20,
#                         height=3)
# btn_.grid(column=0, row=0, sticky="e")

# handle event

def items_selected(event):
    """ handle item selected event
    """
    # get selected indices
    global selected_indices
    selected_indices = subjects.curselection()
    # get selected items
    global selected_arti
    selected_arti = ",".join([subjects.get(i) for i in selected_indices])
    print(f"{selected_arti}")

subjects.bind('<Double-Button-1>', lambda event: exe_file(selected_arti))
subjects.bind('<<ListboxSelect>>', items_selected)

#def tgl_btn
# Keep track of the button state on/off
#global is_on
is_on = True

# Create Label
# my_label = Label(root,
# # 	text = "The Switch Is On!",
# # 	fg = "green",
#  	font = ("Helvetica", 32))
# #my_label.grid(pady = 20)
# my_label.grid(column=0, row=0, sticky="w")


# # Define tgl switch btn function

# def switch():
# 	global is_on
# 	
# 	# Determine is on or off
# 	if is_on:
# 		on_button.config(image = off)
# # 		my_label.config(text = "auto",
# # 						fg = "grey")
#         #import set_daily # set to checl any of the articles, daily
# 		is_on = False
# 	else:
# 	
# 		on_button.config(image = on)
# # 		my_label.config(text = "The Switch is On", fg = "green")
# 		is_on = True
# # Define Our Images
# on = PhotoImage(file = "on.png")
# off = PhotoImage(file = "off.png")
# # Create a Button
# on_button = Button(root, image = on, bd = 0,
# 				command = switch) #
# on_button.grid(pady = 0)
# on_button.grid(column=0, row=0, sticky="w")



root.mainloop()