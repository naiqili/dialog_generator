import random

def random_select(lst):
    s = sum(v for (k, v) in lst)
    uniform_lst = [(k, 1.0*v/s) for (k, v) in lst]
    p = 0
    rnd = random.random()
    for (k, v) in uniform_lst:
        p = p + v
        if p >= rnd:
            return k
    return uniform_lst[-1][0]

def subsets_of(lst):
    if lst == []:
        return [[]]
    rec = subsets_of(lst[1:])
    return rec + [[lst[0]] + l for l in rec]

def lst_to_str(lst):
    if len(lst) == 0:
        return ""
    res = str(lst[0])
    for s in lst[1:-1]:
        res = res + ', ' + s
    if len(lst) > 1:
        res = res + ' and ' + lst[-1]
    return res

if __name__=='__main__':
#    for k in range(20):
#        print random_select([("high", 0.6), ("median", 0.3), ("low", 0.1)])

    tmp = subsets_of([1, 2, 3])
    tmp.remove([])
    print(tmp)
