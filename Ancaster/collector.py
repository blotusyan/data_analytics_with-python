import csv
import os
import math
import shutil
import os.path


def Collect():
    output_dir = r"C:\YAN\M"
    source_dir = r"C:\YAN\M"
    outlist =['Vidlist-Name','# of Frames', 'Total detection FP','Object ID',"FP start","FP end","Sub total",'Object ID',"FP start","FP end","Sub total"]
    for (dirpath, dirnames, filenames) in os.walk(source_dir):
        for filename in filenames:
            if ('PD' in filename):
                os.chdir(source_dir)
                with open(filename) as file1:
                    r1 = csv.reader(file1)
                    print("open")
                    next(r1)
                    frameNumList1=[]
                    frameNumList2=[]
                    #1
                    vidname=filename
                    print(vidname)
                    #2
                    data= [r for r in file1]
                    totalnumFrame=data[-1][0:3]
                    print(totalnumFrame)
                    print("1")
                    for i in range(int(totalnumFrame)):
                        newlist=data[i].split(',')
                        #print(newlist)
                        if (newlist[1]=="1"):
                           frameNumList1.append(int(newlist[0]))
                           print(newlist[0])
                        if (newlist[1]=="2"):
                           frameNumList2.append(int(newlist[0]))
                    print(frameNumList1)
                    #5                
                    FPStart1=min(frameNumList1)
                    #6
                    FPEnd1=max(frameNumList1)
                    #7
                    FPSub1=FPEnd1-FPStart1+1
                    print(len(frameNumList2)
                    '''
                    if not frameNumList2:
                          
                          FPStart2=frameNumList2[0]
                          FPEnd2=frameNumList2[-1]
                          FPSub2=FPEnd2-FPStart2+1
                    else:
                    FPSub2==0
                    TotalDetection=FPSub1+FPSub2
                    print(FPStart1)
                    '''

Collect()
