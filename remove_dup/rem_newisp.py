import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\YAN\batch\DLD"
os.chdir(source_dir)
fileopen = open("find.txt","r")
old=fileopen.readlines()
oldLength=len(old)

new=[]
counter=0
for i in range(oldLength):   
    if "NEWISP" in old[i]:
        counter=counter+1
    elif "DLD4Sailauf" in old[i]:
        counter=counter+1
    elif "FE_MP" in old[i]:
        counter=counter+1
    else:
        new.append(old[i])
fileopen.close()
#print(counter)

outputfile=open("Half.txt","w")
for i in range(len(new)):
    outputfile.write(new[i])
outputfile.close()