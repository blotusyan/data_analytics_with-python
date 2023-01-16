import csv
import os
import math
import shutil
import os.path
import xlwings as xw


def Collect():
    #dir to be changed
    output_dir = r"C:\Users\shuayan\Desktop\get127Back\changeAttri_xml"
    source_dir = r"C:\Users\shuayan\Desktop\get127Back"
    #outlist =['Vidlist-Name','# of Frames', 'Total detection FP','Object ID',"FP start","FP end","Sub total",'Object ID',"FP start","FP end","Sub total"]
    
    for (dirpath, dirnames, filenames) in os.walk(source_dir):
        #OPEN FOLDER
        #print(filenames)
        #j=2
        for filename in filenames:
            #clear
            #print(filename)
            os.chdir(source_dir)
            with open(filename) as file1:
                old=file1.readlines()
                oldLength=len(old)
                new=[""]
                #print(oldLength)
                new[0]=old[0].replace('FAIL_SAFE','REAR_FS')
                #print(new[0])
                #print(old[0])
            os.chdir(output_dir)
            newName=filename[:-4]+"_copy.txt"
            outputfile=open(newName,"w")
            outputfile.write(new[0])
            for i in range(1,len(old)):
                outputfile.write(old[i])
            outputfile.close()

Collect()