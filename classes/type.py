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
    att = ['_code','_event_type'] # cada tipo de evento tem um codigo predefinido
    # Class header title
    header = 'Event Type'
    # field description for use in, for example, in input form
    des = ['Code','Event Type']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, event_type):
        super().__init__()
        # Object attributes
        self._code = str(code)
        self._event_type = event_type
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
    def event_type(self):
        return self._event_type
    @event_type.setter
    def event_type(self, tipo):
        self._type = tipo