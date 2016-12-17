class BasicDecoder(object):
    def __init__(self):
        pass

    # Each acts is a set of actions
    def decode(self, acts_list, states_list):
        res = []
        for k in range(len(acts_list)):
            already_inform = False
            s = ""
            act = acts_list[k]
            if act == set(("user_start", )):
                s = "user: hi, i want to set a reminder"
            elif act == set(("sys_ack", )):
                s = "sys: ok, i am listening"
            elif act == set(("user_ack", )):
                s = "user: ok "
            elif act == set(("user_finish", )):
                s = "user: that's all for now"
            elif act == set(("user_restart", )):
                s = "user: let's start over again"
            elif act == set(("user_report", )):
                s = "user: tell me everything you recorded so far"
            elif act == set(("sys_report", )):
                s = "sys: you said "
                flag = False
                state = states_list[k]
                e_name = state["what"][1]
                if e_name != "null":
                    flag = True
                    s = s + "you want to " + \
                        self.parseEventName(e_name) + ". "
                s = s + "the event "
                if state["when_start"][1] != "null":
                    flag = True
                    s = s + "starts at %d : %d " % \
                        eval(state["when_start"][1])
                    if state["day"][1] != "null":
                        s = s + state["day"][1]
                    s = s + " "
                    if state["duration"][1] != "null":
                        s = s + "and last for %d hours %d minutes. " \
                            % eval(state["duration"][1])
                if state["who"][1] != "null":
                    flag = True
                    s = s + "you are also inviting "
                    for peo in eval(state["who"][1]):
                        s = s + peo + " "
                    s = s + "to go with you "
                if flag == False:
                    s = "sys: you said nothing"
            elif act == set(("sys_report_request", )):
                s = "sys: do you want me to report the details?"
            elif act == set(("sys_finish", )):
                s = "sys: ok, the reminder is successfully set"
            elif act == set(("user_dont_want_report", )):
                s = "user: no need for the report"
            elif list(act)[0][0] == "user_inform":                
                s = "user: "
                if already_inform:
                    s = s + " i change my mind. "
                already_inform = True
                for a in list(act):
                    if a[1] == "what":
                        s = s + "i want to " + \
                            self.parseEventName(a[2]) + ". "
                    if a[1] == "when_start":
                        s = s + "it starts at %d : %d. " % \
                            eval(a[2])
                    if a[1] == "duration":
                        s = s + "it lasts for %d hours %d minutes. " \
                            % eval(a[2])
                    if a[1] == "who":
                        s = s + "i am going with "
                        for peo in eval(a[2]):
                            s = s + peo + ", "
                    if a[1] == "where":
                        s = s + "the location is " + a[2] + ", "
                    if a[1] == "day":
                        s = s + "the day is " + a[2] + ", "
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
            elif list(act)[0][0] == "sys_makesure":
                s = "sys: are you sure that "
                for a in list(act):
                    state = states_list[k]
                    if a[1] == "what":
                        s = s + "the name of the event is %s " % \
                            self.parseEventName(state["what"][1]) + ", "
                    if a[1] == "when_start":
                        s = s + "it starts at %d : %d, " % \
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
            res.append(s)
        return res

    def parseEventName(self, s):
        return s
