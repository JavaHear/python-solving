# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:00:52 2021

@author: User
"""

dostlar = ['rustam','zohit','behzod']
for dost in dostlar:
    print(f"hurmatli dositim  {dost.title()} sizni toyimga taklif etaman")
    print('hurmat bilan Javohir')
   
sonlar = list(range(1, 11))
for son in sonlar:
       print(f"{son} ning kvadirati {son**2} ga teng")
 
sonlar = list(range(11))
kv = []
for son in sonlar:
    kv.append(son**2)
    print(sonlar)
    print(kv)

x = []
print('5 ta dostingizni kiriting???')
for y in range(5):
    print(input(f"{y+1}- dostingizni ismini kiriting: "))
print(y)