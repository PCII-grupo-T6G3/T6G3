# Class Feedback

from classes.gclass import Gclass
from classes.registration import Registration
from classes.event import Event
from classes.participant import Participant

class Feedback(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_registration_code', '_feedback']
    # Class header title
    header = 'Feedback'
    # field description for use in, for example, in input form
    des = ['Ticket code', 'Feedback']

    def __init__(self, registration_code, feedback):
        super().__init__()
        
        # verifica integridade do evento e do participante
        if registration_code in Registration.lst:
            self._feedback = feedback
            self._registration_code = registration_code
            Feedback.obj[self._registration_code] = self
            Feedback.lst.append(self._registration_code)
        else:
            print('Ticket', registration_code, 'not found')

    @property
    def registration_code(self):
        return self._registration_code
    @property
    def feedback(self):
        return self._feedback
