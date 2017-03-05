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


i = 0;
maxNavDelay = 0;
minNavDelay = 100000;
maxVidDelay = 0;
minVidDelay = 100000;
while i < len(navFiles):
  navLines = [line.rstrip('\n') for line in open(navFiles[i])];
  vidLines = [line.rstrip('\n') for line in open(vidFiles[i])];

  navDelays = [];
  vidDelays = [];

  lineCount = 0;
  while lineCount < 60:
    navDelays.append(float(navLines[lineCount]));
    vidDelays.append(float(vidLines[lineCount]));

    totalNavAvg[lineCount] += (float)(navLines[lineCount]);
    totalVidAvg[lineCount] += (float)(vidLines[lineCount]);

    if(maxNavDelay < float(navLines[lineCount])):
        maxNavDelay = float(navLines[lineCount]);
    if(maxVidDelay < float(vidLines[lineCount])):
        maxVidDelay = float(vidLines[lineCount]);
    if(minVidDelay > float(vidLines[lineCount])):
        minVidDelay = float(vidLines[lineCount]);
    if(minNavDelay > float(navLines[lineCount])):
        minNavDelay = float(navLines[lineCount]);
    lineCount = lineCount + 1;
  i+=1;


plt.ylabel('Averagea delay (sec)')
plt.xlabel('No of IMAGE messages')
plt.plot(vidRange,totalVidAvg)
plt.show()

plt.ylabel('Averagea delay (sec)')
plt.xlabel('No of Navdata messages')
plt.plot(navRange,totalNavAvg)
plt.show()

#print len([name for name in os.listdir('.') if os.path.isfile(name)])
