import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop\remove_dup"
os.chdir(source_dir)
fileopen = open("myfile.txt","r")
old=fileopen.readlines()
oldLength=len(old)

'''
new=[]
counter=0
for i in range(oldLength):
    if old[i] in new:
        #print("it is duplicated")
        counter=counter+1
    elif old[i]+'\n' in new:
        #print("it is duplicated")
        counter=counter+1
    else:
        new.append(old[i])
        #print(new)

#print (len(new))
#print (len(old))
fileopen.close()

outputfile=open("output.txt","w")
for i in range(len(new)):
    outputfile.write(new[i])
outputfile.close()
'''