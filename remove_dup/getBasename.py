import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\Users\shuayan\Desktop"
os.chdir(source_dir)
fileopen = open("PDonDLD_37.6_100_All_Data_Rear.txt","r")
son=fileopen.readlines()
#print(son)
sonLength=len(son)

daughter=[]
counter=0
#new.append(old[0])
for i in range(sonLength):
    #print(old[i])
    basename = os.path.basename(son[i])
    #print(basename)
    daughter.append(basename)

#print(new)
#print (counter)
fileopen.close()

outputfile=open("376.txt","w")
for i in range(len(daughter)):
    outputfile.write(daughter[i])
outputfile.close()



