import nltk
from nltk.parse.generate import Nonterminal
from grammar.generate import generate
from utils import *

class GrammarDecoder(object):
    def __init__(self):
        self.grammar = nltk.data.load('file:./grammar/grammar.cfg')

    def decode_from_grammar(self, head):
        sent = ' '.join(next(generate(self.grammar, start=Nonterminal(head), n=1)))
        return sent

    def subsitute_txt(self, state, txt):
        res = txt
        res = res.replace('<what>', state['what'][1].lower())
        if state['who'][0] != 'null':
            res = res.replace('<who>', lst_to_str(eval(state['who'][1])))
        if state['when_start'][0] != 'null':
            res = res.replace('<st_hour>', '%02d' % eval(state['when_start'][1])[0])
            res = res.replace('<st_min>', '%02d' % eval(state['when_start'][1])[1])
        if state['duration'][0] != 'null':
            res = res.replace('<dur>', '%d hours and %d minutes' % (eval(state['duration'][1])[0], eval(state['duration'][1])[1]))
        if state['when_start'][0] != 'null' and state['duration'][0] != 'null':
            (st_hour, st_min) = eval(state['when_start'][1])
            (dur_hour, dur_min) = eval(state['duration'][1])
            tmp = 60*(st_hour+dur_hour) + (st_min+dur_min)
            ed_hour = tmp // 60
            ed_min = tmp - 60*ed_hour
            res = res.replace('<ed_hour>', '%02d' % ed_hour)
            res = res.replace('<ed_min>', '%02d' % ed_min)
        res = res.replace('<day>', str(state['day'][1]))
        res = res.replace('<where>', str(state['where'][1]))
        return res
        
    # Each acts is a set of actions
    def decode(self, acts_list, states_list):
        res = []
        for k in range(len(acts_list)):
            already_inform = False
            s = ""
            act = acts_list[k]
            if act == set(("user_start", )):
                s = "user: %s" % (self.decode_from_grammar('USER_START'))
            if act == set(("user_yes", )):
                s = "user: %s" % (self.decode_from_grammar('USER_YES'))
            elif act == set(("sys_ack", )):
                s = "sys: ok, i am listening"
            elif act == set(("user_ack", )):
                s = "user: %s" % (self.decode_from_grammar('USER_ACK'))
            elif act == set(("user_finish", )):
                s = "user: that's all for now"
            elif act == set(("user_restart", )):
                s = "user: %s" % (self.decode_from_grammar('USER_RESTART'))
            elif act == set(("user_report", )):
                s = "user: %s" % (self.decode_from_grammar('USER_REPORT'))
            elif act == set(("sys_report", )):
                s = "sys: you said "
                flag = False
                state = states_list[k]
                e_name = state["what"][1]
                if e_name != "null":
                    flag = True
                    s = s + "you want to " + \
                        self.parseEventName(e_name).lower() + ". "
                s = s + "the event "
                if state["when_start"][1] != "null":
                    flag = True
                    s = s + "starts at %02d : %02d " % \
                        eval(state["when_start"][1])
                    if state["day"][1] != "null":
                        s = s + 'on ' + state["day"][1]
                    s = s + " "
                    if state["duration"][1] != "null":
                        s = s + "and last for %d hours %d minutes. " \
                            % eval(state["duration"][1])
                if state["who"][1] != "null":
                    flag = True
                    s = s + "you are also inviting "
                    for peo in eval(state["who"][1]):
                        s = s + peo + ", "
                    s = s + "to go with you "
                if flag == False:
                    s = "sys: you said nothing"
            elif act == set(("sys_report_request", )):
                s = "sys: do you want me to report the details ?"
            elif act == set(("sys_finish", )):
                s = "sys: ok, the reminder is successfully set."
            elif act == set(("user_dont_want_report", )):
                s = "user: %s" % (self.decode_from_grammar('USER_DONT_WANT_REPORT'))
            elif list(act)[0][0] == "user_inform":                
                s = "user: "
                ontology_ord = ['what', 'when_start', 'duration', 'day', 'who', 'where']
                ontology_flag = {}
                ontology_trans = {'what': '_WHAT', 'when_start': '_WHENST', 'duration': '_WHENED', \
                                  'day': '_DAY', 'who': '_WHO', 'where': '_WHERE'}
                tmp_s = 'USER_INFORM'
                already_inform = False
                for a in list(act):
                    ontology_flag[a[1]] = True                    
                    if k > 0 and states_list[k-1][ a[1] ][0] != 'null':
                        already_inform = True
                if already_inform:
                    s = s + self.decode_from_grammar('USER_EXPLAIN_WRONG') + '. '
                for ont in ontology_ord:
                    if ont in ontology_flag:
                        tmp_s = tmp_s + ontology_trans[ont]
                plain_grammar_txt = self.decode_from_grammar(tmp_s)
                state = states_list[k]
                while plain_grammar_txt.find('<ed_hour>') > -1 and (state['when_start'][0] == 'null' or \
                                                               state['duration'][0] == 'null') :
                    plain_grammar_txt = self.decode_from_grammar(tmp_s)
                subs_grammar_txt = self.subsitute_txt(states_list[k], plain_grammar_txt)
                s = s + subs_grammar_txt
                    
            elif list(act)[0][0] == "sys_request":
                s = "sys: what about "
                for a in list(act):
                    if a[1] == "what":
                        s = s + "the name of the event, "
                    if a[1] == "when_start":
                        s = s + "when it starts, "
                    if a[1] == "duration":
                        s = s + "how long it takes, "
                    if a[1] == "who":
                        s = s + "whom you are going with, "
                    if a[1] == "where":
                        s = s + "the location, "
                    if a[1] == "day":
                        s = s + "the day, "
                s = s[:-2] + ' ?'
            elif list(act)[0][0] == "sys_makesure":
                s = "sys: are you sure that "
                for a in list(act):
                    state = states_list[k]
                    if a[1] == "what":
                        s = s + "the name of the event is %s " % \
                            self.parseEventName(state["what"][1]).lower() + ", "
                    if a[1] == "when_start":
                        s = s + "it starts at %02d : %02d, " % \
                            eval(state["when_start"][1])
                    if a[1] == "duration":
                        s = s + "it takes %d hours and %d minutes, " % eval(state["duration"][1])
                    if a[1] == "who":
                        s = s + "you are going with "
                        for peo in eval(state["who"][1]):
                            s = s + peo + ", "
                    if a[1] == "where":
                        s = s + "the location is " + state["where"][1] + ", "
                    if a[1] == "day":
                        s = s + "the day is " + state["day"][1] + ", "
                s = s[:-2] + ' ?'
            res.append(s)
        return res

    def parseEventName(self, s):
        return s
