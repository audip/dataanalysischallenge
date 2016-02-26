# Data Analysis Challenge

Challenge for developing most efficient, robust and implements high-quality code for the problems.

[![Build Status](https://travis-ci.com/audip/dataanalysischallenge.svg?token=GHivzknmxHfYWrAfnY58&branch=master)](https://travis-ci.com/audip/dataanalysischallenge)
https://travis-ci.com/audip/dataanalysischallenge.svg?token=GHivzknmxHfYWrAfnY58&branch=master

## Problem Statement

The data can be downloaded in zip format from:
http://www.ssa.gov/oact/babynames/state/namesbystate.zip. The data description can be found in the zip folder. Please answer the following questions.
- What is the most popular name of all time in US? (Of either gender.)
- What are the top 5 most gender ambiguous names in 2013?

Use the data provided in the attachment for this question. The data of interest begins from line 79 where you will find 6 columns of numeric data. The column names are Time, Temperature, Heat.Flow, Heat.Capacity, Sample.Purge.Flow and LNCS.Pressure. Submit a HTML file containing 2 plots. The first plot of Temperature v/s Time and second plot is between Heat.Flow v/s Temperature. It will be impressive if the plots are interactive in nature. (PS: This is one of the actual data-file that from Deptt. of Material Science, TAMU)

## User Stories

The following user stories have been implemented:
- [x] User can find most popular baby name of all time from the dataset: http://www.ssa.gov/oact/babynames/state/namesbystate.zip
- [x] User can see top 5 most gender ambigious names in 2013 (Optional)
- [x] User can view HTML reports with plots of actual data as received from log file

The following additional (optional) user stories have been implemented:
- [x] Implement robust project structure for working in fast-paced team setting
- [x] Implements Plotly (http://plot.ly) API for modern graph plotting
- [x] Implements classes & creates objects for better reusability
- [x] Enforces validation for input files by checking against unacceptable file format
- [x] Implements version control system (Git) to keep track of documents and ability to revert back
- [x] Performs unit testing to check for any break in builds and introduction of any bugs (Testing script included)
- [x] Deploys on Continous Integration (CI) platform - Travis-CI, for continously testing the builds being deployed and reporting failures.
- [x] Builds a dashboard for easily viewing reports, based on Twitter's bootstrap framework

## Installation

1. Downloading the zip archive, consisting of powerful project structure for medium to large projects
2. Run the script for dependencies to be installed: `pip install -r requirements.txt`

## Testing

- Run in `dataanalysischallenge/`: `nosetests -v --with-coverage --cover-package=dataanalysischallenge --cover-inclusive --cover-erase tests`
