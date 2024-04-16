# Class Event
# Import the generic class
from classes.gclass import Gclass
import datetime
from classes.Venue import Venue
from classes.Type import Type

class Event(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_dt','_info','_slots','_venue_code','_type_code']
    # Class header title
    header = 'Events'
    # field description for use in, for example, in input form
    des = ['Code','Name','Date and Time','Description','Available Slots',\
           'Venue','Type']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, date, time, info, slots, venue_code, type_code):
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
        for i in range(len(dl)):
            dl[i] = int(dl[i])
        tl = time.split(':')
        for i in range(len(tl)):
            tl[i] = int(tl[i])
        self._dt = datetime.datetime(dl[2],dl[1],dl[0],tl[0],tl[1])
        self._dt = str(self._dt)
        self._info = info
        self._slots = int(slots)
        
        if venue_code in Venue.obj.keys():
            self._venue_code = Venue.obj[str(venue_code)]
        else:
            print('Venue not found!')
        if type_code in Type.obj.keys():
            self._type_code = Type.obj[str(type_code)]
        else:
            print('Type not found!')

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
        self._dt = datetime.datetime(dl[2],dl[1],dl[0],tl[0],tl[1])
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
    @property
    def venue_code(self):
        return self._venue
    @venue_code.setter
    def venue_code(self, venue_code):
        if venue_code in Venue.obj.keys():
            self._venue = Venue.obj[str(venue_code)]
        else:
            print('Venue not found!')
    @property
    def event_type(self):
        return self._event_type
    @event_type.setter
    def event_type(self, type_code):
        if type_code in Type.obj.keys():
            self._event_type = Type.obj[str(type_code)]
        else:
            print('Type not found!')
            
v1 = Venue('None', 'Pavilhão da Areosa', 'Areosa', '100')
print(v1)
t1 = Type('01','Desporto')
print(t1)
e1 = Event('None','TAS','27-3-2024','11:00','Torneio de Futsal','8',\
'1','01')
print(e1)