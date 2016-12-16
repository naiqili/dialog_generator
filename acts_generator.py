from utils import *
from conf import *

class ActsGenerator(object):
    def __init__(self, conf):
        self.__dict__.update(conf)
        self.end_of_seq = False
        self.dialog_started = False
        
    def processUserState(self):
        res = []
        nxt = random_select([("restart",self.user_restart_prob),
                             ("report", self.user_report_prob),
                             ("inform", self.user_inform_prob),
                             ("finish", self.user_finish_prob)])
        if nxt == "restart":
            res.append(set(("user_restart", )))
            res.append(set(("sys_ack", )))
            conf = getDefaultConfig()
            self.state = conf["state"]
            return res
        elif nxt == "report":
            res.append(set(("user_report", )))
            res.append(set(("sys_report", )))
            return res
        elif nxt == "finish":
            res.append(set(("user_finish", )))
            self.state["role"] = "sys"
            return res
        else: # nxt == "inform"
            user_acts = set()
            for ont in self.ontology:
                if self.state[ont][0] == "null":
                    tmp = random_select([("skip", self.user_inform_skip_prob),
                                         ("toweak", self.user_inform_new_weak_prob),
                                         ("toknow", self.user_inform_new_know_prob)])
                    if tmp == "skip":
                        pass
                    elif tmp == "toweak":
                        value = self.initValue(ont)
                        user_acts.add(("user_inform", ont, value))
                        self.state[ont] = ("weak", value)
                    elif tmp == "toknow":
                        value = self.initValue(ont)
                        user_acts.add(("user_inform", ont, value))
                        self.state[ont] = ("know", value)
                else: # the slot is already filled
                    tmp = random_select([(True, self.user_inform_change_prob),
                                         (False, 1-self.user_inform_change_prob)])
                    if tmp: # Change it
                        value = self.changeValue(ont, self.state[ont][1])
                        user_acts.add(("user_inform", ont, value))
                        self.state[ont] = ("weak", value)
                    else: # Not chane
                        pass
            if len(user_acts) > 0:
                self.state["role"] = "sys"
                res.append(user_acts)
            return res    
            
    def processSysState(self):
        res = []
        if any([self.state[ont][0]=="weak" for ont in self.ontology]): # Still has weak slots
            sys_acts = set()
            for ont in self.ontology:
                if self.state[ont][0] == "weak":
                    sys_acts.add(("sys_makesure", ont))
            res.append(sys_acts)
            ack_prob = self.user_ack_makesure_prob
            ack_res = random_select([(True, ack_prob), \
                                     (False, 1 - ack_prob)])
            if ack_res: # User ack that all are correct
                 for ont in self.ontology:
                    if self.state[ont][0] == "weak":
                        self.state[ont] = ("know", self.state[ont][1])
                 res.append(set(("user_ack", )))
            else: # User randomly re-informs some weak slots
                  # Slots not mentioned will be set to know
                weak_slots = [ont for ont in self.ontology \
                               if self.state[ont][0] == "weak"]
                # Candidate is a non-empty subset of weak_slots
                cands = subsets_of(weak_slots)
                cands.remove([])
                # Randomly sample one from candidate
                # r_cand is a list of weak slots
                r_cand = random_select([(k, 1) for k in cands])
                user_acts = set()
                for ont in r_cand:
                    new_value = self.changeValue(ont, self.state[ont][1])
                    user_acts.add(("user_inform", ont, new_value))
                    self.state[ont] = ("weak", new_value)
                    # Set unmentioned slots to known
                    for ont in self.ontology:
                        if (ont not in r_cand) and self.state[ont] == "weak":
                            self.state[ont] = ("know", self.state[ont][1])
                res.append(user_acts) 
            return res # The role is still sys
        elif all([self.state[ont][0]=="know" for ont in self.ontology]): # All slots are known
            # Sys ask 'do you want to hear a report?'
            res.append(set(("sys_report_request", )))
            report_prob = self.user_ack_report_request_prob
            report_ack = random_select([(True, report_prob), \
                                        (False, 1-report_prob)])
            if report_ack: # User wants report
                res.append(set(("user_ack", )))
                res.append(set(("sys_report", )))
                report_correct = random_select([(True, self.report_correct_prob), 
                                                (False, 1 - self.report_correct_prob)])
                if report_correct:
                    res.append(set(("user_ack", )))
                    res.append(set(("sys_finish", )))
                    self.end_of_seq = True
                else:
                    self.state["role"] = "user" # Change role to user
            else: # User does not want report
                res.append(set(("user_reject", )))
                res.append(set(("sys_finish", )))
                self.end_of_seq = True
            return res
        else: # No weak slots, but some NULL
              # sys ask for the NULL slots
              # and change role to user
            sys_acts = set()
            for ont in self.ontology:
                if self.state[ont][0] == "null":
                    sys_acts.add(("sys_request", ont))
            res.append(sys_acts)
            self.state["role"] = "user"
            return res
                    
    def getNextActs(self): # Returns a list of action sets
        res = []
        if self.end_of_seq:
            return None
        # If not yet start, user may chose to say 'hello'
        # Or skips the step, and gives order directly
        if not self.dialog_started:
            start_prob = self.user_start_prob
            start_ack = random_select([(True, start_prob),
                                       (False, 1-start_prob)])

            if start_ack:
                res.append(set(("user_start", )))
                res.append(set(("sys_ack", )))
            self.dialog_started = True
            return self.getNextActs()

        if self.state["role"] == "user":
            res = self.processUserState()
        else: # self.state["role"] == "sys"
            res = self.processSysState()

        if res == []:
            return self.getNextActs()
        else:
            return res

    def getActsSeq(self):
        res = []
        while True:
            tmp = self.getNextActs()
            if tmp == None:
                return res
            res = res + tmp
          
    def initValue(self, ont):
        return ont + "_value"

    def changeValue(self, ont, prev_v):
        return ont + "_change"

if __name__=="__main__":
    conf = getDefaultConfig()
    ag = ActsGenerator(conf)

    for a in ag.getActsSeq():
        print a
