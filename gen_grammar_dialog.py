from dialog_generator import DialogGenerator
from conf import *

conf = getGrammarConfig()
dg = DialogGenerator(conf)

case = 500
for k in range(case):
    print("Test %d:" % k)
    dg.genNew()
    for s in dg.getActsStr():
        print(s)
    print()
