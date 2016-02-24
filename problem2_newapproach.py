#!/usr/bin/python

import os
import zipfile
import operator

dictionary_namecount = {}

class babyDetails(object):
    def __init__(self, rawData):
            parts = rawData.split(',')
            # Parses values into class variables
            self.state = parts[0].strip()
            self.gender = parts[1].strip()
            self.year = parts[2].strip()
            self.name = parts[3].strip()
            self.birthCount = int(parts[4].strip())

    def printsOutput(self):
        print self.state+"::"+self.gender+"::"+self.year+"::"+self.name+"::"+str(self.birthCount)

    def getName(self):
        return self.name
    def getState(self):
        return self.state
    def getGender(self):
        return self.gender
    def getYear(self):
        return self.year
    def getBirthCount(self):
        return self.birthCount

with zipfile.ZipFile('fixtures/namesbystate.zip') as namesbystate:
    for filename in namesbystate.namelist():
        if not os.path.isdir(filename) and filename != 'StateReadMe.pdf':
            # if m.endswith('.mp3'):
            # read the file
            with namesbystate.open(filename) as f:
                for line in f:
                    # processing line by line
                    baby = babyDetails(line)
                    print baby.getBirthCount()

sorted_list = sorted(dictionary_namecount.items(), key=operator.itemgetter(1))
sorted_list.reverse()
for loop_var in range(5):
    print sorted_list[loop_var]