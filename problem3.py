#!/usr/bin/python

import os
import operator
import math
import plotly.plotly as py
import plotly.graph_objs as go

fixtureName = 'fixtures/Sample_DSC_Data.txt'
path = 'fixtures/'

class industrialDetails(object):
    def __init__(self, rawData):
            raw = rawData.strip()
            parts = raw.split('\t')
            # Parses values into class variables
            # for part in parts:
            #     if 'E-' in part:
            #         value = part.rstrip('\r\t').split('E-')
            #         powerOf = pow(10,(-1*int(value[1])))
            #         part = float(value[0]) * powerOf

            self.time = float(parts[0].strip())
            self.temperature = float(parts[1].strip())
            self.heatFlow = float(parts[2].strip())
            self.heatCapacity = float(parts[3].strip())
            self.samplePurgeFlow = float(parts[4].strip())
            self.pressure = float(parts[5].strip())


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
    # Unzips the file and return industrial data
    temperatureList = []
    timeList = []
    heatFlowList = []
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
                    # Starts reading line by line
                    if lineToRead == 1:
                        counter += 1
                        raw = line.strip()
                        parts = line.rstrip("\n").split("\t")
                        # Checks for exponential data e.g.: 3.32E-4
                        for part in parts:
                            if 'E-' in part:
                                value = part.rstrip('\r\t').split('E-')
                                powerOf = pow(10,(-1*int(value[1])))
                                part = float(value[0]) * powerOf
                        # Checks as time can never be negative
                        time = parts[0]
                        if float(time) > 0.0:
                            industrialData = industrialDetails(line)
                            timeList.append(industrialData.getTime())
                            temperatureList.append(industrialData.getTemperature())
                            heatFlowList.append(industrialData.getHeatFlow())
                            # industry.printsOutput()
                    # if counter > 10:
                    #     break

    plot1 = plotsGraph(timeList, temperatureList, 'Industrial: Temperature v/s Time', 'Time', 'Temperature')
    plot2 = plotsGraph(timeList, heatFlowList, 'Industrial: Heat Flow v/s Time', 'Time', 'Hear Flow')
    # Heat Flow vs Time
    reportToHTML(plot1, plot2)
    # print timeList
    # print temperatureList
    # print heatFlowList

def plotsGraph(list1, list2, graphTitle, xAxisTitle, yAxisTitle):
    trace = go.Scatter(
        x = list1,
        y = list2,
        name= 'Trace'
    )
    data = [trace]

    layout = go.Layout(
        title=graphTitle,
        xaxis=dict(
            title=xAxisTitle
        ),
        yaxis=dict(
            title=yAxisTitle
        ), showlegend=True, legend=dict(
            x=0.9,
            y=1
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename=graphTitle, sharing='public', auto_open=False)
    return plot_url

def reportToHTML(plot_url1, plot_url2):
    html_string = '''
    <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
            <style>body{ margin:0 100; background:whitesmoke; }</style>
        </head>
        <body>
            <h1>Plot 1: Industrial Temperature vs Time</h1>

            <div style="margin:auto;">
                <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
        src="''' + plot_url1 + '''.embed?width=800&height=450"></iframe>
            </div>
            <h1>Plot 2: Industrial Temperature vs Time</h1>

            <div style="margin:auto;">
                <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
        src="''' + plot_url2 + '''.embed?width=800&height=450"></iframe>
            </div>
        </body>
    </html>'''

    filename = 'reports/problem3.html'
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "w") as f:
        f.write(html_string)
        f.close()

    print "Plot complete, report available at ./reports/problem3.html"
    # webbrowser.open(filename)
    # full_path = os.getcwd()+'/'+filename
    # print full_path
    # webbrowser.open(full_path)

def main():
    print "1. Main program initiated"
    dataUnload(fixtureName)
    print "n. Main program finished"

if __name__ == "__main__":main()
