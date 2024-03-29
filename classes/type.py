# Event Type
# Import the generic class
from classes.gclass import Gclass

class Type(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_type_name'] # cada tipo de evento tem um codigo predefinido
    # Class header title
    header = 'Event Type'
    # field description for use in, for example, in input form
    des = ['Code','Type Name']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, type_name):
        super().__init__()
        # Object attributes
        self._code = str(code)
        self._type_name = type_name
        # Add the new object to the Participant list
        Type.obj[code] = self
        Type.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def type_name(self):
        return self._type_name
    @type_name.setter
    def type_name(self, tipo):
        self._type = tipo