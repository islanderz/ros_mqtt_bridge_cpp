#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, os.path
import csv
from operator import add

print "Processing ",

filterFile = open("logFilter.txt", 'rt');

filterDataTime = [];
filterDataYaxis = [];

#Reading the IMU and KF files
filterReader = csv.reader(filterFile, delimiter=" ");  
 
filterCount = 0;

#Extracting first 1899 for nav and 1800 for vid
for row in filterReader: 
   filterDataTime.append(str((int(row[0])-180000)));
   filterDataYaxis.append(row[17]);
   #print(row[0]);
   filterCount+=1;
   if(filterCount >= 18000):
     break;
filterFile.close();
 
idx = 0;

plt.figure(1);
#plt.subplot(211)
plt.ylabel('Predicted x(metric)')
plt.xlabel('Time (ms)')
axes = plt.gca()
#axes.set_ylim([0.34,0.38])
 	
plt.plot(filterDataTime,filterDataYaxis,'b-',label="filterData");
plt.legend();
plt.show()
