# dataanalysischallenge
Data Analysis Challenge TAMU

## Problem Statement

The next step in the process is the code test. In the code test, you are challenged to write a script that does some common data manipulation and analysis tasks. The coding test is intended to take at least a few hours, but it is not timed and candidates are judged solely on the quality of the work done and not on the time spent on the process. Here is the list of tasks that is expected to be done from the script.

## Code Challenge:

The data can be downloaded in zip format from:
http://www.ssa.gov/oact/babynames/state/namesbystate.zip. The data description can be found in the zip folder. Please answer the following questions.
- [ ] What is the most popular name of all time in US? (Of either gender.)
- [ ] (Optional) What are the top 5 most gender ambiguous names in 2013?

Use the data provided in the attachment for this question. The data of interest begins from line 79 where you will find 6 columns of numeric data. The column names are Time, Temperature, Heat.Flow, Heat.Capacity, Sample.Purge.Flow and LNCS.Pressure. Submit a HTML file containing 2 plots. The first plot of Temperature v/s Time and second plot is between Heat.Flow v/s Temperature. It will be impressive if the plots are interactive in nature. (PS: This is one of the actual data-file that we are currently working on)

## Testing

nosetests -v --with-coverage --cover-package=dataanalysischallenge --cover-inclusive --cover-erase tests

## Submission Instructions

Try to use Python or R for scripting for the first two questions as we are using these two languages in most of our work. ipython notebook is also accepted if you are using python. Do NOT assume i have the data-set saved locally. The script should be elegant to download the data and do the analysis. Be sure to include code comments so that i know what you are trying to achieve. Once finished, please email the script and the HTML file to ramaranjanruj@tamu.edu. Do not include the downloaded data-set or any other material in the attachment. The deadline for the submission is Friday (02/26) 23:59 PM.

Feel free to ask if you have any queries. Thanks and i look forward to reviewing your work. All the best!

In the meantime, please find a link to the Materials Data Curation System(MDCS) that we are seeking to adapt and deploy within TAMU.

https://github.com/usnistgov/MDCS
