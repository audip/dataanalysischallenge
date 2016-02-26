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

    def __init__(self):
        self.state = ""
        self.gender = ""
        self.year = ""
        self.name = ""
        self.birthCount = 0

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

    # Perform unit testing to check for object creation, linked to Travis-CI (https://travis-ci.org/)
    def testObjectCreation(self):
        return "Object creation successful"

def dataUnload(file_name, yearOfBirth):
    """ Unwraps data from the dataset using filename """
    bornInYear = []
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
                        if baby.getYear() in yearOfBirth:
                            bornInYear.append(baby.getAll())
    print "3. File read completed"
    return bornInYear

def findNameCount(babyList = []):
    """ Finds babies born in 2013 and maps them in a dictionary """
    print "4. Finding name counts of babies"
    dictionary_baby = {}
    for babyData in babyList:
        baby = babyDetails(babyData)
        maleCount = 0
        femaleCount = 0
        # name = str(baby.getName())
        # print name+ "Dictionary:"+dictionary_baby[name]
        if baby.getName() not in dictionary_baby:
            # Format for data dict(Key, "M::count1::F::count2")
            # print "Baby"+baby.getName()+" didn't exist"
            if baby.getGender() in 'M':
                dictionary_baby[baby.getName()] = "M::"+str(baby.getBirthCount())+"::F::0"
            elif baby.getGender() in 'F':
                dictionary_baby[baby.getName()] = "M::0::F::"+str(baby.getBirthCount())
        else:
            # print "Baby"+baby.getName()+" exists+ Dict:"+dictionary_baby[baby.getName()]
            parts = dictionary_baby[baby.getName()].split('::')
            # print parts
            maleCount = int(parts[1].strip())
            femaleCount = int(parts[3].strip())
            # print maleCount+femaleCount
            if baby.getGender() in 'M':
                # print 'Male'+str(baby.getBirthCount())
                maleCount = maleCount + baby.getBirthCount()
                dictionary_baby[baby.getName()] = "M::"+str(maleCount)+"::F::"+str(femaleCount)
            elif baby.getGender() in 'F':
                # print 'Female'+str(baby.getBirthCount())
                femaleCount = femaleCount + baby.getBirthCount()
                dictionary_baby[baby.getName()] = "M::"+str(maleCount)+"::F::"+str(femaleCount)

    print "5. Finding completed of babies name counts"
    return dictionary_baby

def findAmbigiousNames(dict_namecount={}):
    """ For all names, checks for names with maleCount, femaleCount greater than zero and sums it up  """
    print "6. Finding ambigious names with counts greater than 0"
    maleCount = 0
    femaleCount = 0
    totalCount = 0
    dictionary_baby = {}
    for key, value in dict_namecount.items():
        # Value: M::100::F:200
        parts = value.split('::')
        maleCount = int(parts[1].strip())
        femaleCount = int(parts[3].strip())
        if maleCount > 0 and femaleCount > 0:
            totalCount = maleCount + femaleCount
            dictionary_baby[key] = totalCount

    print "7. Found all the ambigious names"
    return dictionary_baby

def top5(dict_namecount = {}):
    """ Takes dictionary as input and prints top five name """
    print "8. Sorting the list to find the top 5"
    sorted_list = sorted(dict_namecount.items(), key=operator.itemgetter(1))
    sorted_list.reverse()
    for loop_var in range(5):
        print sorted_list[loop_var]

def main():
    print "9 steps in total"
    print "1. Main program initiated"
    babyBornInYear = dataUnload(fixtureName, '2013')
    dict_namecount = findNameCount(babyBornInYear)
    dict_ambigious = findAmbigiousNames(dict_namecount)
    top5(dict_ambigious)
    print "9. Main program finished"

if __name__ == "__main__":main()
