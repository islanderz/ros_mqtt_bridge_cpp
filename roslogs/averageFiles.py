#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, os.path
import csv
from operator import add

A = os.listdir('.');

lenA = len(A);

i = 0;
navFiles = [];
vidFiles = [];
while i < lenA:
  if(A[i].startswith("log_file_image")):
    vidFiles.append(A[i]);
  elif(A[i].startswith("log_file_nav")):
    navFiles.append(A[i]);
  i+=1;

print "Processing ",
print len(navFiles),
print " Navdata files and ",
print len(vidFiles),
print " Video Files"

if(len(navFiles) != len(vidFiles)):
  print "mismatching no. of vidFiles and navFiles.. please check current working directory.."
  exit();

i = 0;


totalNavAvg = [0 for x in range(60)]
totalVidAvg = [0 for x in range(60)]

navRange = range(0,12000,200);
vidRange = range(0,1800,30);

AllNavAvg = np.zeros((60,1));
AllVidAvg = np.zeros((60,1));

i = 0;
maxNavDelay = [0 for x in range(60)]
minNavDelay = [100000 for x in range(60)]
maxVidDelay = [0 for x in range(60)]
minVidDelay = [100000 for x in range(60)]

while i < len(navFiles):
  navLines = [line.rstrip('\n') for line in open(navFiles[i])];
  vidLines = [line.rstrip('\n') for line in open(vidFiles[i])];

  navDelays = np.zeros((60,1));
  vidDelays = np.zeros((60,1));

  lineCount = 0;
  while lineCount < 60:
    navDelays[lineCount] = float(navLines[lineCount]);
    vidDelays[lineCount] = float(vidLines[lineCount]);

    totalNavAvg[lineCount] += (float)(navLines[lineCount]);
    totalVidAvg[lineCount] += (float)(vidLines[lineCount]);


    if(maxNavDelay[lineCount] < float(navLines[lineCount])):
        maxNavDelay[lineCount] = float(navLines[lineCount]);
    if(maxVidDelay[lineCount] < float(vidLines[lineCount])):
        maxVidDelay[lineCount] = float(vidLines[lineCount]);
    if(minVidDelay[lineCount] > float(vidLines[lineCount])):
        minVidDelay[lineCount] = float(vidLines[lineCount]);
    if(minNavDelay[lineCount] > float(navLines[lineCount])):
        minNavDelay[lineCount] = float(navLines[lineCount]);
    lineCount = lineCount + 1;
  i+=1;
  navDelays = np.vstack(navDelays);
  vidDelays = np.vstack(vidDelays);
  AllNavAvg = np.hstack((AllNavAvg, np.asarray(navDelays)));
  AllVidAvg = np.hstack((AllVidAvg, np.asarray(vidDelays)));

AllNavAvg = AllNavAvg[:,1:];
AllVidAvg = AllVidAvg[:,1:];
totalNavAvg = [ x/len(navFiles) for x in totalNavAvg];
totalVidAvg = [ x/len(vidFiles) for x in totalVidAvg];

#displaying the error bar graph for images
minPlusMax = [x+y for x,y in zip (minVidDelay, maxVidDelay) ]
e = [x / 2 for x in minPlusMax]
plt.ylabel('Averagea delay (sec)')
plt.xlabel('No of IMAGE messages')
plt.errorbar(vidRange, totalVidAvg, e, linestyle='-', marker='o')
plt.show()

#displaying the error bar graph for navdata
minPlusMax = [x+y for x,y in zip (minNavDelay, maxNavDelay) ]
e = [x / 2 for x in minPlusMax]
plt.ylabel('Averagea delay (sec)')
plt.xlabel('No of Navdata messages')
plt.errorbar(navRange, totalNavAvg, e, linestyle='-', marker='^')
plt.show()

#displaying the error bar graph for images and navdata combined
plt.ylabel('Averagea delay (sec)')
plt.xlabel('Time(sec). Displaying Images and Navdata Delays Combined')
plt.errorbar(range(60), totalVidAvg, e, linestyle='-', marker='o', label='Video Messages')
plt.errorbar(range(60), totalNavAvg, e, linestyle='-', marker='^', label='Navdata Messages')
plt.legend()
plt.show()

plt.ylabel('Averagea delay (sec)')
plt.xlabel('No of IMAGE messages')
plt.plot(vidRange,totalVidAvg)
plt.show()

plt.ylabel('Averagea delay (sec)')
plt.xlabel('No of Navdata messages')
plt.plot(navRange,totalNavAvg)
plt.show();

plt.boxplot(AllVidAvg,0,'-');
#plt.boxplot(AllVidAvg);
plt.show()

plt.boxplot(AllNavAvg,0,'-');
#plt.boxplot(AllNavAvg);
plt.show()
#print len([name for name in    os.listdir('.') if os.path.isfile(name)])
