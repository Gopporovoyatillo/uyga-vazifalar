# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 23:21:57 2021

@author: Admin
"""
#Topingchi, quyidagi kod qanday vazifani bajaradi?
#list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))


mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar2=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar2)

#boshi a harfili va oxiri r harifli bo'lgan so'zlarni consolga chiqaradi 
