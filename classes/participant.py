# Class Participant
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
    att = ['_code','_name','_year','_phone'] # code é o up
    # Class header title
    header = 'Participants'
    # field description for use in, for example, in input form
    des = ['UP Number','Name','Year','Phone Number']
    # Constructor: Called when an object is instantiated
    def __init__(self,code,name,year,phone):
        super().__init__()
        # Object attributes
        self._code = str(code)
        self._name = name
        self._year = year
        self._phone = str(phone)
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
    def name(self):
        return self._name
    # year property getter method
    @property
    def year(self):
        return self._year
    # phone property getter method
    @property
    def phone(self):
        return self._phone
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # year property setter method
    @year.setter
    def year(self, year):
        self._year = int(year)
    # phone property setter method
    @phone.setter
    def phone(self, phone):
        self._phone = str(phone)
        
    def chk_validity(self):
        message = 'Approved!'
        # Verifica se o UP tem 9 digitos
        if len(self._code) != 9:
            message = 'UP must have 9 digits!'
            return message
        # Verifica se o telemóvel é um número
        if not self._year.isdigit():
            message = 'Year must be a number!'
            return message
        return message
    
    def chk_removal(self):
        message = 'Deleted!'
        from classes.registration import Registration
        for regist in Registration.obj.values():
            if self.code == regist.participant.code:
                message = 'Deletion not possible because this participant is\
                    registered in one or more events. Please delete their\
                    registrations first.'
                return message
        return message
        