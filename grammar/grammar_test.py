import nltk
from nltk.parse.generate import Nonterminal
from generate import generate
from utils import subsets_of

lst = ['WHAT', 'WHENST', 'WHENED', 'DAY', 'WHO', 'WHERE']

all_lst = subsets_of(lst)
all_lst.remove([])

str_lst = ['USER_INFORM_' + '_'.join(l) for l in all_lst]
print(len(str_lst))
print(str_lst)

grammar = nltk.data.load('file:grammar.cfg')
grammar_list = ['USER_START', 'USER_RESTART', 'USER_REPORT', 'USER_FINISH', 'USER_ACK', 'USER_DONT_WANT_REPORT']
grammar_list = grammar_list + str_lst
k = 30
for grammar_start in grammar_list:
    print(grammar_start)
    for steps in range(k):
        sent = next(generate(grammar, start=Nonterminal(grammar_start),\
                         n=1))
        print(' '.join(sent))
    print()

