import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop\remove_dup\xml_csv"
os.chdir(source_dir)
fileopen = open("1over8.txt","r")
old=fileopen.readlines()
oldLength=len(old)

new=[]
counter=0
new.append(old[0])
for i in range(oldLength):
    #print(old[i])
    inside=0
    for j in range(len(new)):
        if old[i] in new[j]:
            print(old[i])
            print(new[j])
            print("it is duplicated")
            inside=1
    if not inside:
        new.append(old[i])

#print(new)
#print (counter)
fileopen.close()

outputfile=open("checkUnique.txt","w")
for i in range(len(new)):
    outputfile.write(new[i])
outputfile.close()

