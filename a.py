# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:46:13 2024

@author: marti
"""
from classes.Event import Event
from classes.Venue import Venue
from classes.Type import Type

            
v1 = Venue('None', 'Pavilhão da Areosa', 'Areosa', '100')
print(v1)
t1 = Type('01','Desporto')
print(t1)
e1 = Event('None','TAS','27-3-2024','11:00','Torneio de Futsal','8',\
'1','01')
print(e1)

Event.read("data/project.db") 
Event.insert()