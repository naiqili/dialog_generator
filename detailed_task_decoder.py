class DetailedTaskDecoder(object):
    def __init__(self):
        pass

    def decode(self, acts_list, states_list):
        already_inform = False
        s = ""
        for k in range(len(acts_list)):
            acts = acts_list[k]
            if acts == set(("user_start", )):
                s = s + "user: Start with a hello message.\n"
            elif acts == set(("sys_ack", )):
                s = s + "sys: Acknoledge the user's previous command.\n"
            elif acts == set(("user_restart", )):
                s = s + "user: Ask the system to restart.\n"
            elif acts == set(("sys_report_request", )):
                s = s + "sys: Ask the user whether want a detail of the current system state.\n"
            elif acts == set(("sys_report", )):
                s = s + "sys: report all the information you obtain so far.\n"
            elif acts == set(("user_dont_want_report", )):
                s = s + "user: Tell the system that you don't need a report.\n"
            elif acts == set(("user_ack", )):
                s = s + "user: Say yes to the system's previous request.\n"
            elif acts == set(("sys_finish", )):
                s = s + "sys: Tell the user that a reminder has been successfully set.\n"
            elif acts == set(("user_finish", )):
                s = s + "user: Tell the system that you have finished.\n"
            elif list(acts)[0][0] == "sys_request":
                s = s + "sys: Ask the user about "
                for act in acts:
                    if act[1] == "what":
                        s = s + "the name of the event, "
                    elif act[1] == "when_start":
                        s = s + "when it starts, "
                    elif act[1] == "duration":
                        s = s + "how long it lasts, "
                    elif act[1] == "who":
                        s = s + "who will go with you, "
                    elif act[1] == "where":
                        s = s + "where does it take place, "
                    elif act[1] == "day":
                        s = s + "what's the day of the event, "
                s = s[:-2] + ".\n"
            elif list(acts)[0][0] == "sys_makesure":
                s = s + "sys: make sure that "
                state = states_list[k-1]
                for act in acts:
                    if act[1] == "what":
                        s = s + "the user want to %s, " % self.parseEventName(state["what"][1])
                    elif act[1] == "when_start":
                        s = s + "it starts at %d:%d, " % eval(state["when_start"][1])
                    elif act[1] == "duration":
                        s = s + "it lasts %d hours %d minutes, " % eval(state["duration"][1])
                    elif act[1] == "who":
                        peo_list = eval(state["who"][1])
                        s = s + "you are going with %s" % peo_list[0]
                        for peo in peo_list[1:]:
                            s = s + ", %s" % peo
                        s = s + ", "
                    elif act[1] == "where":
                        s = s + "it take place at %s, " % state["where"][1]
                    elif act[1] == "day":
                        s = s + "the day is %s, " % state["day"][1]
                s = s[:-2] + ".\n"
            elif list(acts)[0][0] == "user_inform":
                e_name, st_h, st_m, dur_h, dur_m, peo_list, loc, day = \
                    "", "",   "",   "",    "",    "",       "",  ""
                for act in acts:
                    if act[1] == "what":
                        e_name = self.parseEventName(act[2])
                    elif act[1] == "when_start":
                        (st_h, st_m) = eval(act[2])
                    elif act[1] == "duration":
                        (dur_h, dur_m) = eval(act[2])
                    elif act[1] == "who":
                        peo_list = eval(act[2])
                    elif act[1] == "where":
                        loc = act[2]
                    elif act[1] == "day":
                        day = act[2]
                if not already_inform:
                    #already_inform = True
                    s = s + "user: Tell the system that "
                    if e_name != "" and day != "":
                        s = s + "you want to %s %s, " % (e_name, day)
                    elif e_name != "":
                        s = s + "you want to %s, " % e_name
                    elif day != "":
                        s = s + "the day is %s, " % day
                    if loc != "":
                        s = s + "the location is %s, " % loc
                    if st_h != "" and dur_h != "":
                        s = s + "it starts at %d:%d and lasts for %d hours %d minutes, " % (st_h, st_m, dur_h, dur_m)
                    elif st_h != "":
                        s = s + "it starts at %d:%d, " % (st_h, st_m)
                    elif dur_h != "":
                        s = s + "it takes %d hours %d minutes, " % (dur_h, dur_m)
                    if peo_list != "":
                        s = s + "you are going with %s" % peo_list[0]
                        for peo in peo_list[1:]:
                            s = s + ", %s" % peo
                        s = s + "."
                    s = s + "\n"
                else:
                    s = s + "user: Tell the system that you change "
                    if e_name != "":
                        s = s + "the event name to %s, " % e_name
                    if loc != "":
                        s = s + "the location to %s, " % loc
                    if day != "":
                        s = s + "the day to %s, " % day
                    if st_h != "":
                        s = s + "the start time to %d:%d, " % (st_h, st_m)
                    if dur_h != "":
                        s = s + "that it take %d hours %d minutes, " % (dur_h, dur_m)
                    if peo_list != "":
                        s = s + "you are going with " + peo_list[0]
                        for peo in peo_list[1:]:
                            s = s + ", %s" % peo
                    s = s[:-2] + ".\n"
            else:
                pass
        return s

    def parseEventName(self, s):
        d = {}
        d['take_bus'] = 'take a bus'
        d['take_plane'] = 'take a plane'
        d['meeting'] = 'have a meeting'
        d['movie'] = 'watch a movie'
        d['sport'] = 'do some sports'
        d['lunch'] = 'have lunch'
        d['supper'] = 'have supper'
        d['game'] = 'play computer game'
        if d[s]:
            return d[s]
        return s
