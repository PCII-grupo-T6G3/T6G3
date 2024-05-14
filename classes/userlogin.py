# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2022)
#objective: class Person
"""""
#%% Class User - generic version
# import sys
import bcrypt
# Import the generic class
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_user','_usergroup','_password']
    # Class header title
    header = 'Users'
    # field description for use in, for example, in input form
    des = ['User','User group','Password']
    username = ''
    # Constructor: Called when an object is instantiated
    def __init__(self, user, usergroup, password):
        super().__init__()
        # Object attributes
        self._user = user
        self._usergroup = usergroup
        self._password = password
        # Add the new object to the dictionary of objects
        Userlogin.obj[user] = self
        # Add the code to the list of object codes
        Userlogin.lst.append(user)

    # code property getter method
    @property
    def user(self):
        return self._user
    # name property getter method
    @property
    def usergroup(self):
        return self._usergroup
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
        
    @property
    def password(self):
        return ""
    
    @password.setter
    def password(self, password):
        self._password = password

    @classmethod
    def chk_password(self, user, password):
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            message = "Valid"
            if not valid:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()