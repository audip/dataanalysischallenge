#!/usr/bin/python

import os
import zipfile
import operator
import requests

dictionary_namecount = {}
progress = 0
total_names = 5647426
archive_link = "http://www.ssa.gov/oact/babynames/state/namesbystate.zip"
file_record = requests.get(archive_link)

with zipfile.ZipFile(file_record) as namesbystate:
    for filename in namesbystate.namelist():
        if not os.path.isdir(filename) and filename != 'StateReadMe.pdf':
            # if m.endswith('.mp3'):
            # read the file
            with namesbystate.open(filename) as f:
                for line in f:
                    # processing line by line
                    str = line.split(',')
                    baby_name = str[3]
                    progress = progress + 1
                    if baby_name not in dictionary_namecount:
                        dictionary_namecount[baby_name] = 1
                    else:
                        dictionary_namecount[baby_name] += 1

# def keywithmaxval(d):
#     # Fastest key value sorter approach
#     # Key: Baby's name, Value: Count of name occurence
#     name_count=list(d.values())
#     dict_key=list(d.keys())
#     return dict_key[name_count.index(max(name_count))]
#
# highest_key = keywithmaxval(dictionary_namecount)
# print highest_key

sorted_list = sorted(dictionary_namecount.items(), key=operator.itemgetter(1))
sorted_list.reverse()
for loop_var in range(5):
    print sorted_list[loop_var]
