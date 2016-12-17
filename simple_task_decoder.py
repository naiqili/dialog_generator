class SimpleTaskDecoder(object):
    def __init__(self):
        pass

    def decode(self, acts_list, states_list):
        already_inform = False
        s = ""
        for k in range(len(acts_list)):
            acts = acts_list[k]
            if list(acts)[0][0] == "user_inform":
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
                    already_inform = True
                    s = s + "You want to set a reminder that you are going to %s at %s %s.\n" % (e_name, loc, day)
                    s = s + "It starts from %d:%d, and will take %d hours and %d minutes.\n" % (st_h, st_m, dur_h, dur_m)
                    if peo_list != "":
                        s = s + "You are also inviting " + peo_list[0]
                        for peo in peo_list[1:]:
                            s = s + ", " + peo
                        s = s + " to go with you.\n"
                else:
                    s = s + "But suddenly you remember that you have another important thing to do.\n"
                    s = s + "You change "
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
                    s = s + ".\n"
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
