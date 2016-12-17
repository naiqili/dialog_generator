from utils import *
import random

class EventGenerator(object):
    def __init__(self, dataroot='./data/'):
        with open(dataroot + 'events') as f_events, \
             open(dataroot + 'names') as f_names:
            self.events = {}
            for line in f_events:
                if line[0] == '#':
                    continue
                lst = [s.strip() for s in line.split('-')]
                event_name = lst[0]
                event_detail = {}
                event_detail['st_range'] = eval(lst[1])
                event_detail['basic_dur'] = eval(lst[2])
                event_detail['locs'] = eval(lst[3])
                event_detail['invite'] = lst[4]
                self.events[event_name] = event_detail

            self.names = []
            for line in f_names:
                self.names.append(line.strip())

    def randomEventName(self):
        lst = [(k, 1) for k in self.events.keys()]
        res = random_select(lst)
        return res

    def randomLoc(self, event_name):
        locs = self.events[event_name]["locs"]
        lst = [(k, 1) for k in locs]
        res = random_select(lst)
        return res

    def randomStartTime(self, event_name):
        [(h1, m1), (h2, m2)] = self.events[event_name]["st_range"]
        st = h1*60 + m1
        ed = h2*60 + m2
        rnd = random.randint(st, ed)
        res_h = rnd / 60
        res_m = rnd - res_h*60
        return (res_h, res_m)

    def randomDay(self):
        lst1 = ["this", "next"]
        lst2 = ["Monday", "Tuesday", "Wednesday", "Thursday", \
                "Friday", "Saturday", "Sunday"]
        res = ' '.join(random.choice(l) for l in [lst1, lst2])
        return res

    def randomDur(self, event_name):
        (h, m) = self.events[event_name]["basic_dur"]
        # Randomly +- 1 hour
        tmp = h*60 + m + random.randint(-60, 60)
        if tmp < 15: # an event lasts for at least 15 mins
            tmp = 15
        res_h = tmp / 60
        res_m = tmp - res_h*60
        return (res_h, res_m)

    def randomNames(self):
        lst = subsets_of(self.names)
        lst.remove([])
        return random_select([(k, 1) for k in lst])

if __name__=='__main__':
    eg = EventGenerator()
    print eg.events
    print eg.names
    print
    for k in range(5):
        name = eg.randomEventName()
        loc = eg.randomLoc(name)
        st_day = eg.randomDay()
        st_time = eg.randomStartTime(name)
        dur = eg.randomDur(name)
        names = eg.randomNames()
        print name, loc, st_day, st_time, dur, names
