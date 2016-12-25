from conf import *
from acts_generator import ActsGenerator
from basic_decoder import BasicDecoder
from grammar_decoder import GrammarDecoder
from simple_task_decoder import SimpleTaskDecoder
from detailed_task_decoder import DetailedTaskDecoder
import copy

class DialogGenerator(object):
    def __init__(self, conf):
        self.conf = conf
        self.__dict__.update(conf)
        self.acts_decoder = eval(self.acts_decoder)()
        
    def genNew(self):
        self.acts_generator = ActsGenerator(copy.deepcopy(self.conf))        
        self.acts_seq = self.acts_generator.getActsSeq()
        self.states_seq = self.acts_generator.state_list
        self.acts_str_list = self.acts_decoder.decode(self.acts_seq, self.states_seq)
        return self.acts_seq

    def getActsSeq(self):
        return self.acts_seq

    def getActsStr(self):
        return self.acts_str_list

    def getStateSeq(self):
        return self.states_seq

    

if __name__=="__main__":
    conf = getDefaultConfig()
    #conf = getTaskConfig()
    dg = DialogGenerator(conf)

    for k in range(3):
        print("Test Case:", k)
        dg.genNew()
        print(dg.getActsSeq())
        print()
        print(dg.getStateSeq())
        print()
        for s in dg.getActsStr():
            print(s)
        print()
        print(len(dg.getActsSeq()), len(dg.getStateSeq()))
