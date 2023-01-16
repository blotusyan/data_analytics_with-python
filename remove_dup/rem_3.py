import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop\remove_dup"
os.chdir(source_dir)
fileopen = open("output.txt","r")
old=fileopen.readlines()
oldLength=len(old)

new=[]
counter=0
for i in range(oldLength):
    basename = os.path.basename(old[i])
    if "rear" in basename:
        counter=counter+1
    elif "left" in basename:
        counter=counter+1
    elif "right" in basename:
        counter=counter+1
    else:
        new.append(old[i])
fileopen.close()
print(counter)

outputfile=open("vidlist.txt","w")
for i in range(len(new)):
    outputfile.write(new[i])
outputfile.close()