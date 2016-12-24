from dialog_generator import DialogGenerator
from conf import *

conf = getSimpleTaskConfig()
dg = DialogGenerator(conf)

dg.genNew()
print dg.getActsSeq()
print
print dg.getStateSeq()
print
print dg.getActsStr()
