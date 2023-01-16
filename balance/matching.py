import math
import csv
import os
import shutil
import os.path

source_dir=r"C:\YAN\balance"
os.chdir(source_dir)
fileopen = open("gt_akbar.txt","r")
small=fileopen.readlines()
#print(son)
#xmlLength=len(xml)

fileopen2 = open("gtbiglist.txt","r")
big=fileopen2.readlines()
#print(mom)
#aviLength=len(avi)

daughter=[]
counter=0
#new.append(old[0])
for i in range(len(small)):
    #print(old[i])
    #basenameXML = os.path.basename(xml[i]).strip()
    #print(basenameXML)
    #basenameAVI = os.path.basename(avi[i]).strip()
    smallName=small[i].strip()
    #print(basenameAVI)
    for j in range(len(big)):
        if smallName.lower() in big[j].lower():
            #print("yes "+str(i))
            daughter.append(big[j])
            break
        #else:
            #print("no "+str(i))
            #break
        


print(len(daughter))
#print(new)
#print (counter)
fileopen.close()
fileopen2.close()

outputfile=open("MATCH.txt","w")
for i in range(len(daughter)):
    outputfile.write(str(daughter[i]))
outputfile.close()

