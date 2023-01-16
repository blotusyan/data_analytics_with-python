import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop\remove_dup"
os.chdir(source_dir)
fileopen = open("myfile@.txt","r")
old=fileopen.readlines()
oldLength=len(old)

new=[]
counter=0
new.append(old[0])
for i in range(oldLength):
    #print(old[i])
    basename = os.path.basename(old[i])
    inside=0
    for j in range(len(new)):
        if basename in new[j]:
            #print("it is duplicated")
            inside=1
    if not inside:
        new.append(old[i])

#print(new)
#print (counter)
fileopen.close()

outputfile=open("output.txt","w")
for i in range(len(new)):
    outputfile.write(new[i])
outputfile.close()

