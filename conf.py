from basic_decoder import *
import random

def getDefaultConfig():
    conf = {}

    # Each slot in state is a pair (level, value),
    # e.g. state(when_start) = (high, 13)
    # All levels and values are initialized to be nulll.
    start_h = random.randint(0, 23)
    start_m = random.choice([0, 30])
    dur_h = random.choice([0, 3])
    dur_m = random.choice([0, 30])
    conf["state"] = {"role": "user", "what": ("null", "null"), "when_start": ("null", (start_h, start_m)), "duration": ("null", (dur_h, dur_m)), "who": ("null", "null"), "where": ("null", "null"), "day": ("null", "null")}
    conf["ontology"] = {"what", "when_start", "duration", "who", "where", "day"}

    # Transition probabilities
    conf["user_start_prob"] = 0.3
    conf["user_ack_expl_confirm_prob"] = 0.7
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

def getGrammarConfig():
    conf = {}

    # Each slot in state is a pair (level, value),
    # e.g. state(when_start) = (high, 13)
    # All levels and values are initialized to be nulll.
    conf["state"] = {"role": "user", "what": ("null", "null"), "when_start": ("null", "null"), "duration": ("null", "null"), "who": ("null", "null"), "where": ("null", "null"), "day": ("null", "null")}
    conf["ontology"] = {"what", "when_start", "duration", "who", "where", "day"}

    # Transition probabilities
    conf["user_start_prob"] = 0.3
    conf["user_ack_expl_confirm_prob"] = 0.9
    conf["user_ack_report_request_prob"] = 0.9

    conf["user_restart_prob"] = 0.05
    conf["user_report_prob"] = 0.05
    conf["user_finish_prob"] = 0.05
    conf["user_inform_prob"] = 0.85

    conf["user_inform_skip_prob"] = 0.4
    conf["user_inform_new_weak_prob"] = 0.1
    conf["user_inform_new_know_prob"] = 0.9
    conf["user_inform_change_prob"] = 0.05

    conf["report_correct_prob"] = 0.9

    conf["acts_decoder"] = "GrammarDecoder"
    
    return conf

def getSimpleTaskConfig():
    conf = {}

    # Each slot in state is a pair (level, value),
    # e.g. state(when_start) = (high, 13)
    # All levels and values are initialized to be nulll.
    conf["state"] = {"role": "user", "what": ("null", "null"), "when_start": ("null", "null"), "duration": ("null", "null"), "who": ("null", "null"), "where": ("null", "null"), "day": ("null", "null")}
    conf["ontology"] = {"what", "when_start", "duration", "who", "where", "day"}

    # Transition probabilities
    conf["user_start_prob"] = 0.0
    conf["user_ack_expl_confirm_prob"] = 1.0
    conf["user_ack_report_request_prob"] = 1.0

    conf["user_restart_prob"] = 0.0
    conf["user_report_prob"] = 0.0
    conf["user_finish_prob"] = 0.0
    conf["user_inform_prob"] = 1.0

    conf["user_inform_skip_prob"] = 0.0
    conf["user_inform_new_weak_prob"] = 0.0
    conf["user_inform_new_know_prob"] = 1.0
    conf["user_inform_change_prob"] = 0.7

    conf["report_correct_prob"] = 0.7

    conf["acts_decoder"] = "SimpleTaskDecoder"
    
    return conf

def getDetailedTaskConfig():
    conf = {}

    # Each slot in state is a pair (level, value),
    # e.g. state(when_start) = (high, 13)
    # All levels and values are initialized to be nulll.
    conf["state"] = {"role": "user", "what": ("null", "null"), "when_start": ("null", "null"), "duration": ("null", "null"), "who": ("null", "null"), "where": ("null", "null"), "day": ("null", "null")}
    conf["ontology"] = {"what", "when_start", "duration", "who", "where", "day"}

    # Transition probabilities
    conf["user_start_prob"] = 0.3
    conf["user_ack_expl_confirm_prob"] = 0.7
    conf["user_ack_report_request_prob"] = 0.6

    conf["user_restart_prob"] = 0.05
    conf["user_report_prob"] = 0.05
    conf["user_finish_prob"] = 0.05
    conf["user_inform_prob"] = 0.85

    conf["user_inform_skip_prob"] = 0.2
    conf["user_inform_new_weak_prob"] = 0.3
    conf["user_inform_new_know_prob"] = 0.5
    conf["user_inform_change_prob"] = 0.07

    conf["report_correct_prob"] = 0.8

    conf["acts_decoder"] = "DetailedTaskDecoder"
    
    return conf
