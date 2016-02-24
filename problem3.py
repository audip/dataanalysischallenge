#!/usr/bin/python

import os
import operator

fixtureName = 'fixtures/Sample_DSC_Data.txt'
path = 'fixtures/'

class industrialDetails(object):
    def __init__(self, rawData):
            parts = rawData.split(' ')
            # Parses values into class variables
            self.time = int(parts[0].strip())
            self.temperature = int(parts[1].strip())
            self.heatFlow = int(parts[2].strip())
            self.heatCapacity = int(parts[3].strip())
            self.samplePurgeFlow = int(parts[4].strip())
            self.pressure = int(parts[5].strip())

    def printsOutput(self):
        print str(self.time)+","+str(self.temperature)+","+str(self.heatFlow)+","+str(self.heatCapacity)+","+str(self.samplePurgeFlow)+","+str(self.pressure)
    def getAll(self):
        return str(self.time)+","+str(self.temperature)+","+str(self.heatFlow)+","+str(self.heatCapacity)+","+str(self.samplePurgeFlow)+","+str(self.pressure)
    def getTime(self):
        return self.time
    def getTemperature(self):
        return self.temperature
    def getHeatFlow(self):
        return self.heatFlow
    def getheatCapacity(self):
        return self.heatCapacity
    def getSamplePurgeFlow(self):
        return self.samplePurgeFlow
    def getPressure(self):
        return self.pressure

def dataUnload(file_name):
    # Unzips the file and return babies born in 2013
    counter = 0
    lineToRead = 0
    for filename in os.listdir(path):
        extension = os.path.splitext(filename)[1][1:].strip().lower()
        if not os.path.isdir(filename) and extension == 'txt':
            filename = os.path.join(path, filename)
            with open(filename, "r") as f:
                for line in f:
                    # processing line by line
                    # print "hello"
                    if line.strip() == "StartOfData":
                        lineToRead = 1
                        # Skips the StartOfData line
                        continue
                    if lineToRead == 1:
                        counter += 1
                        print line
                    if counter > 100:
                        break

def main():
    print "1. Main program initiated"
    dataUnload(fixtureName)
    print "n. Main program finished"

if __name__ == "__main__":main()
