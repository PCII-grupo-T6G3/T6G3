# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:13:27 2024

@author: afons
"""

from datafile import filename

from classes.Venue import Venue

Venue.read(filename + 'project.db')

v1 = Venue('None', 'Pavilhão da Areosa', 'Areosa', '100')
print(v1)

print("objeto sem estar gravado ",v1)

Venue.insert(getattr(v1,Venue.att[0]))

v1 = Venue('None', 'Pavilhão da Areosa', 'Areosa', '100')
Venue.insert(getattr(v1,Venue.att[0]))


print("\nLista dos objetos gravados " ,Venue.lst)

#Alterar
v1 = Venue.first()
print ("\nPrimeiro objeto gravado ",v1)
v1.capacity = "25"
Venue.update(getattr(v1, Venue.att[0]))

Venue.read(filename + 'project.db')

print("\nobjectos gravados")    
for code in Venue.lst:
    print(Venue.obj[code])
    
Venue.reset()
Venue.read(filename + 'project.db')