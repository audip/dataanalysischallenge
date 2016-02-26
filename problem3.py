#!/usr/bin/python

import os
import operator
import math
import plotly.plotly as py
import plotly.graph_objs as go

fixtureName = 'fixtures/Sample_DSC_Data.txt'
path = 'fixtures/'

class industrialDetails(object):
    def __init__(self):
        self.time = 0.0
        self.temperature = 0.0
        self.heatFlow = 0.0
        self.heatCapacity = 0.0
        self.samplePurgeFlow = 0.0
        self.pressure = 0.0

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

    # Perform unit testing to check for object creation, linked to Travis-CI (https://travis-ci.org/)
    def testObjectCreation(self):
        return "Object creation successful"

def dataUnload(file_name):
    # Unzips the file and return industrial data
    temperatureList = []
    timeList = []
    heatFlowList = []
    heatCapacityList = []
    purgeFlowList = []
    pressureList = []
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
                            heatCapacityList.append(industrialData.getheatCapacity())
                            purgeFlowList.append(industrialData.getSamplePurgeFlow())
                            pressureList.append(industrialData.getPressure())

                            # industry.printsOutput()
                    # if counter > 10:
                    #     break

    plot1 = plotsGraph(timeList, temperatureList, 'Industrial: Temperature v/s Time', 'Time', 'Temperature')
    plot2 = plotsGraph(timeList, heatFlowList, 'Industrial: Heat Flow v/s Time', 'Time', 'Heat Flow')
    plot3 = plotsGraph(timeList, heatCapacityList, 'Industrial: Heat Capacity v/s Time', 'Time', 'Heat Capacity')
    plot4 = plotsGraph(timeList, purgeFlowList, 'Industrial: Purge Flow v/s Time', 'Time', 'Purge Flow')
    plot5 = plotsGraph(timeList, pressureList, 'Industrial: Pressure v/s Time', 'Time', 'Pressure')
    # Heat Flow vs Time
    reportToHTML(plot1, plot2, plot3, plot4, plot5)
    # print timeList
    # print temperatureList
    # print heatFlowList

def plotsGraph(list1, list2, graphTitle, xAxisTitle, yAxisTitle):
    trace = go.Scatter(
        x = list1,
        y = list2,
        name= 'Trace',
        fill='tozeroy'
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
            x=1,
            y=1
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename=graphTitle, sharing='public', auto_open=False)
    return plot_url

def reportToHTML(plot_url1, plot_url2,plot_url3, plot_url4, plot_url5):
    html_string = '''
    <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">

            <!-- Bootstrap Core CSS -->
            <!-- Latest compiled and minified CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
            <!-- Custom CSS -->
            <link rel="stylesheet" href="../dashboard/style.css">

            <!-- Custom Fonts -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
            <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700|Kaushan+Script|Droid+Serif:400,700,400italic,700italic|Roboto+Slab:400,100,300,700" rel="stylesheet" type="text/css">

        </head>
        <body id="page-top" class="">
            <div id="ip-container" class="ip-container ">
                <div class="main-container">
                    <div class="ip-main">
                        <div class="browser">
                            <!-- Navigation -->
                            <nav class="navbar navbar-default navbar-fixed-top loading" id="navbar">
                                <!-- Brand and toggle get grouped for better mobile display -->
                                <div class="navbar-header page-scroll">
                                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                                        <span class="sr-only">Toggle navigation</span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                    </button>
                                    <a class="navbar-brand page-scroll" href="#page-top">Project Data Analysis</a>
                                </div>

                                <!-- Collect the nav links, forms, and other content for toggling -->
                                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                                    <ul class="nav navbar-nav navbar-right">
                                        <li class="hidden">
                                            <a href="#page-top"></a>
                                        </li>
                                        <li>
                                            <a class="page-scroll" href="#"><i class="fa fa-lg fa-archive"></i> Problem 1</a>
                                        </li>
                                        <li>
                                            <a class="page-scroll" href="#"><i class="fa fa-lg fa-archive"></i> Problem 2</a>
                                        </li>
                                        <li>
                                            <a class="page-scroll" href="#"><i class="fa fa-lg fa-archive"></i> Problem 3</a>
                                        </li>
                                    </ul>
                                </div>
                                <!-- /.navbar-collapse -->
                        </div>
                        <!-- /.container-fluid -->
                        </nav>

                        <!-- Header -->
                        <div class="header">
                            <div class="container">
                                <h1 style="margin-top:100px">Plot 1: Industrial Temperature vs Time</h1>

                                <div style="margin:auto;">
                                    <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
                            src="''' + plot_url1 + '''.embed?width=800&height=450"></iframe>
                                </div>
                                <h1 style="margin-top:100px">Plot 2: Industrial Heat Flow vs Time</h1>

                                <div style="margin:0 auto 50 auto">
                                    <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
                            src="''' + plot_url2 + '''.embed?width=800&height=450"></iframe>
                                </div>
                                <h1 style="margin-top:100px">Plot 3: Industrial Heat Capacity vs Time</h1>

                                <div style="margin:0 auto 50 auto">
                                    <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
                            src="''' + plot_url3 + '''.embed?width=800&height=450"></iframe>
                                </div>
                                <h1 style="margin-top:100px">Plot 4: Industrial Purge Flow vs Time</h1>

                                <div style="margin:0 auto 50 auto">
                                    <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
                            src="''' + plot_url4 + '''.embed?width=800&height=450"></iframe>
                                </div>
                                <h1 style="margin-top:100px">Plot 5: Industrial Pressure vs Time</h1>

                                <div style="margin:0 auto 50 auto">
                                    <iframe width="800" height="450" frameborder="0" seamless="seamless" scrolling="no"
                            src="''' + plot_url5 + '''.embed?width=800&height=450"></iframe>
                                </div>
                            </div>
                        </div>
                        <footer>
                            <div class="container foot">
                                <div class="row">
                                    <div class="col-md-4">
                                        <span class="copyright" style="text-align:center">Developed by Aditya Purandare in 2016</span>
                                    </div>
                                </div>
                            </div>
                        </footer>
                    </div>
                </div>
            </div>

            <!-- jQuery -->
            <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

            <!-- Latest compiled and minified JavaScript -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

            </body>
    </html>'''

    filename = 'dashboard/problem3.html'
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "w") as f:
        f.write(html_string)
        f.close()

    print "Plot complete, report available at ./dashboard/problem3.html"
    # webbrowser.open(filename)
    # full_path = os.getcwd()+'/'+filename
    # print full_path
    # webbrowser.open(full_path)

def main():
    print "1. Main program initiated"
    dataUnload(fixtureName)
    print "n. Main program finished"

if __name__ == "__main__":main()
