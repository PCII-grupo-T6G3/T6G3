# Event Type
# Import the generic class
from classes.gclass import Gclass

class Participant(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_type'] # cada tipo de evento tem um codigo predefinido
    # Class header title
    header = 'Event Type'
    # field description for use in, for example, in input form
    des = ['Code','Event Type']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,eventtype):
        super().__init__()
        # Object attributes
        self._code = code
        self._type = eventtype
        # Add the new object to the Participant list
        Participant.obj[code] = self
        Participant.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def eventtype(self):
        return self._type

    @eventtype.setter
    def eventtype(self, tipo):
        self._type = tipo
