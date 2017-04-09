from dialog_generator import DialogGenerator
from conf import *
import cPickle
import random
import pprint

conf = getGrammarConfig()
dg = DialogGenerator(conf)

case = 8000

def dur2str(h, m):
    res = ''
    trans = ['twelve','one','two','three','four','five','six','seven','eight','nine', \
             'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen', \
             'eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four']
    trans_m = {0:['WRONG'], 15:['fifteen minutes', 'a quarter', 'one quarter'], 30:['thirty minutes', 'half an hour'], 45:['forty five minutes', 'three quarters']}
    if h == 0 and m != 0:
        res = random.choice(trans_m[m])
    elif h != 0 and m == 0:
        res = "%s hours" % trans[h]
    elif h != 0 and m != 0:
        s = random.choice(trans_m[m])
        res = "%s hours and %s" % (trans[h], s)
    return res

def time2str(h, m):
    res = []
    trans = ['twelve','one','two','three','four','five','six','seven','eight','nine', \
             'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen', \
             'eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four']
    trans_m = {0:'WRONG', 15:'fifteen', 30:'thirty', 45:'forty five'}
    if m == 0:
        s = trans[h] + ' oclock'
        res.append(s)
        if h <= 12:
            s = trans[h] + ' am'
            res.append(s)
            s = trans[h] + ' oclock in the morning'
            res.append(s)
        if h in [12, 13, 14]:
            s = trans[h] + ' oclock at noon'
            res.append(s)
        if h > 12 and h <= 18:
            s = trans[h%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' oclock in the afternoon'
            res.append(s)
        if h > 18:
            s = trans[h%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' oclock in the evening'
            res.append(s)
            s = trans[h%12] + ' oclock at night'
            res.append(s)
    elif m == 15:
        s = trans[h] + ' ' + trans_m[m]
        res.append(s)
        if h <= 12:
            s = trans[h] + ' ' + trans_m[m] + ' am'
            res.append(s)
            s = 'a quarter past ' + trans[h] + ' am'
            res.append(s)
            s = trans[h] + ' ' + trans_m[m] + ' in the morning'
            res.append(s)
            s = 'a quarter past ' + trans[h] + ' in the morning'
            res.append(s)
        if h in [12, 13, 14]:
            s = trans[h] + ' ' + trans_m[m] + ' at noon'
            res.append(s)
            s = 'a quarter past ' + trans[h] +  ' at noon'
            res.append(s)
        if h > 12 and h <= 18:
            s = trans[h%12] + ' ' + trans_m[m] + ' pm'
            res.append(s)
            s = 'a quarter past ' + trans[h%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' in the afternoon'
            res.append(s)
            s = 'a quarter past ' + trans[h%12] + ' in the afternoon'
            res.append(s)
        if h > 18:
            s = trans[h%12] + ' ' + trans_m[m] + ' pm'
            res.append(s)
            s = 'a quarter past ' + trans[h%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' in the evening'
            res.append(s)
            s = 'a quarter past ' + trans[h%12] + ' in the evening'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' at night'
            res.append(s)
            s = 'a quarter past ' + trans[h%12] + ' at night'
            res.append(s)
    elif m == 30:
        s = trans[h] + ' ' + trans_m[m]
        res.append(s)
        if h <= 12:
            s = trans[h] + ' ' + trans_m[m] + ' am'
            res.append(s)
            s = 'half past ' + trans[h] + ' am'
            res.append(s)
            s = trans[h] + ' ' + trans_m[m] + ' in the morning'
            res.append(s)
            s = 'half past ' + trans[h] + ' in the morning'
            res.append(s)
        if h in [12, 13, 14]:
            s = trans[h] + ' ' + trans_m[m] + ' at noon'
            res.append(s)
            s = 'half past ' + trans[h] +  ' at noon'
            res.append(s)
        if h > 12 and h <= 18:
            s = trans[h%12] + ' ' + trans_m[m] + ' pm'
            res.append(s)
            s = 'half past ' + trans[h%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' in the afternoon'
            res.append(s)
            s = 'half past ' + trans[h%12] + ' in the afternoon'
            res.append(s)
        if h > 18:
            s = trans[h%12] + ' ' + trans_m[m] + ' pm'
            res.append(s)
            s = 'half past ' + trans[h%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' in the evening'
            res.append(s)
            s = 'half past ' + trans[h%12] + ' in the evening'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' at night'
            res.append(s)
            s = 'half past ' + trans[h%12] + ' at night'
            res.append(s)
    elif m == 45:
        s = trans[h] + ' ' + trans_m[m]
        res.append(s)
        if h <= 12:
            s = trans[h] + ' ' + trans_m[m] + ' am'
            res.append(s)
            s = 'a quarter to ' + trans[h+1] + ' am'
            res.append(s)
            s = trans[h] + ' ' + trans_m[m] + ' in the morning'
            res.append(s)
            s = 'a quarter to ' + trans[h+1] + ' in the morning'
            res.append(s)
        if h in [12, 13, 14]:
            s = trans[h] + ' ' + trans_m[m] + ' at noon'
            res.append(s)
            s = 'a quarter to ' + trans[h+1] +  ' at noon'
            res.append(s)
        if h > 12 and h <= 18:
            s = trans[h%12] + ' ' + trans_m[m] + ' pm'
            res.append(s)
            s = 'a quarter to ' + trans[(h+1)%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' in the afternoon'
            res.append(s)
            s = 'a quarter to ' + trans[(h+1)%12] + ' in the afternoon'
            res.append(s)
        if h > 18:
            s = trans[h%12] + ' ' + trans_m[m] + ' pm'
            res.append(s)
            s = 'a quarter to ' + trans[(h+1)%12] + ' pm'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' in the evening'
            res.append(s)
            s = 'a quarter to ' + trans[(h+1)%12] + ' in the evening'
            res.append(s)
            s = trans[h%12] + ' ' + trans_m[m] + ' at night'
            res.append(s)
            s = 'a quarter to ' + trans[(h+1)%12] + ' at night'
            res.append(s)
    return random.choice(res) 

def process(str_list, act_list, state_list, dg):
    all_res = []
    trans_m = {0:0, 15:1, 30:2, 45:3}
    for k in range(len(act_list)):
        isUser = False
        s = str_list[k]
        a = list(act_list[k])
        state = state_list[k]
        res = {'user_affirm': '<NO>',  'user_ack': '<NO>',  'user_finish': '<NO>',  'user_start': '<NO>',  \
                   'user_finish': '<NO>',  'user_start': '<NO>',  'user_restart': '<NO>',  'user_report': '<NO>',  \
                   'user_dont_want_report': '<NO>',  'user_inform_what': '<NO>',  \
                   'user_inform_whenstart_hour': 24, 'user_inform_whenstart_min': 4,  \
                   'user_inform_whened_hour': 24, 'user_inform_whened_min': 4, \
                   'user_inform_duration_hour': 24, 'user_inform_duration_min': 4,  \
                   'user_inform_who': '<NO>',  'user_inform_where': '<NO>',  \
                   'user_inform_day': '<NO>'}
        while True:
            st_hour = random.randint(1, 23)
            st_min = random.choice([0, 15, 30, 45])
            dur_hour = random.choice([0, 1, 2])
            dur_min = random.choice([0, 15, 30, 45])
            if dur_hour == 0 and dur_min == 0:
                continue
            if (st_hour + dur_hour) * 60 + (st_min + dur_min) > 23 * 60 + 45:
                continue
            ed_hour = ((st_hour + dur_hour) * 60 + (st_min + dur_min)) / 60
            ed_min = (st_hour + dur_hour) * 60 + (st_min + dur_min) - ed_hour * 60
            break
        '''print s
        print 'start:', st_hour, st_min, time2str(st_hour, st_min)
        print 'end:', ed_hour, ed_min
        print 'dur:', dur_hour, dur_min'''
        for act in a:
            if act == 'user_affirm' or act == 'user_ack' or act == 'user_finish' \
               or act == 'user_start' or act == 'user_restart' \
               or act == 'user_report' or act == 'user_dont_want_report':
                res[act] = '<YES>'
                isUser = True
            elif isinstance(act, tuple) and act[0] == 'user_inform':
                if act[1] == 'what':
                    res['user_inform_what'] = act[2].lower()
                if act[1] == 'who':
                    res['user_inform_who'] = [n.lower() for n in eval(act[2])]
                if act[1] == 'where':
                    res['user_inform_where'] = act[2].lower()
                if act[1] == 'day':
                    res['user_inform_day'] = act[2].lower()
                if act[1] == 'when_start':
                    s = s.replace('<st_time>', time2str(st_hour, st_min))
                    res['user_inform_whenstart_hour'] = st_hour
                    res['user_inform_whenstart_min'] = trans_m[st_min]
                if act[1] == 'duration':
                    if s.find('<ed_time>') != -1:
                        s = s.replace('<ed_time>', time2str(ed_hour, ed_min))
                        res['user_inform_whened_hour'] = ed_hour
                        res['user_inform_whened_min'] = trans_m[ed_min]
                    if s.find('<dur_time>') != -1:
                        s = s.replace('<dur_time>', dur2str(dur_hour, dur_min))
                        res['user_inform_duration_hour'] = dur_hour
                        res['user_inform_duration_min'] = trans_m[dur_min]
                isUser = True
        if isUser:
            s = dg.acts_decoder.subsitute_txt(state, s)
            s = s[6:].lower()
            res['text'] = s
            all_res.append(res)
    return all_res

data = []
for k in range(case):
    #print("Test %d:" % k)
    dg.genNew()
    str_list = dg.getActsStr()
    act_list = dg.getActsSeq()
    state_list = dg.getStateSeq()
    assert len(str_list) == len(act_list)
    all_res = process(str_list, act_list, state_list, dg)
    data = data + all_res
print len(data)
pprint.pprint(data[:50])
cPickle.dump(data, open('./tmp/all_data3.pkl', 'w'))
