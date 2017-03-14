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
   filterDataTime.append(int(row[0]));
   filterDataYaxis.append(row[17]);
   #print(row[0]);
   filterCount+=1;
   if(filterCount >= 10000):
     break;
filterFile.close();

imuFile = open("logPTAM.txt", 'rt');
#kfFile = open("logFilter.txt", 'rt');
#kfData = [];
imuData = [];
imuDataVel = [];

#Reading the IMU and KF files
imuReader = csv.reader(imuFile, delimiter=" ");
#kfReader = csv.reader(kfFile, delimiter=" ");
 
imuCount = 0;
#kfCount = 0;

#Extracting first 1899 for nav and 1800 for vid
for row in imuReader: 
   roundedtime = str(row[1])[:5];
   #imuData.append(int(roundedtime));
   imuData.append(int(row[1]));
   #imuData.append(row[1]);
   imuDataVel.append(row[2]);
   #print(row[0]);
   imuCount+=1;
   if(imuCount >= 5000):
     break;
#for row in kfReader:
   #if (row[14] != -1):
   #kfData.append(row[14]);
#   kfData.append(row[14]);
   #print(row[5]);
#   kfCount+=1;
#   if(kfCount >= 800):
#     break;
imuFile.close();
#kfFIle.close();


idx = 0;

plt.figure(1);
#plt.subplot(211)
plt.ylabel('Predicted x(metric)')
plt.xlabel('Time (ms)')
axes = plt.gca()
#axes.set_ylim([0.34,0.38])
 	
filterDataTime = [( x - filterDataTime[0]) for x in filterDataTime];
imuData = [(x - imuData[0]) for x in imuData];
    
plt.plot(filterDataTime,filterDataYaxis,'b-',label="filterData");
plt.plot(imuData,imuDataVel,'r',label="imuData");
plt.legend();

plt.show()
