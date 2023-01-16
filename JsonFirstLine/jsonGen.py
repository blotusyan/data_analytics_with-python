import math
import csv
import os
import shutil
import os.path
import subprocess
import win32com.client
import win32com
import sys
import json

#while True:
source_dir=os.path.dirname(__file__)
os.chdir(source_dir)
name=[]
length=[]
vid=[]
for (dirpath, dirnames, filenames) in os.walk(source_dir):
        #OPEN FOLDER
        for filename in filenames: 
            #1          
            #print(filename)
            
            if ('.json' in filename):
                name.append(filename)
                os.chdir(source_dir)
                #OPEN FILE
                fileopen1 = open(filename,"r")
                lines=fileopen1.readlines()
                #print(mom)
                #2
                linesLength=len(lines)
                print(linesLength)
                length.append(linesLength)
                #with open(filename) as json_file :
                    #student_loaded = json.loads(json_file.read())            
                #path2=student_loaded(['source-ref'])
                a=lines[0]
                y = json.loads(a)
                #print(y)
                path2=y['source-ref']
                basename=os.path.basename(path2)
                #3
                vidname=basename[:-3]+'vid'
                vid.append(vidname)
                #print(vidname)
with open('JSON_REPORT'+'.csv', 'w' , encoding='UTF8', newline='') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    header=['JsonName','length','vidName']
                    writer.writerow(header)
                    for i in range(len(name)):
                        line=[name[i],length[i],vid[i]]
                        writer.writerow(line)
