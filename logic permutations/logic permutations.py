# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:33:26 2022

@author: 1
"""

#%% 
## !!!!!!!!!!!
# to be exectue cell by cell


#%% 
## !!!!!!!!!!!
import time
from itertools import permutations
#%%
#from logic_permutations_input_box import E1 , E2 
#use logic_permutations_input_box for your own anagram
# or  pick one of the cells "works" below

import logic_permutations_input_box

## 0 for no word
# #for two words
# length=(the_org_string.split())
# x_length = len(length[1])
# y_length=len(the_org_string)-x_length-1 # -1 for space ' ' between the words

# x_length=2 #length of first word
# y_length= 4#length of second word

the_org_string=logic_permutations_input_box.E1
x_length =logic_permutations_input_box.E2
y_length =logic_permutations_input_box.E3 
print (x_length,the_org_string,y_length)


#%%  pick one of the cells below
## !!!!!!!!!!!

#%% # does not work because of מ
the_org_string='של מי רוי'
y_length =7 # ירושלים
x_length =0

#%% #works
the_org_string='של םי רוי'
y_length =7 # ירושלים
x_length =0
#%% #works
the_org_string='של מי רוי'
y_length =2 # של 
x_length =5 # 

#%% #works
the_org_string='ירי שלום'
y_length =7 # ירושלים
x_length =0
#%% #works
the_org_string='ירי שלום'
y_length =2 # של # supposed to jump in the loop 
x_length =5 # מורימי

#%% #works
the_org_string='ירי שלום'
y_length =3
x_length =4 #  שלום # supposed to jump in the loop 


#%% Doesn't work ???
the_org_string='ירושלים'
x_length =3
y_length =4 #  שלום # supposed to jump in the loop 
#%% Doesn't work ???
the_org_string='ירושלים'
y_length =2 # של # supposed to jump in the loop 
x_length =5 # מורימי

#%% #works
the_org_string='ירושלים'
y_length =0
x_length =7 #  ישרוםלי # 


#%% 
## !!!!!!!!!!!
#print (permutations(the_org_string, 2)) #makes a permutaions of the words in the length of 2
perms =list(permutations(the_org_string))  #makes a list of permutaions of the words in the length of the the_org_string
listy=list(([''.join(perms) for perms in perms])) # !!!!!!!!!!!!!!! makes a list of the words ONLY !!!!!!!!!!! in the length of the the_org_string
# how to  permutations python consist of number of valuse

# item = 'שלו םירי'
# item = 'םירי שלו'
# item = 'ירישו םל'
# item = 'שלי םירו'
#item = 'שלי םירו'
# item in listy

#%% check conditions 
# the_org_string='ירי שלום'
# y_length =2 # של # supposed to jump in the loop 
# x_length =5 # 

# item = 'ירישו םל'

# item in listy
# Out[87]: True

# item = 'םירי שלו'

# item in listy
# Out[89]: True


#  the_org_string='ירי שלום'
# y_length =3
# x_length =4 #  שלום # supposed to jump in the loop 

# item = 'ירישו םל'

# item in listy
# Out[98]: True

# item = 'שלו םירי'

# item in listy
# Out[100]: True

#  the_org_string='ירי שלום'
# y_length =7 # ירושלים
# x_length =0

# item = 'ירישו םל'
# item in listy
# Out[103]: True

# item = 'םירי שלו'

# item in listy
# Out[105]: True

#%% does the len(splited) is equell to x/y_length . ther is no need in other length of words
## !!!!!!!!!!!
 
#import pdb; pdb.set_trace() # debugging inside only one cell
final_list = [] # the list of all matches word that can be 
length = len(listy)
t = time.time()
# do stuff to take time

for i in range(len(listy)):
#for i in range(length):
    #final_list.extend(listy[i].split())
    splited= (listy[i].split()) # any list cell in listy may containe more than one word inside own cell
    #print (splited[2])
    if x_length==0 or y_length==0 : # can be dynamic if for several words, but it is not worth it to be done.
        # for one word only  to be found
        if (len(splited[0])==x_length) or (len(splited[0])==y_length):  
            final_list.append(splited)
    else:
        # two words to be found
        #if (len(splited[0])==x_length)  and (len(splited[1])==y_length) :
        # #shouldn't it be
        if ((len(splited[0])==x_length)  and (len(splited[1])==y_length)) or ((len(splited[0])==y_length)  and (len(splited[1])==x_length)) :
        # or is it mirror option 
            #print (splited)
            final_list.append(splited)        


elapsed = time.time() - t
print (elapsed)
       
 #%% save into excell
 # import pandas as pd
 # df = pd.DataFrame(final_list)
 # writer = pd.ExcelWriter('final_list.xlsx', engine='xlsxwriter')
 # df.to_excel(writer, sheet_name='final_list', index=False)
 # writer.save()
 # writer.close()

#%% compare the final_list to dictionaries-word-lists in Hebrew 
#https://github.com/NNLP-IL/Resources#dictionaries-word-lists

#%% reading excell
## !!!!!!!!!!! 

def combine_lists(temp_list,excel_list): # must be at the same cell (? ) - maybe not when run time i.e. F5
    df = pd.DataFrame(temp_list)    
    temp_list = df.values.tolist()
    excel_list.extend(temp_list)
    
import pandas as pd
global excel_list,temp_list
excel_list = [] # the list from the excel files

#temp_list = pd.read_excel('./Hebrew word lists/hebrew_most_1000.xlsx')
temp_list = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_most_1000.xlsx')
combine_lists(temp_list,excel_list)
# temp_list  = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_bible.xlsx')
# combine_lists (temp_list,excel_list)
# temp_list  = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_first_names.xlsx')
# combine_lists (temp_list,excel_list)
# temp_list  = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_last_names.xlsx')
# combine_lists (temp_list,excel_list)
# temp_list  = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_stopwords.xlsx')
# combine_lists (temp_list,excel_list) 
# temp_list  = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_toar.xlsx')
# combine_lists (temp_list,excel_list) 

#Hebrew_word_lists = pd.read_excel('./Hebrew word lists/hebrew_most_1000.xlsx')
##df = pd.DataFrame(temp_list.head())
# df = pd.DataFrame(temp_list)
# excel_list = df.values.tolist()
# print(excel_list)
#%% stupid compare the final_list to excel_list
## !!!!!!!!!!! 
matcehs_list = []
#import pdb; pdb.set_trace() # debugging only one cell
# excel_list[i] * final_list[i] loop itarations are too long.....
for j in range(len(excel_list)):
    #print (excel_list[j])
    for i in range(len(final_list)):
        #print (excel_list[j],' ',str(final_list[i][0]) )
        #print (', '.join(excel_list[j]))
        if (', '.join(excel_list[j])== final_list[i][0]) :# for only one word
        #if (excel_list[j]== final_list[i][1]) or (excel_list[j]== final_list[i][0]):# for two words # I think I don't need the or because there are multiplication RESULTS IN final_list
            #print (excel_list[j])
            matcehs_list.append (excel_list[j])
            #print (', '.join(excel_list[j])
print (matcehs_list)

#%% compact the matcehs_list
myset = set(matcehs_list)
print(myset)
## TypeError: unhashable type: 'list'

#%% save in excell file matcehs_list.xlsx the matcehs_list
## !!!!!!!!!!!
import pandas as pd
df = pd.DataFrame(matcehs_list)
writer = pd.ExcelWriter('matcehs_list.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='matcehs_list', index=False)
writer.save()
#writer.close()


