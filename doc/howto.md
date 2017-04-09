This document describes how to use the scripts to generate data for training the NLU component.

# Quick Example

Please click [here](../quick_example.ipynb).

# Data Format

- The bool ontology is a string, '<YES\>' or '<NO\>'. (e.g. 'user_affirm': '<NO\>')
- The string ontology is a string. (e.g. 'user_inform_what': u'watch a movie')
- The time ontology is a number. The following description is IMPORTANT:
    - The hour is in the range [0, 24]. Number 24 is INCLUDED, meaning that the sentence does not mention the hour information (start hour, finish hour).
    - The minute is in the range [0, 4]. 0 means xx:00, 1 means xx:15, 2 means xx:30, 3 means xx:45, 4 means the sentence does not mention the minute information (start minute, finish minute).
- The ontology 'user_inform_who' is a list. (e.g. 'user_inform_who': [u'kaja', u'allsun', u'rebecca', u'tam']).

# How To

* In event_generator.py, you can change the ontology file to be used in the construction function:
```
    ontology = json.load(open('./ontology_itime3.json'))
```
        By defining the ontology file, we can use different event titles, different people name, etc. There are currently 3 ontology files: ontology_itime1-3.json.

* Run build_data1.py. It writes the data to './tmp/all_data3.pkl', and prints the first 50 data in console. The following is an example:
```
     {'text': u"alarm me next monday from seven forty five at night till ten fifteen pm . set the location as old geology , and i'm going with jena . ",
      'user_ack': '<NO>',
      'user_affirm': '<NO>',
      'user_dont_want_report': '<NO>',
      'user_finish': '<NO>',
      'user_inform_day': 'next monday',
      'user_inform_duration_hour': 24,
      'user_inform_duration_min': 4,
      'user_inform_what': '<NO>',
      'user_inform_whened_hour': 22,
      'user_inform_whened_min': 1,
      'user_inform_whenstart_hour': 19,
      'user_inform_whenstart_min': 3,
      'user_inform_where': 'old geology',
      'user_inform_who': [u'jena'],
      'user_report': '<NO>',
      'user_restart': '<NO>',
      'user_start': '<NO>'}
```
        Basically, that's all you need to do to generate the data.

* (Optional) Run build_dict.py. It generates the dictionary files. It considers the vocabulary of the training data is given, while unseen words in the dev data will be replaced with special tokens.

* (Optional) There is another script build_traindata.py, which is not very important. It does two things:
    * Add noise to the data, by randomly replace one word with another.
    * It splits the data into training data and dev data. Furthermore, it considers the vocabulary of the training data is given, while unseen words in the dev data will be replaced with special tokens.
    
# How It Works

Most of the jobs are handled by the process() function in build_data1.py. The basic idea is to generate dialogs as usual. But since we are only interested in NLU, we will ignore unrelevent parts in the dialogs, such as the system's response. In process() the action list of the whole dialog is obtained by
```
a = list(act_list[k])
```
(You can print it to see what it looks like.)
Then we only process interested sentences:
```
for act in a:
    if act == 'user_affirm' or act == 'user_ack' or act == 'user_finish' \
       or act == 'user_start' or act == 'user_restart' \
       or act == 'user_report' or act == 'user_dont_want_report':
        res[act] = '<YES>'
        isUser = True
    elif isinstance(act, tuple) and act[0] == 'user_inform':
        if act[1] == 'what':
            res['user_inform_what'] = act[2].lower()
    ....
```
This means that it picks out the actions of 'user_affirm', 'user_ack', ..., 'user_inform'. Actually in the NLU task, only 'user_inform' is of interest. It is not difficult to change the script to only generate 'user_inform' sentences.