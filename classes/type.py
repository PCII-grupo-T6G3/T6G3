# Event Type
# Import the generic class
from classes.Gclass import Gclass

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
        flag = False
        while not flag:
            if code not in Type.lst:
                self._code = str(code)
                self._type_name = type_name
                # Add the new object to the Participant list
                Type.obj[code] = self
                Type.lst.append(code)
                flag = True
            else:
                print('Code already used!')
                code = input('New code: ')
    # Object properties
    @property
    def code(self):
        return self._code
    @property
    def name(self):
        return self._type_name
    @name.setter
    def name(self, tipo):
        self._type = tipo