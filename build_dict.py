import cPickle

# the vocabulary uses only all_data1.pkl

all_words = set([])
ontology_bool = ['user_affirm',  'user_ack',  'user_finish', 'user_start',  \
                   'user_finish',  'user_start',  'user_restart',  'user_report',  \
                   'user_dont_want_report']
ontology_time = ['user_inform_whenstart_hour', 'user_inform_whenstart_min',  \
                   'user_inform_whened_hour', 'user_inform_whened_min', \
                   'user_inform_duration_hour', 'user_inform_duration_min']
ontology_str = ['user_inform_what','user_inform_day','user_inform_where', 'text']
data = cPickle.load(open('tmp/all_data2.pkl'))

for d in data:
    for ont in ontology_str:
        all_words = all_words.union(d[ont].split())
    if d['user_inform_who'] != '<NO>':
        for n in d['user_inform_who']:
            all_words.add(n)

all_words = ['<END>', '<START>', '<TOK0>', '<TOK1>', '<TOK2>', '<TOK3>', '<TOK4>', '<TOK5>', '<TOK6>', '<TOK7>', '<TOK8>', '<TOK9>', '<TOK10>', '<TOK11>', '<TOK12>', '<TOK13>', '<TOK14>', '<TOK15>', '<TOK16>', '<TOK17>', '<TOK18>', '<TOK19>'] + list(all_words)

ind2word = {}
word2ind = {}

for (ind, w) in enumerate(all_words):
    ind2word[ind] = w
    word2ind[w] = ind

cPickle.dump((ind2word, word2ind, ontology_bool, ontology_time, ontology_str), open('./tmp/dict.pkl', 'w'))

print ind2word.items()[:50]
print word2ind.items()[:50]
print len(ind2word), len(word2ind)
