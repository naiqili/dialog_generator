from conf import getDefaultConfig
from acts_generator import ActsGenerator
from basic_decoder import BasicDecoder

class DialogGenerator(object):
    def __init__(self, conf):
        self.__dict__.update(conf)
        self.acts_generator = ActsGenerator(conf)
        self.acts_decoder = eval(self.acts_decoder)()
        self.genNew()

    def genNew(self):
        self.acts_seq = self.acts_generator.getActsSeq()
        self.acts_str_list = self.acts_decoder.decode(self.acts_seq)
        return self.acts_seq

    def getActsSeq(self):
        return self.acts_seq

    def getActsStr(self):
        return self.acts_str_list

if __name__=="__main__":
    conf = getDefaultConfig()
    dg = DialogGenerator(conf)

    for k in range(3):
        print "Test Case:", k
        dg.genNew()
        print dg.getActSeq()
        print
        print dg.getActsStr()
        print
        print
