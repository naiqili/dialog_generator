from dialog_generator import DialogGenerator
from conf import *

conf = getDetailedTaskConfig()
dg = DialogGenerator(conf)

dg.genNew()
print dg.getActsSeq()
print
print dg.getActsStr()
