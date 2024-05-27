# Class Event
# Import the generic class
from classes.gclass import Gclass
from datetime import datetime as dt
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
    att = ['_code','_name','_date','_time','_info','_slots','_venue_code','_type_code']
    att2 = ['_code','_name','_date','_time','_info','_slots','_venue_code','_type_code','_used_slots']
    # Class header title
    header = 'Events'
    # field description for use in, for example, in input form
    des = ['Code','Name','Date (dd-mm-yyyy)', 'Time (hh:mm)','Description',\
           'Available Slots','Venue Code','Type Code']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, date, time, info, slots, venue_code, type_code, used_slots=0):
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
        self._info = info
        self._date = date
        self._time = time
        
        self._venue_code = venue_code
        self._venue = ''
        self._type_code = type_code
        self._type = ''
        self._slots = int(slots)
        
        self._used_slots = int(used_slots)

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
    @date.setter
    def date(self, data):
        self._date = data
    @time.setter
    def time(self, hora):
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
        self._slots = int(slots)
    @property
    def venue_code(self):
        return self._venue_code
    @venue_code.setter
    def venue_code(self, venue_code):
        self._venue_code = venue_code
    @property
    def venue_name(self):
        return Venue.obj[self.venue_code].name
    @property
    def type_code(self):
        return self._type_code
    @type_code.setter
    def type_code(self, type_code):
        self._type_code = type_code
    @property
    def type_name(self):
        return Type.obj[self.type_code].name
    @property
    def used_slots(self):
        return self._used_slots
    @used_slots.setter
    def used_slots(self, used_slots):
        self._used_slots = int(used_slots)
    @property
    def remaining_slots(self):
        return self._slots - self._used_slots
    
    # Overload do método str da Gclass para escrever
    # o nome do venue e do type em vez do código
    # def __str__(self):
    #     strprint = "f'"
    #     for att2 in type(self).att2:
    #         strprint += '{self.' + att2 + '};'
    #     strprint = strprint[:-1] + "'"
    #     return eval(strprint)
    
    @staticmethod
    def is_date(string):
        try:
            dt.strptime(string, '%d-%m-%Y')
            return True
        except ValueError:
            return False
    @staticmethod
    def is_time(string):
        try:
            dt.strptime(string, '%H:%M')
            return True
        except ValueError:
            return False
    
    def chk_validity(self):
        message = 'Approved!'
        # Verifica data
        if not Event.is_date(self._date):
            message = 'Date not inserted correctly!'
            return message
        if not Event.is_time(self._time):
            message = 'Time not inserted correctly!'
            return message
        # Verifica o espaço do evento
        if self._venue_code in Venue.obj.keys():
            self._venue = Venue.obj[str(self._venue_code)]
        else:
            message = 'Venue not found!'
            return message
        # Verifica o tipo do evento
        if self._type_code in Type.obj.keys():
            self._type = Type.obj[str(self._type_code)]
        else:
            message = 'Type not found!'
            return message
        # Verifica se o número de slots é superior à capacidade do espaço
        if int(self._slots) <= self._venue.capacity:
            self._slots = int(self._slots)
        else:
            message = "The selected venue isn't big enough!"
            return message
        return message