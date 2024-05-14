# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:46:13 2024

@author: afons
"""

from datafile import filename
from classes.userlogin import Userlogin

Userlogin.read(filename + 'project.db')

print("\nLista dos objetos gravados " ,Userlogin.lst)

adm = Userlogin('amcs','admin','123')
adm.set_password('321')
print('user antes de gravar', adm)

Userlogin.insert(getattr(adm,Userlogin.att[0]))

print("\nLista dos objetos gravados " ,Userlogin.lst)

# Userlogin.remove(getattr(adm,Userlogin.att[0]))

# Userlogin.read(filename + 'project.db')

# print("\nLista dos objetos gravados " ,Userlogin.lst)