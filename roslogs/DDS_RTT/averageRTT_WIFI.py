#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, os.path
import csv
from operator import add

A = os.listdir('.');

lenA = len(A);

i = 0;
mqttFiles = [];
ddsFiles = [];
while i < lenA:
  if(A[i].startswith("ping_mqtt")):
    mqttFiles.append(A[i]);
  elif(A[i].startswith("ping_dds")):
    ddsFiles.append(A[i]);
  i+=1;


print "Processing ",
print len(mqttFiles),
print " MQTT files and ",
print len(ddsFiles),
print " DDS Files"

if(len(mqttFiles) != len(ddsFiles)):
  print "mismatching no. of ddsFiles and mqttFiles.. please check current working directory.."
  exit();

i = 0;

#totalNavAvg = [0 for x in range(500)]
#totalVidAvg = [0 for x in range(500)]
dds05 = []
mqtt05 = []
dds_wifi05 = []
mqtt_wifi05 = []

dds20 = []
mqtt20 = []
dds_wifi20 = []
mqtt_wifi20 = []


packetsRange = range(1,501);
 
#For 0.5 Kb - Show DDS & MQTT == DDS+WIFI & MQTT+WIFI 
#  X-axis Packet number (0.5Kb)
#  Y-axis Average RTT(Round-trip-time) delay (ms)

#For 20 Kb - Show DDS & MQTT & DDS+WIFI & DDS+WIFI
#  X-axis Packet number (dds0520Kb)
#  Y-axis RTT(Round-trip-time) dedds05lay (ms)

fileCount = 0;
  
while i < len(mqttFiles): 
  mqttFile = open(mqttFiles[i], 'rt');
  mqttReader = csv.reader(mqttFile, delimiter=" ");
  currentExpMqtt05Arr = []
  currentExpMqttWiFi05Arr = []
  currentExpMqtt20Arr = []
  currentExpMqttWiFi20Arr = []
  
  rowCount = 0;   
  for row in mqttReader:
   currentExpMqtt05Arr.append(row[0]);
   currentExpMqttWiFi05Arr.append(row[1]);
   currentExpMqtt20Arr.append(row[2]);
   currentExpMqttWiFi20Arr.append(row[3]);
   rowCount+=1;
   if(rowCount >= 500):
    break;
    
  mqtt05.append(currentExpMqtt05Arr);
  mqtt_wifi05.append(currentExpMqttWiFi05Arr);

  mqtt20.append(currentExpMqtt20Arr);
  mqtt_wifi20.append(currentExpMqttWiFi20Arr);

  fileCount+=1;
  if(fileCount >= len(mqttFiles)):
   break;
  i+=1;

plt.figure(1);
#plt.subplot(211)e
plt.ylabel('RTT Delay(ms)')
plt.xlabel('Packet number - sent every second (~10min)')
axes = plt.gca()

for yplot in mqtt05: 
 plt.plot(packetsRange,yplot,color='blue',label="RTT for 0.5Kb MQTT packet.");
for yplot in mqtt_wifi05: 
 plt.plot(packetsRange,yplot,color='cyan',label="RTT for 0.5Kb MQTT & WIFI packet.");

plt.legend();
plt.show()    

fileCount = 0;
i = 0;

while i < len(ddsFiles): 
  ddsFile = open(ddsFiles[i], 'rt');
  ddsReader = csv.reader(ddsFile, delimiter=" ");
  currentExpDds05Arr = []
  currentExpDdsWiFi05Arr = []
  currentExpDds20Arr = []
  currentExpDdsWiFi20Arr = []
  
  rowCount = 0;   
  for row in ddsReader:
   currentExpDds05Arr.append(row[0]);
   currentExpDdsWiFi05Arr.append(row[1]);
   currentExpDds20Arr.append(row[2]);
   currentExpDdsWiFi20Arr.append(row[3]);
   rowCount+=1;
   if(rowCount >= 500):
    break;
  print('XXX');
  dds05.append(currentExpDds05Arr);
  dds_wifi05.append(currentExpDdsWiFi05Arr);

  dds20.append(currentExpDds20Arr);
  dds_wifi20.append(currentExpDdsWiFi20Arr);

  fileCount+=1;
  if(fileCount >= len(ddsFiles)):
   break;
  i+=1;

plt.figure(1); 
plt.ylabel('RTT Delay(ms)')
plt.xlabel('Packet number - sent every second (~10min)')
axes = plt.gca()

print (len(dds05));
print (len(dds_wifi05));

for yplot in dds05: 
 plt.plot(packetsRange,yplot,color='lightpink',label="RTT for 0.5Kb DDS packet.");
for yplot in dds_wifi05: 
 plt.plot(packetsRange,yplot,color='maroon',label="RTT for 0.5Kb DDS & WIFI packet.");


plt.legend();
plt.show() 
