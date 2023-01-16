import math
import csv
import os
import shutil
import os.path
import subprocess
import win32com.client
import win32com
import sys

#while True:
source_dir=os.path.dirname(__file__)
os.chdir(source_dir)
name=[]
index=[]
for (dirpath, dirnames, filenames) in os.walk(source_dir):
        #OPEN FOLDER
        for filename in filenames:           
            #print(filename)
            if ('.csv' in filename):
                os.chdir(source_dir)
                #OPEN FILE
                LIST=[]
                col=[]
                with open(filename) as file1:
                    data= [r for r in file1]
                    for i in range(len(data)):
                        #print(data[i])
                        Line=data[i].split(',')
                        #LIST is 2D: m*m
                        #print(Line)
                        LIST.append(Line)
                    #print(LIST[1])

                    if int(LIST[0][1][-2])==0:
                        col.append(int(LIST[0][1][:-2])-9)
                        print(LIST[0][1])
                        print(LIST[0][1][-2])
                        print(LIST[0][1][:-1])
                        print(int(LIST[0][1][:-1])-9)
                        #print("it is one:"+str(int(LIST[i][1][-3])), str(int(LIST[i][1][:-2])-9))
                    if int(LIST[0][1][-2])>0:
                        col.append(int(LIST[0][1][:-2])-int(LIST[0][1][-3])+1)
                        print(LIST[0][1])
                        print(LIST[0][1][-2])
                        print(LIST[0][1][:-1])
                        print(int(LIST[0][1][:-1])-int(LIST[0][1][-2])+1)