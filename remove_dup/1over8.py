import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop\remove_dup"
os.chdir(source_dir)
fileopen = open("FindMom.txt","r")
old=fileopen.readlines()
oldLength=len(old)

new=[]
counter=0
for i in range(oldLength):
    #basename = os.path.basename(old[i])
    if "REAR" in old[i]:
        counter=counter+1
    elif "LEFT" in old[i]:
        counter=counter+1
    elif "RIGHT" in old[i]:
        counter=counter+1
    elif "FRONT" in old[i]:
        counter=counter+1
    elif "Four_Camera" in old[i]:
        counter=counter+1
    elif "FE_MP" in old[i]:
        counter=counter+1
    else:
        new.append(old[i])
fileopen.close()
print(counter)

outputfile=open("1over8.txt","w")
for i in range(len(new)):
    outputfile.write(new[i])
outputfile.close()