# Class Event
# Import the generic class
from classes.gclass import Gclass
import datetime

class Event(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_datetime','_info','_slots']
    # Class header title
    header = 'Events'
    # field description for use in, for example, in input form
    des = ['Code','Name','Date and Time','Description','Available Slots']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, date, time, info, slots):
        super().__init__()
        # Uncomment in case of auto number on
        if code == 'None':
            codes = Event.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int,Event.getatlist('_code'))) + 1)
        # Object attributes
        self._code = code
        self._name = name
        dl = date.split('-')
        tl = time.split(':')
        self._dt = datetime.datetime(dl[2],dl[1],dl[0],tl[0],tl[1],tl[2])
        self._info = info
        self._slots = int(slots)
        # Add the new object to the Event list
        Event.obj[code] = self
        Event.lst.append(code)
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # dt property getter method
    @property
    def dt(self):
        return self._dt
    # dt property setter method
    @dt.setter
    def dt(self, date, time):
        dl = date.split('-')
        tl = time.split(':')
        self._dt = datetime.datetime(dl[2],dl[1],dl[0],tl[0],tl[1],tl[2])
    # info property getter method
    @property
    def info(self):
        return self._info
    # info property setter method
    @info.setter
    def info(self, info):
        self._info = info
    @property
    def slots(self):
        return self._slots
    @slots.setter
    def slots(self, slots):
        self._slots = slots