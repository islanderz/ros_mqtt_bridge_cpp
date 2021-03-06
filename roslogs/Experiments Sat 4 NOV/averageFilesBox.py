#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, os.path
import csv
from operator import add

vidFiles = [];

D = [x[0] for x in os.walk('.')]
dirs = [];
k = 0;
while k < len(D):
  if (D[k] == './DDS_1_LATENCIES/100' ):
     dirs.append(D[k]);
     A = os.listdir(D[k]);    
     vidFiles.append(A[0]);
  k+=1;

k = 0;
while k < len(D):
  if (D[k] == './DDS_2_LATENCIES/100' ):
     dirs.append(D[k]);
     A = os.listdir(D[k]);   
     vidFiles.append(A[0]);
  k+=1;

k = 0;
while k < len(D):
  if (D[k] == './DDS_3_LATS/100' ):
     dirs.append(D[k]);
     A = os.listdir(D[k]);    
     vidFiles.append(A[0]);
  k+=1;

k = 0;
while k < len(D):
  if (D[k] == './ROSTCP_1_LATS/100' ):
     dirs.append(D[k]);
     A = os.listdir(D[k]);    
     vidFiles.append(A[0]);
  k+=1;

k = 0;
while k < len(D):
  if (D[k] == './ROSTCP_2_LATENCIES/100' ):
     dirs.append(D[k]);
     A = os.listdir(D[k]);    
     vidFiles.append(A[0]);
  k+=1;

k = 0;
while k < len(D):
  if (D[k] == './ROSTCP_3_LATS/100' ):
     dirs.append(D[k]);
     A = os.listdir(D[k]);    
     vidFiles.append(A[0]);
  k+=1;

fig, ax1 = plt.subplots(figsize=(10, 6))
fig.canvas.set_window_title('A Boxplot Example')
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)


print " Navdata files and ",
print len(vidFiles),
print " Video Files"
fig, ax1 = plt.subplots(figsize=(10, 6))
fig.canvas.set_window_title('A Boxplot Example')
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

i = 0;

totalVidAvg = [0 for x in range(60)]
 
AllVidAvg = np.zeros((60,1));

i = 0;
maxVidDelay = [0 for x in range(60)]
minVidDelay = [100000 for x in range(60)]

while i < len(dirs):
  vidLines = [line.rstrip('\n') for line in open(dirs[i]+'/'+vidFiles[i])];

  vidDelays = np.zeros((60,1));

  lineCount = 0;
  while lineCount < 60:
    vidDelays[lineCount] = float(vidLines[lineCount]);

    totalVidAvg[lineCount] += (float)(vidLines[lineCount]);

    if(maxVidDelay[lineCount] < float(vidLines[lineCount])):
        maxVidDelay[lineCount] = float(vidLines[lineCount]);
    if(minVidDelay[lineCount] > float(vidLines[lineCount])):
        minVidDelay[lineCount] = float(vidLines[lineCount]);
    lineCount = lineCount + 1;
  i+=1; 
  vidDelays = np.vstack(vidDelays); 
  AllVidAvg = np.hstack((AllVidAvg, np.asarray(vidDelays)));

AllVidAvg = AllVidAvg[:,1:];

plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['DDS - 1 MAV', 'DDS - 2 MAVs', 'DDS - 3 MAVs', 'ROSTCP - 1 MAV', 'ROSTCP - 2 MAVs','ROSTCP - 3 MAVs', 'MQTT - 1 MAV','MQTT - 2 MAVs'])


# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
#ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Video frame message latencies (100Mbps LAN)')
ax1.set_xlabel('Protcol and Number of MAVs')
ax1.set_ylabel('Latency (sec)')

# Set the axes ranges and axes labels
# top = 40
# bottom = -5
# ax1.set_ylim(bottom, top)
#xtickNames = plt.setp(ax1, xticklabels=np.repeat(AllNavAvg, 2))
#plt.setp(xtickNames, rotation=45, fontsize=8)

plt.boxplot(AllVidAvg, notch=False, sym='+', vert=True, whis=1.5, positions=None, widths=None, patch_artist=False, bootstrap=None, usermedians=None, conf_intervals=None);
#plt.boxplot(AllVidAvg);
plt.show()

