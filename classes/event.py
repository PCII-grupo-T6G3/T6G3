# Class Event
# Import the generic class
from classes.gclass import Gclass
import datetime
from classes.venue import Venue
from classes.type import Type

class Event(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_date', '_time','_info','_slots','_venue_code','_type_code']
    att2 = ['_code','_name','_date','_time','_info','_slots','_venue_name','_type_name']
    # Class header title
    header = 'Events'
    # field description for use in, for example, in input form
    des = ['Code','Name','Date', 'Time','Description','Available Slots',\
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
        self._date = date
        self._time = time
        # dl = date.split('-')
        # for i in range(len(dl)):
        #     dl[i] = int(dl[i])
        # tl = time.split(':')
        # for i in range(len(tl)):
        #     tl[i] = int(tl[i])
        #self._dt = datetime.datetime(dl[2],dl[1],dl[0],tl[0],tl[1])
        
        self._info = info
        
        if venue_code in Venue.obj.keys():
            self._venue = Venue.obj[str(venue_code)]
            self._venue_code = venue_code
            self._venue_name = self._venue.name
        else:
            print('Venue not found!')
        if type_code in Type.obj.keys():
            self._type = Type.obj[str(type_code)]
            self._type_code = type_code
            self._type_name = self._type.name
        else:
            print('Type not found!')
            
        if int(slots) <= self._venue.capacity:
            self._slots = int(slots)
        else:
            while int(slots) > self._venue.capacity:
                slots = input('Venue not big enough for event slots! Try again: ')
            self._slots = int(slots)
                      
        self._used_slots = 0

        # Add the new object to the Event list
        Event.obj[code] = self
        Event.lst.append(code)
    # Object properties
    @property
    def code(self):
        return self._code
    @property
    def name(self):
        return self._name
    @property
    def date(self):
        return self._date
    @property
    def time(self):
        return self._time
    # dt property setter method
    # @dt.setter
    # def dt(self, date, time):
    #     dl = date.split('-')
    #     tl = time.split(':')
    #     self._dt = datetime.datetime(dl[2],dl[1],dl[0],tl[0],tl[1])
    
    @date.setter
    def date(self,data):
        self._date = data
    @time.setter
    def time(self,hora):
        self._time = hora
    # info property getter method
    @property
    def info(self):
        return self._info
    @property
    def slots(self):
        return self._slots
    @slots.setter
    def slots(self, slots):
        if int(slots) <= self._venue.capacity:
            self._slots = int(slots)
        else:
            while int(slots) > self._venue.capacity:
                slots = input('Venue not big enough for event slots! Try again: ')
            self._slots = int(slots)
    @property
    def venue_code(self):
        return self._venue_code
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
    
    # Overload do método str da Gclass para escrever
    # o nome do venue e do type em vez do código
    def __str__(self):
        strprint = "f'"
        for att2 in type(self).att2:
            strprint += '{self.' + att2 + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)
    
# v1 = Venue('None', 'Pavilhão da Areosa', 'Areosa', '100')
# print(v1)
# t1 = Type('01','Desporto')
# print(t1)
# e1 = Event('None','TAS','27-3-2024','11:00','Torneio de Futsal','8',\
# '1','01')
# print(e1)