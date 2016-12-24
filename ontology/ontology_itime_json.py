# generate ontology_itime.json
import json
ontology_itime = {}

ontology_itime['title'] = ['arbitrary values']

ontology_itime['startDay'] = ['YYYYMMDD']
ontology_itime['startTime'] = []
for i in range(24):
	ontology_itime['startTime'].append('%02d:%02d:%02d' % (i, 0, 0))
	ontology_itime['startTime'].append('%02d:%02d:%02d' % (i, 30, 0))

ontology_itime['duration'] = []
ontology_itime['duration'].append('00:30:00')
for i in range(1, 24):
	ontology_itime['duration'].append('%02d:%02d:%02d' % (i, 0, 0))
	ontology_itime['duration'].append('%02d:%02d:%02d' % (i, 30, 0))
ontology_itime['duration'].append('24:00:00')

ontology_itime['invitee'] = ['dontcare', 'lists of arbitrary names']

ontology_itime['location'] = ['dontcare', 'https://maps.unimelb.edu.au/parkville/building']

ontology_itime['frequency'] = ['dontcare', 'daily', 'weekly', 'monthly', 'yearly']

ontology_itime['interval'] = []
for i in range(1, 31):
	ontology_itime['interval'].append('%02d' % i)

ontology_itime['untilDay'] = ['YYYYMMDD']

with open('ontology_itime.json', 'w') as outfile:
    json.dump(ontology_itime,
    		  outfile,
    		  sort_keys=True,
    		  indent=4,
    		  separators=(',', ': '))
