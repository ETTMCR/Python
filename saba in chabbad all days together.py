# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:28:02 2022

@author: 1
"""    
from requests_html import HTMLSession
import nest_asyncio
nest_asyncio.apply()
session = HTMLSession()

month = list(range(1, 13))
day = list(range(1, 31))
# https://col.org.il/events/3/33364?y=5782&m=6&d=7 #פלסר 
url1='https://col.org.il/events/3/33364?y=5782&m='
url2='&d='
filename = 'who.txt' # option - suffix the name of article in the file name

# all_url = url1 + month +  url2 + day
for x in month:
    for y in day:
      all_url = url1 + str(x) +  url2 + str(y)
      #print(all_url)      
      r = session.get(all_url)
      html_str = r.text
      
      #does = html_str.find('פלסר') #רבי אברהם אבא אבלי אוסישקין סבא רבא רבא רבא שלי1
      #does = html_str.find('אבא')
      does = html_str.find('אוסישקין') # output  - https://col.org.il/events/3/33364?y=5782&m=8&d=20

      if does > -1 :
          with open(filename,'a',encoding='utf8') as file1:
              file1.write(all_url)
              file1.write('\n') # new line writln ;-)
              file1.close()
              print(all_url)
              


# s  = HTMLSession()
# response = s.get(url)
# response.html.render()
#print(response)


 
#print(html_str.find('חומוס'))

#print(html_str)
# prints out fully loaded page content      