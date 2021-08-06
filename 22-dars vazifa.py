# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:25:15 2021

@author: Admin
"""

def jamla(*jami):
    return sum(jami)
print(jamla(1,2,3,4,5))
print (jamla(4,5,6,7))
    

def info(x,y,**dalee):
    dalee["ismi"]=x
    dalee["familyasi "]=y
    return dalee

mal=info('oyatillo',"g'pporov",yoshi=23,kasbi="dasturchi")
print(mal)  
