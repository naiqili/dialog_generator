from basic_decoder import *

def getDefaultConfig():
    conf = {}

    # Each slot in state is a pair (level, value),
    # e.g. state(when_start) = (high, 13)
    # All levels and values are initialized to be nulll.
    conf["state"] = {"role": "user", "what": ("null", "null"), "when_start": ("null", "null"), "when_end": ("null", "null"), "who": ("null", "null")}
    conf["ontology"] = {"what", "when_start", "when_end", "who"}

    # Transition probabilities
    conf["user_start_prob"] = 0.3
    conf["user_ack_makesure_prob"] = 0.7
    conf["user_ack_report_request_prob"] = 0.6

    conf["user_restart_prob"] = 0.05
    conf["user_report_prob"] = 0.05
    conf["user_finish_prob"] = 0.05
    conf["user_inform_prob"] = 0.85

    conf["user_inform_skip_prob"] = 0.2
    conf["user_inform_new_weak_prob"] = 0.3
    conf["user_inform_new_know_prob"] = 0.5
    conf["user_inform_change_prob"] = 0.1

    conf["report_correct_prob"] = 0.8

    conf["acts_decoder"] = "BasicDecoder"
    
    return conf