from utils import *
import random
import json
import itertools

class EventGenerator(object):
    def __init__(self, dataroot='./data/'):
        ontology = json.load(open('./ontology_itime3.json'))
        self.names = ontology['invitee']
        self.names.remove('Dontcare')
        self.locations = list(itertools.chain.from_iterable([loc['short_name'] for loc in ontology['location']]))
        self.locations.remove('Dontcare')
        self.titles = ontology['title']

    def randomEventName(self):
        res = random.choice(self.titles)
        return res

    def randomLoc(self, event_name):
        res = random.choice(self.locations)
        return res

    def randomStartTime(self, event_name):
        res_h = random.choice(list(range(0, 24)))
        res_m = random.choice([0, 30])
        return (res_h, res_m)

    def randomDay(self):
        flag = random_select([(True, 0.5), (False, 0.5)])
        if flag:
            lst1 = ["this", "next"]
            lst2 = ["Monday", "Tuesday", "Wednesday", "Thursday", \
                "Friday", "Saturday", "Sunday"]
        else:
            lst1 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', \
                       'agaust', 'september', 'october', 'november', 'december']
            lst2 = list(map(str, range(1, 30)))
        res = ' '.join(random.choice(l) for l in [lst1, lst2])
        return res

    def randomDur(self, event_name):
        res_h = random.choice(list(range(0, 5)))
        res_m = random.choice([0, 30])
        if res_h == 0 and res_m == 0:
            res_m = 30
        return (res_h, res_m)

    def randomNames(self):
        lst = []
        for k in range(4):
            if len(lst) > 0 and random.random() > 0.8:
                break
            lst.append(random.choice(self.names))
        return lst

if __name__=='__main__':
    eg = EventGenerator()
    print(eg.titles)
    print(eg.names)
    print()
    for k in range(5):
        name = eg.randomEventName()
        loc = eg.randomLoc(name)
        st_day = eg.randomDay()
        st_time = eg.randomStartTime(name)
        dur = eg.randomDur(name)
        names = eg.randomNames()
        print(name, loc, st_day, st_time, dur, names)
