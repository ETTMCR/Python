import tkinter as tk
global How_many_words , E1,E2,E3
# to make it combobox 
# to make it dynamic for How_many_words , and then open the relevant number of  input text box 
def add_word():
    How_many_words = e4.get()
    print (int(e4.get()))
    #https://stackoverflow.com/questions/14804735/tkinter-how-can-i-dynamically-create-a-widget-that-can-then-be-destroyed-or-rem
    
def show_entry_fields():
    print("The anagram: %s\nFirst Name: %s\nLast Name: %s" % (e1.get(),e2.get(), e3.get())) #(E1,E2,E3))#

def master_quit():
    global How_many_words , E1,E2,E3

    E1=e1.get()
    E2=e2.get()
    E3=e3.get()
    master.quit()
    
    
master = tk.Tk()
tk.Label(master, 
         text="The anagram").grid(row=0)#the_org_string
tk.Label(master, 
         text="First word length").grid(row=1)#x_length
tk.Label(master, 
         text="Last word length").grid(row=2)#y_length
tk.Label(master, 
         text="How many words").grid(row=3)  # can be dynamic button for more words, but it is not worth it.

e1 = tk.Entry(master)#"The anagram").grid(row=0)#the_org_string
e2 = tk.Entry(master)#First word length = x_length
e3 = tk.Entry(master)#last word length = y_length
e4 = tk.Entry(master)#

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

tk.Button(master, 
          text='Quit', 
          command=master_quit ).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(master, 
          text='V', command=add_word).grid(row=3, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)                                                       

    
tk.mainloop()