#!/usr/bin/python

import os
import zipfile
import operator

dictionary_namecount = {}
progress = 0
total_names = 5647426

with zipfile.ZipFile('namesbystate.zip') as namesbystate:
    for filename in namesbystate.namelist():
        if not os.path.isdir(filename) and filename != 'StateReadMe.pdf':
            # if m.endswith('.mp3'):
            # read the file
            with namesbystate.open(filename) as f:
                for line in f:
                    # processing line by line
                    str = line.split(',')
                    baby_name = str[3]
                    birth_count = int(str[4].splitlines()[0])
                    progress = progress + 1
                    if baby_name not in dictionary_namecount:
                        dictionary_namecount[baby_name] = birth_count
                    else:
                        dictionary_namecount[baby_name] += birth_count

sorted_list = sorted(dictionary_namecount.items(), key=operator.itemgetter(1))
sorted_list.reverse()
for loop_var in range(5):
    print sorted_list[loop_var]
