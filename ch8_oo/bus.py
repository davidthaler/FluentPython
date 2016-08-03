# Example 8-8, 8-12 and 8-15 from FluentPython

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def __repr__(self):
        return repr(self.passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class HauntedBus(Bus):

    def __init__(self, passengers=[]):
        self.passengers = passengers


class TwilightZoneBus(Bus):

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers


