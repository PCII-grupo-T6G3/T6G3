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
    att = ['_event_code', '_participant_code', '_ticket']
    # Class header title
    header = 'Registration'
    # field description for use in, for example, in input form
    des = ['Event code', 'Participant code']

    def __init__(self, event_code, participant_code):
        super().__init__()
        
        # verifica se evento existe
        if event_code in Event.lst:
            self._event_code = event_code
            self._event = Event.obj[event_code]
            # verifica se evento está cheio
            if self._event._used_slots < self._event.slots:
                self._event._used_slots += 1
                # verifica se participante existe
                if participant_code in Participant.lst:
                    self._participant_code = participant_code
                    self._ticket = event_code + participant_code
                    Registration.obj[self._ticket] = self
                    Registration.lst.append(self._ticket)
                elif participant_code not in Participant.lst and event_code in Event.lst:
                    print('Participant ', participant_code, ' not found!')
            else:
                print('Event is full!')
        else:
            print('Event ', event_code, ' not found!')

    @property
    def event_code(self):
        return self._event_code
    @property
    def participant_code(self):
        return self._participant_code
    @property
    def ticket(self):
        return self._ticket
    
# Coisas que mudámos da classe do professor:
# 1. juntámos os códigos das classes evento e participante
# 2. verificámos a integridade para ambos o evento e o participante
# 3. não incluímos um setter para os códigos do evento e do participante
# 4. mudámos o nkey para 2