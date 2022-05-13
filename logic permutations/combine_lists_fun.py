# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:51:52 2022

@author: 1
"""
def combine_lists (temp_list,excel_list):
    df = pd.DataFrame(temp_list)    
    temp_list = df.values.tolist()
    excel_list.extend(temp_list)
    
    
import pandas as pd
global excel_list,temp_list
excel_list = []

#Hebrew_word_lists = pd.read_excel('./Hebrew word lists/hebrew_most_1000.xlsx')
temp_list = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_most_1000.xlsx')
combine_lists(temp_list,excel_list)
temp_list  = pd.read_excel('D:/ET\MINE/תיכנות/python/logic permutations/Hebrew word lists/hebrew_bible.xlsx')
combine_lists(temp_list,excel_list)    
