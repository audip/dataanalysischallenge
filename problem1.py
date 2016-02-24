#!/usr/bin/python
# Python 2.7

import os
import zipfile
import operator

fixtureName = 'fixtures/namesbystate.zip'

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
        print self.state+","+self.gender+","+self.year+","+self.name+","+str(self.birthCount)
    def getAll(self):
        return self.state+","+self.gender+","+self.year+","+self.name+","+str(self.birthCount)
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

def dataUnload(file_name):
    """ Unwraps data from the dataset using filename """
    dictionary_namecount = {}
    print "2. File read initiated"
    # Unzips the file and return babies born in 2013
    with zipfile.ZipFile(file_name) as namesbystate:
        for filename in namesbystate.namelist():
            extension = os.path.splitext(filename)[1][1:].strip().lower()
            if not os.path.isdir(filename) and extension == 'txt':
                # read the file & validates for txt files only
                with namesbystate.open(filename) as f:
                    for line in f:
                        # processing line by line
                        baby = babyDetails(line)
                        if int(baby.getYear()) >= 1915:
                            if baby.getName() not in dictionary_namecount:
                                dictionary_namecount[baby.getName()] = baby.getBirthCount()
                            else:
                                dictionary_namecount[baby.getName()] += baby.getBirthCount()
    print "3. File read completed"
    return dictionary_namecount

def top(dict_namecount = {}):
    """ Takes dictionary as input and prints top five name """
    print "4. Sorting the list to find the top 5"
    sorted_list = sorted(dict_namecount.items(), key=operator.itemgetter(1))
    sorted_list.reverse()
    for loop_var in range(1):
        print sorted_list[loop_var]

def main():
    print "5 steps in total"
    print "1. Main program initiated"
    dictionary_data = dataUnload(fixtureName)
    top(dictionary_data)
    print "5. Main program finished"

if __name__ == "__main__":main()
