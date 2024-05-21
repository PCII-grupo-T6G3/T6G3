# Class Registration
from classes.gclass import Gclass
from classes.participant import Participant
from classes.event import Event
from classes.venue import Venue
from classes.type import Type

class Registration(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 2
    # class attributes, identifier attribute must be the first one on the list
    att = ['_event_code', '_participant_code']
    # Class header title
    header = 'Registration'
    # field description for use in, for example, in input form
    des = ['Event code', 'Participant code']

    def __init__(self, event_code, participant_code):
        super().__init__()
        
        self._event_code = event_code
        self._participant_code = participant_code
        self._ticket = event_code + participant_code
        
        # Add the new object to the Event list
        Registration.obj[event_code] = self
        Registration.lst.append(event_code)

    @property
    def event_code(self):
        return self._event_code
    @property
    def participant_code(self):
        return self._participant_code
    @property
    def ticket(self):
        return self._ticket
    
    def chk_validity(self):
        message = f'Registration successful!\nYour ticket number: {self._ticket}'
        # Verifica o evento
        if self._event_code in Event.obj.keys():
            self._event = Event.obj[str(self._event_code)]
        else:
            message = 'Event not found!'
            return message
        # Verifica o participante
        if self._participant_code in Participant.obj.keys():
            self._participant = Participant.obj[str(self._participant_code)]
        else:
            message = 'Participant not found!'
            return message
        # Verifica se ainda há vagas disponíveis
        if self._event._used_slots < self._event._slots:
            self._event._used_slots += 1
        else:
            message = 'The event is full!'
            return message
        return message