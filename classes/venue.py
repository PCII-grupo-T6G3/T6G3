#Class Venue
#import the generic class

from classes.gclass import Gclass

class Venue(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1  # = 1 in case of auto number on
    nkey = 1
    # Class attributes, identifier attribute must be the first one on the list
    att = ['_code', '_name', '_location', '_capacity']
    # Class header title
    header = 'Venues'
    # Field description for use in, for example, in input form
    des = ['Code', 'Name', 'Location', 'Capacity']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, location, capacity):
        super().__init__()
        # Uncomment in case of auto number on
        if code == 'None':
            codes = Venue.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int, Venue.getatlist('_code'))) + 1)
        # Object attributes
        self._code = code
        self._name = name
        self._location = location
        self._capacity = int(capacity)
        # Add the new object to the Venue list
        Venue.obj[code] = self
        Venue.lst.append(code)

    # Object properties
    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
