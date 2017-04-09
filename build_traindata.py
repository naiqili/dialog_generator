import cPickle
import random
import pprint

# train data is from all_data 2
# dev data is from all_data 3

#data1 = cPickle.load(open('tmp/all_data1.pkl'))
data2 = cPickle.load(open('tmp/all_data2.pkl'))
data3 = cPickle.load(open('tmp/all_data3.pkl'))

(ind2word, word2ind, ontology_bool, ontology_time, ontology_str) = cPickle.load(open('tmp/dict.pkl'))

all_data = []
train_data = []
dev_data = []

all_data = data2

def add_noise(data, noise_rate=0.01):
    s = data['text']
    lst = s.split()
    r_lst = []
    for w in lst:
        if random.random() < noise_rate:
            new_ind = random.randint(2, len(ind2word)-1)
            r_lst.append(ind2word[new_ind])
        else:
            r_lst.append(w)
    r_s = ' '.join(r_lst)
    data['text'] = r_s
    return data

def process_data(data):
    global ind2word, word2ind, ontology_bool, ontology_time, ontology_str
    tmp_map = {}
    ind_lst = range(10)
    tok_ind = 0
    for ont in ontology_str:
        s = data[ont]
        s = s.split()
        rs = []
        for w in s:
            if w in word2ind:
                rs.append(w)
            elif w in tmp_map:
                rs.append(tmp_map[w])
            else:
                tok_ind = random.choice(ind_lst)
                ind_lst.remove(tok_ind)
                tmp_map[w] = "<TOK%d>" % tok_ind                
                rs.append(tmp_map[w])
        s_res = ' '.join(rs)
        data[ont] = s_res
    s = data['user_inform_who']
    if s == "<NO>":
        data['user_inform_who'] = "<NO>"
    else:
        rs = []
        for w in s:
            w = w.lower()
            if w in word2ind:
                rs.append(w)
            elif w in tmp_map:
                rs.append(tmp_map[w])
            else:
                tok_ind = random.choice(ind_lst)
                ind_lst.remove(tok_ind)
                tmp_map[w] = "<TOK%d>" % tok_ind
                rs.append(tmp_map[w])
        s_res = ' '.join(rs)
        data['user_inform_who'] = s_res
    return data

for d in data3:
    d_sub = process_data(d)
    all_data.append(d_sub)

for d in all_data:
    add_noise(d)

random.shuffle(all_data)
print 'Data size:', len(all_data)
tt = int(len(all_data)*0.8)
train_data = all_data[:tt]
dev_data = all_data[tt:]
print '\n==========================================\n'
print 'Train data:'
pprint.pprint(train_data[:80])
print '\n==========================================\n'
print 'Dev data:'
pprint.pprint(dev_data[:80])

cPickle.dump(train_data, open('tmp/train_data.pkl', 'w'))
cPickle.dump(dev_data, open('tmp/dev_data.pkl', 'w'))

