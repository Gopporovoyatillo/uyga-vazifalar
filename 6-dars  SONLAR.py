# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:31:05 2021

@author: Admin

"""
#Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:

#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur


#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga
# chiqaruvchi dastur


#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi,
# ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur



#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
x = int(input("Istalgan son kiriting:\n>>>"))
print(x, " ning kvadrati ", x**2, " ga teng")
print(x, " ning kubi ", x**3, " ga teng")

# Foydalanuvchining yoshini so'rang, 
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring.
yosh = int(input("Yoshingiz nechida? \n>>>"))
t_yil = 2020-yosh
print("Siz ", t_yil, " da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, 
# kiritilgan sonlarning yig'indisi, ayirmasi, 
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)