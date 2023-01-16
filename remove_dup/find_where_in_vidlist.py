import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop\remove_dup"
os.chdir(source_dir)
fileopen = open("AtsBr_Rear_127_without_dot_vid.txt","r")
son=fileopen.readlines()
#print(son)
sonLength=len(son)

fileopen2 = open("vidlist_without_xlm_dot_text.txt","r")
mom=fileopen2.readlines()
#print(mom)
momLength=len(mom)

daughter=[]
counter=0
#new.append(old[0])
for i in range(sonLength):
    #print(old[i])
    basename = os.path.basename(son[i])
    #print(basename)
    inside=0
    for j in range(momLength):
        #print("here")
        if basename in mom[j]:
            print("basename is : "+basename)
            print("mom is : "+mom[j])
            inside=1
            daughter.append(mom[j])

#print(new)
#print (counter)
fileopen.close()
fileopen2.close()

outputfile=open("Ambulance.txt","w")
for i in range(len(daughter)):
    outputfile.write(daughter[i])
outputfile.close()

