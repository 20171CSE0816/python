# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:38:10 2020

@author: ADMIN
"""

import xlrd as xls


wb=xls.open_workbook("sequences.xlsx")
sheet=wb.sheet_by_index(0)
l=[]
n=sheet.nrows
for i in range(1,n):
    l.append(sheet.cell_value(i,2))
    l.append(sheet.cell_value(i,0))

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

friend=ChatBot('Friend')
train=ListTrainer(friend)
train.train(l)

ans=friend.get_response("hello")
print("hello")
print(ans)
while True:
    q=input("user:")
    if q=='exit':
        break
    else:
        ans=friend.get_response(q)
        print("friend :",ans)
        

''' 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer    

abot = ChatBot("vishal")
trainer = ListTrainer(abot)
# now training the abot with the help of trainer

trainer.train(l)

answer = abot.get_response("")
print(answer)
print("Talk to abot ")
while True:
  query = input()
  if query == 'exit':
        break
  answer = abot.get_response(query)
  print("abot : ", answer)
'''