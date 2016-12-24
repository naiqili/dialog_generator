from __future__ import print_function

import itertools
import sys
import random
from nltk.grammar import Nonterminal

def generate(grammar, start=None, depth=None, n=None):
    """
    Generates an iterator of all sentences from a CFG.

    :param grammar: The Grammar used to generate sentences.
    :param start: The Nonterminal from which to start generate sentences.
    :param depth: The maximal depth of the generated tree.
    :param n: The maximum number of sentences to return.
    :return: An iterator of lists of terminal tokens.
    """
    if not start:
        start = grammar.start()
    if depth is None:
        depth = sys.maxsize

    iter = _generate_all(grammar, [start], depth)

    if n:
        iter = itertools.islice(iter, n)

    return iter

def _generate_all(grammar, items, depth):
    if items:
        for frag1 in _generate_one(grammar, items[0], depth):
            for frag2 in _generate_all(grammar, items[1:], depth):
                yield frag1 + frag2
    else:
        yield []

def _generate_one(grammar, item, depth):
    if depth > 0:
        if isinstance(item, Nonterminal):
            lst = grammar.productions(lhs=item)
            random.shuffle(lst)
            for prod in lst:
                for frag in _generate_all(grammar, prod.rhs(), depth-1):
                    yield frag
        else:
            yield [item]
