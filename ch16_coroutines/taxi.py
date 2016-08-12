# Example A-6, used in chapter 16 of Fluent Python

'''
Taxi Simulator
--------------
>>> main(num_taxis=2, seed=10)
Taxi: 0  Event(time=0, process=0, action='leave garage')
Taxi: 0  Event(time=5, process=0, action='pick up')
Taxi: 1    Event(time=5, process=1, action='leave garage')
Taxi: 1    Event(time=10, process=1, action='pick up')
Taxi: 1    Event(time=15, process=1, action='drop off')
Taxi: 0  Event(time=17, process=0, action='drop off')
Taxi: 1    Event(time=24, process=1, action='pick up')
Taxi: 0  Event(time=26, process=0, action='pick up')
Taxi: 0  Event(time=30, process=0, action='drop off')
Taxi: 0  Event(time=34, process=0, action='going home')
Taxi: 1    Event(time=46, process=1, action='drop off')
Taxi: 1    Event(time=48, process=1, action='pick up')
Taxi: 1    Event(time=110, process=1, action='drop off')
Taxi: 1    Event(time=139, process=1, action='pick up')
Taxi: 1    Event(time=140, process=1, action='drop off')
Taxi: 1    Event(time=150, process=1, action='going home')
***End of Events***
'''

import random
import collections
import queue
import argparse
import time

NUM_TAXIS = 3
END_TIME = 180
SEARCH_TIME = 5
TRIP_TIME = 20
DEPARTURE_INT = 5

Event = collections.namedtuple('Event', 'time process action')

def taxi_process(id, trips, start_time=0):
    '''Yield to simulator, issuing event each time'''
    time = yield Event(start_time, id, 'leave garage')
    for i in range(trips):
        time = yield Event(time, id, 'pick up')
        time = yield Event(time, id, 'drop off')
    yield Event(time, id, 'going home')

class Simulator:

    def __init__(self, process_map):
        self.events = queue.PriorityQueue()
        self.processes = dict(process_map)

    def run(self, end_time):
        '''Schedule and display events until time is up.'''
        for _, process in sorted(self.processes.items()):
            first_event = next(process)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('***End of Events***')
                break

            current_event = self.events.get()
            sim_time, id, previous_action = current_event
            print('Taxi:', id, '  ' * id, current_event)
            active_process = self.processes[id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_process.send(next_time)
            except StopIteration:
                del self.processes[id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time. {} events pending ***'
            print(msg.format(self.events.qsize()))


def compute_duration(previous_action):
    '''Compute duration using exponential distribution.'''
    if previous_action in ['leave garage', 'drop off']:
        # prowling
        interval = SEARCH_TIME
    elif previous_action == 'pick up':
        interval = TRIP_TIME
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1

def main(end_time=END_TIME, num_taxis=NUM_TAXIS, seed=None):
    '''
    Initialize random number generator, build processes and run simulation.
    '''
    if seed is not None:
        random.seed(seed)
    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INT) 
                for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Taxi fleet simulator')
    parser.add_argument('-e', '--end_time', type=int, default=END_TIME, 
                        help='simulation end time; default=%s' % END_TIME)
    parser.add_argument('-t', '--taxis', type=int, default=NUM_TAXIS, 
                        help='number of taxis running; default=%s' % NUM_TAXIS)
    parser.add_argument('-s', '--seed', type=int, default=None, 
                        help='random number generator seed (for testing).')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)