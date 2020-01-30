# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:19:58 2020

@author: ADMIN
"""
import tkinter as t
from PyDictionary import PyDictionary
dictionary=PyDictionary()



def meaning():
    word=txt.get()
    m=dictionary.meaning(word)
    l2.configure(text=m,wraplength=500,highlightthickness=1)
    
    
   
main=t.Tk()
main.title("dictionary")

main.geometry("500x500")
l=t.Label(main,text="English dictionary",font=("times roman",25))
l.grid(column=1, row=0)
l2=t.Label(main,font=("Arial",12))
l2.grid(column=1, row=4)

txt = t.Entry(main,width=100)
txt.grid(column=1, row=1)
bt=t.Button(main,text='find meaning',command=meaning)
bt.grid(column=1, row=2)


main.mainloop()
