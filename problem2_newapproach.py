#!/usr/bin/python

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

def dataUnload(file_name, yearOfBirth):
    bornInYear = []
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
                        if baby.getYear() in yearOfBirth:
                            bornInYear.append(baby.getAll())
    return bornInYear

def findNameCount(babyList = []):
    dictionary_baby = {}
    for babyData in babyList:
        baby = babyDetails(babyData)
        maleCount = 0
        femaleCount = 0
        # name = str(baby.getName())
        # print name+ "Dictionary:"+dictionary_baby[name]
        if baby.getName() not in dictionary_baby:
            # Format for data dict(Key, "M::count1::F::count2")
            print "Baby"+baby.getName()+" didn't exist"
            if baby.getGender() in 'M':
                dictionary_baby[baby.getName()] = "M::"+str(baby.getBirthCount())+"::F::0"
            elif baby.getGender() in 'F':
                dictionary_baby[baby.getName()] = "M::0::F::"+str(baby.getBirthCount())
        else:
            print "Baby"+baby.getName()+" exists+ Dict:"+dictionary_baby[baby.getName()]
            parts = dictionary_baby[baby.getName()].split('::')
            print parts
            maleCount = int(parts[1].strip())
            femaleCount = int(parts[3].strip())
            print maleCount+femaleCount
            if baby.getGender() in 'M':
                print 'Male'+str(baby.getBirthCount())
                maleCount = maleCount + baby.getBirthCount()
                dictionary_baby[baby.getName()] = "M::"+str(maleCount)+"::F::"+str(femaleCount)
            elif baby.getGender() in 'F':
                print 'Female'+str(baby.getBirthCount())
                femaleCount = femaleCount + baby.getBirthCount()
                dictionary_baby[baby.getName()] = "M::"+str(maleCount)+"::F::"+str(femaleCount)
    return dictionary_baby

def findAmbigiousNames(dict_namecount={}):
    maleCount = 0
    femaleCount = 0
    for key, value in dict_namecount.items():
        # Value: M::100::F:200
        parts = value.split('::')
        maleCount = int(parts[1].strip())
        femaleCount = int(parts[3].strip())

def main():
    babyBornInYear = dataUnload(fixtureName, '2013')
    dict_namecount = findNameCount(babyBornInYear)
    dict_ambigious = findAmbigiousNames(dict_namecount)
    for key, value in dict_ambigious.items():
        print key+":"+value
    # for item in bornInYear:
    #     print item

if __name__ == "__main__":main()

# sorted_list = sorted(dictionary_namecount.items(), key=operator.itemgetter(1))
# sorted_list.reverse()
# for loop_var in range(5):
#     print sorted_list[loop_var]
