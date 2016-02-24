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
                    string_name = line.split(',')
                    birth_year = string_name[2]
                    gender = string_name[1]
                    baby_name = string_name[3]
                    birth_count = int(string_name[4].splitlines()[0])
                    progress = progress + 1
                    # print birth_year in '2013'
                    if birth_year in '2013':
                        # print "Gender:"+gender+" Birth_year:"+birth_year+" baby_name:"+baby_name+" BirthCount:"+str(birth_count)
                        if baby_name not in dictionary_namecount:
                            dictionary_namecount[baby_name] = gender+'::'+birth_count
                        else:
                            value = dictionary_namecount[baby_name]
                            string_line = value.split('::')
                            if len(string_line) == 2:
                                gender1 = string_line[0]
                                count = string_line[1]
                                if gender1 in 'F':
                                    dictionary_namecount[baby_name] =
                            elif len(string_line) == 3:
                                gender1 = string_line[0]
                                gender2 = string_line[1]
                                count = string_line[2]
                            if gender in 'F':
                                dictionary_namecount[baby_name] += birth_count

sorted_list = sorted(dictionary_namecount.items(), key=operator.itemgetter(1))
sorted_list.reverse()
for loop_var in range(5):
    print sorted_list[loop_var]
