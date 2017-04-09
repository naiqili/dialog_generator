from dialog_generator import DialogGenerator
from conf import *

conf = getGrammarConfig()
dg = DialogGenerator(conf)

case = 10
for k in range(case):
    print("Test %d:" % k)
    dg.genNew()
    for s in dg.getActsStr():
        print(s)
    for s in dg.getActsSeq():
        print(s)
    print()
