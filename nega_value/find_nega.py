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
            print(filename)
            if ('AWS' in filename):
                os.chdir(source_dir)
                #OPEN FILE
                LIST=[]
                with open(filename) as file1:
                    data= [r for r in file1]
                    for i in range(len(data)):
                        #print(data[i])
                        Line=data[i].split(',')
                        #LIST is 2D: m*m
                        #print(Line)
                        LIST.append(Line)
                    print(len(LIST))
                    isinside=0
                    vidindex=[]
                    for i in range(1,len(LIST)):
                        thisline=0
                        for j in range(math.floor(len(LIST[i])/8)):
                            if int(LIST[i][7+8*j])<0:
                                thisline=thisline+1
                                isinside=isinside+1
                        if thisline:
                            vidindex.append(LIST[i][0])
                    if isinside:
                        name.append(filename)
                        index.append(vidindex)
        print(name)
        print(index)


