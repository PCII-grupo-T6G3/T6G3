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
    att = ['_participant_code', '_event_code']
    # Class header title
    header = 'Registration'
    # field description for use in, for example, in input form
    des = ['Participant code', 'Event Code']

    def __init__(self, participant_code, event_code):
        super().__init__()
        self._participant_code = str(participant_code)
        self._event_code = str(event_code)
        self._ticket = participant_code + event_code
        
        # Add the new object to the Event list
        Registration.obj[self._ticket] = self
        Registration.lst.append(self._ticket)
        
        if self._event_code in Event.obj.keys():
            self._event = Event.obj[self._event_code]
        if self._participant_code in Participant.obj.keys():
            self._participant = Participant.obj[self._participant_code]

    @property
    def event_code(self):
        return self._event_code
    @property
    def event(self):
        return self._event
    @property
    def participant_code(self):
        return self._participant_code
    @property
    def participant(self):
        return self._participant
    @property
    def ticket(self):
        return self._ticket
    
    def chk_validity(self):
        message = 'Approved!'
        # Verifica o evento
        if self._event_code not in Event.obj.keys():
            message = 'Event not found!'
            return message
        # Verifica o participante
        if self._participant_code not in Participant.obj.keys():
            message = 'Participant not found!'
            return message
        # Verifica se participante já está inscrito
        if Registration.lst.count(self._ticket) == 2:
            message = 'Participant already registered in this event!'
            return message
        # Verifica se ainda há vagas disponíveis
        if self._event._used_slots < self._event._slots:
            self._event._used_slots += 1
            Event.update(self._event_code)
        else:
            message = 'The event is full!'
            return message
        return message
    
    def chk_removal(self):
        message = 'Deleted!'
        return message