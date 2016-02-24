#!/usr/bin/python

import os
import zipfile
import operator

dictionary_namecount = {}
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

def dataUnload(file_name, yearOfBirth):
    bornInYear = []
    with zipfile.ZipFile(file_name) as namesbystate:
        for filename in namesbystate.namelist():
            extension = os.path.splitext(filename)[1][1:].strip().lower()
            if not os.path.isdir(filename) and extension == 'txt':
                # read the file
                with namesbystate.open(filename) as f:
                    for line in f:
                        # processing line by line
                        baby = babyDetails(line)
                        if baby.getYear() in yearOfBirth:
                            bornInYear.append(baby.getAll())
    return bornInYear

def processingData(babyList = []):
    for babyData in babyList:
        baby = babyDetails(str(babyData))
        print baby.getAll()

def main():
    babyBornInYear = dataUnload(fixtureName, '2013')
    processingData(babyBornInYear)
    # for item in bornInYear:
    #     print item

if __name__ == "__main__":main()

# sorted_list = sorted(dictionary_namecount.items(), key=operator.itemgetter(1))
# sorted_list.reverse()
# for loop_var in range(5):
#     print sorted_list[loop_var]
