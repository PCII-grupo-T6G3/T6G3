# Class Registration
from classes.gclass import Gclass
from classes.participant import Participant
from classes.event import Event

class Registration(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_registration_code', '_event_code', '_participant_code']
    # Class header title
    header = 'Registration'
    # field description for use in, for example, in input form
    des = ['Event code', 'Participant code']

    def __init__(self, event_code, participant_code):
        super().__init__()
        
        # verifica integridade do evento e do participante
        if participant_code in Participant.lst and event_code in Event.lst:
            self._event_code = event_code
            self._participant_code = participant_code
            self._registration_code = event_code + participant_code
            Registration.obj[self._registration_code] = self
            Registration.lst.append(self._registration_code)
        elif participant_code not in Participant.lst and event_code in Event.lst:
            print('Participant ', participant_code, ' not found')
        elif participant_code in Participant.lst and event_code not in Event.lst:
            print('Event ', event_code, ' not found')
        else:
            print('Event', event_code, 'and participant', participant_code, 'not found')

    @property
    def event_code(self):
        return self._event_code
    @property
    def participant_code(self):
        return self._participant_code
    @property
    def registration_code(self):
        return self._registration_code
    
# Coisas que mudámos da classe do professor:
# 1. juntámos os códigos das classes evento e participante
# 2. verificámos a integridade para ambos o evento e o participante
# 3. não incluímos um setter para os códigos do evento e do participante