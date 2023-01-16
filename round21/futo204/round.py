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
                    for i in range(len(LIST)):
                        if int(LIST[i][1][-2])==0:
                            col.append(int(LIST[i][1][:-1])-9)
                            #print("it is one:"+str(int(LIST[i][1][-3])), str(int(LIST[i][1][:-2])-9))
                        if int(LIST[i][1][-2])>0:
                            col.append(int(LIST[i][1][:-1])-int(LIST[i][1][-2])+1)
                            #print("it is two:"+str(int(LIST[i][1][-3])), str(int(LIST[i][1])-int(LIST[i][1][-3])+1))
                with open(filename[:-4]+'_new.csv', 'w' , encoding='UTF8', newline='') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    # write a row to the csv file
                    for i in range(len(LIST)):
                        line=[LIST[i][0],LIST[i][1],col[i]]
                        writer.writerow(line)
