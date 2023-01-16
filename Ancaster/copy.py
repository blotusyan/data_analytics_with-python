import csv
import os
import math
import shutil
import os.path
import xlwings as xw


def Collect():
    #dir to be changed
    output_dir = r"T:\YAN\From_Moh\20200828\CropMP_CClassBr_20200825_5cc7d2_2Cam_PDIntg HighTP\REPORT"
    source_dir = r"T:\YAN\From_Moh\20200828\CropMP_CClassBr_20200825_5cc7d2_2Cam_PDIntg HighTP\Rear Detection CSVs"
    #outlist =['Vidlist-Name','# of Frames', 'Total detection FP','Object ID',"FP start","FP end","Sub total",'Object ID',"FP start","FP end","Sub total"]
    
    for (dirpath, dirnames, filenames) in os.walk(source_dir):
        #OPEN FOLDER
        #print(filenames)
        j=2
        for filename in filenames:
            
            print(filename)
            if ('PD' in filename):
                os.chdir(source_dir)
                #OPEN FILE
                with open(filename) as file1:
                    r1 = csv.reader(file1)
                    #print("open")
                    next(r1)
                    frameNumList=[[] for m in range(21)]
                    FPStart=['']*21
                    FPEnd=['']*21
                    FPSub=['']*21
                    ObjectID=['']*21
                    #frameNumList1=[]
                    #frameNumList2=[]
                    #111111111111111111111111111111111111111111111111111111111
                    vidname=filename
                    #print(vidname)
                    
                    #OPEN LINE
                    data= [r for r in file1]
                    #222222222222222222222222222222222222222222222222222222222
                    lastLine=data[-1].split(',')
                    totalnumFrame=lastLine[0]
                    #print(totalnumFrame)
                    #print("1")
                    #append to framenumList
                    for i in range(int(totalnumFrame)):
                        
                        newlist=data[i].split(',')
                        if len(newlist)==1:
                            flag=0
                            
                        elif len(newlist)==16:
                           frameNumList[0].append(int(newlist[0]))
                           #print(newlist[0])
                           #(newlist[16]=="1")
                        
                        else:
                            for k in range(0,math.floor(len(newlist)/15),1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))


                        #THE REST OF ELIF CAN BE SUMMED TO ELSE NO WE CANNOT 
                        #BUT WE CAN SAY for k in range(0,len(newlist)/15,1)
                        #TO MAKE 9 ELIF INTO ONE ELSE
                        '''
                        elif len(newlist)==31:
                            #OBJ1
                            for k in range(0,2,1):
                                #print("NEWLIST IS: " + str(newlist[1+15*k]))
                                #print ("K IS: " + str(k))
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                                #else:
                                    #print("NOT APPENDED")
                                    
                        
                        elif len(newlist)==46:
                            #OBJ2
                            for k in range(0,3,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==61:
                            #OBJ3
                            for k in range(0,4,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==76:
                            #OBJ4
                            for k in range(0,5,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==91:
                            #OBJ5
                            for k in range(0,6,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==106:
                            #ONJ6
                            for k in range(0,7,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==121:
                            #OBJ7
                            for k in range(0,8,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==136:
                            #OBJ8
                            for k in range(0,9,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        elif len(newlist)==151:
                            #OBJ9
                            for k in range(0,10,1):
                                if str(newlist[1+15*k])==str(k):
                                    frameNumList[k].append(int(newlist[0]))
                        '''
                #print("length is "+ "" + str(len(frameNumList)))
                #print(frameNumList)
                #这段if可以不用 因为不会进入 只用else就可以
                if len(frameNumList)==0:
                    
                    for w in range(10):
                        
                        FPStart[w]=""
                        FPEnd[w]=""
                        FPSub[w]=""
                        ObjectID[w]=""
                        TotalDetection=""
                else:
                    TotalDetection=0
                    for w in range(21):
                        if len(frameNumList[w])==0:
                            FPStart[w]=""
                            FPEnd[w]=""
                            FPSub[w]=""
                            ObjectID[w]=""
                        else:
                            FPSub[w]=len(frameNumList[w])
                            FPStart[w]=frameNumList[w][0]
                            FPEnd[w]=frameNumList[w][-1]
                            ObjectID[w]=w
                            #print("OBJ ID IS: " + str(ObjectID[p]))
                            TotalDetection=TotalDetection+FPSub[w]
                             


                        
            os.chdir(output_dir)    
            wb=xw.Book('tem.xlsx')
            sh=wb.sheets['Sheet1']
            sh.range('A'+str(j)).value=vidname
            sh.range('B'+str(j)).value=totalnumFrame
            sh.range('C'+str(j)).value=TotalDetection
            sh.range('D'+str(j)).value=ObjectID[0]
            sh.range('E'+str(j)).value=FPStart[0]
            sh.range('F'+str(j)).value=FPEnd[0]
            sh.range('G'+str(j)).value=FPSub[0]
            sh.range('H'+str(j)).value=ObjectID[1]
            sh.range('I'+str(j)).value=FPStart[1]
            sh.range('J'+str(j)).value=FPEnd[1]
            sh.range('K'+str(j)).value=FPSub[1]
            sh.range('L'+str(j)).value=ObjectID[2]
            sh.range('M'+str(j)).value=FPStart[2]
            sh.range('N'+str(j)).value=FPEnd[2]
            sh.range('O'+str(j)).value=FPSub[2]
            sh.range('P'+str(j)).value=ObjectID[3]
            sh.range('Q'+str(j)).value=FPStart[3]
            sh.range('R'+str(j)).value=FPEnd[3]
            sh.range('S'+str(j)).value=FPSub[3]
            sh.range('T'+str(j)).value=ObjectID[4]
            sh.range('U'+str(j)).value=FPStart[4]
            sh.range('V'+str(j)).value=FPEnd[4]
            sh.range('W'+str(j)).value=FPSub[4]
            sh.range('X'+str(j)).value=ObjectID[5]
            sh.range('Y'+str(j)).value=FPStart[5]
            sh.range('Z'+str(j)).value=FPEnd[5]
            sh.range('AA'+str(j)).value=FPSub[5]
            sh.range('AB'+str(j)).value=ObjectID[6]
            sh.range('AC'+str(j)).value=FPStart[6]
            sh.range('AD'+str(j)).value=FPEnd[6]
            sh.range('AE'+str(j)).value=FPSub[6]
            sh.range('AF'+str(j)).value=ObjectID[7]
            sh.range('AG'+str(j)).value=FPStart[7]
            sh.range('AH'+str(j)).value=FPEnd[7]
            sh.range('AI'+str(j)).value=FPSub[7]
            sh.range('AJ'+str(j)).value=ObjectID[8]
            sh.range('AK'+str(j)).value=FPStart[8]
            sh.range('AL'+str(j)).value=FPEnd[8]
            sh.range('AM'+str(j)).value=FPSub[8]
            sh.range('AN'+str(j)).value=ObjectID[9]
            sh.range('AO'+str(j)).value=FPStart[9]
            sh.range('AP'+str(j)).value=FPEnd[9]
            sh.range('AQ'+str(j)).value=FPSub[9]
            sh.range('AR'+str(j)).value=ObjectID[10]
            sh.range('AS'+str(j)).value=FPStart[10]
            sh.range('AT'+str(j)).value=FPEnd[10]
            sh.range('AU'+str(j)).value=FPSub[10]
            sh.range('AV'+str(j)).value=ObjectID[11]
            sh.range('AW'+str(j)).value=FPStart[11]
            sh.range('AX'+str(j)).value=FPEnd[11]
            sh.range('AY'+str(j)).value=FPSub[11]
            sh.range('AZ'+str(j)).value=ObjectID[12]
            sh.range('BA'+str(j)).value=FPStart[12]
            sh.range('BB'+str(j)).value=FPEnd[12]
            sh.range('BC'+str(j)).value=FPSub[12]
            sh.range('BD'+str(j)).value=ObjectID[13]
            sh.range('BE'+str(j)).value=FPStart[13]
            sh.range('BF'+str(j)).value=FPEnd[13]
            sh.range('BG'+str(j)).value=FPSub[13]
            sh.range('BH'+str(j)).value=ObjectID[14]
            sh.range('BI'+str(j)).value=FPStart[14]
            sh.range('BJ'+str(j)).value=FPEnd[14]
            sh.range('BK'+str(j)).value=FPSub[14]
            sh.range('BL'+str(j)).value=ObjectID[15]
            sh.range('BM'+str(j)).value=FPStart[15]
            sh.range('BN'+str(j)).value=FPEnd[15]
            sh.range('BO'+str(j)).value=FPSub[15]
            sh.range('BP'+str(j)).value=ObjectID[16]
            sh.range('BQ'+str(j)).value=FPStart[16]
            sh.range('BR'+str(j)).value=FPEnd[16]
            sh.range('BS'+str(j)).value=FPSub[16]
            sh.range('BT'+str(j)).value=ObjectID[17]
            sh.range('BU'+str(j)).value=FPStart[17]
            sh.range('BV'+str(j)).value=FPEnd[17]
            sh.range('BW'+str(j)).value=FPSub[17]
            sh.range('BX'+str(j)).value=ObjectID[18]
            sh.range('BY'+str(j)).value=FPStart[18]
            sh.range('BZ'+str(j)).value=FPEnd[18]
            sh.range('CA'+str(j)).value=FPSub[18]
            sh.range('CB'+str(j)).value=ObjectID[19]
            sh.range('CC'+str(j)).value=FPStart[19]
            sh.range('CD'+str(j)).value=FPEnd[19]
            sh.range('CE'+str(j)).value=FPSub[19]
            sh.range('CF'+str(j)).value=ObjectID[20]
            sh.range('CG'+str(j)).value=FPStart[20]
            sh.range('CH'+str(j)).value=FPEnd[20]
            sh.range('CI'+str(j)).value=FPSub[20]
            j=j+1
            #print(j)
        break
                
                
Collect()
        
'''
                    if len(frameNumList)==2:
                                        FPStart9=""
                                        FPEnd9=""
                                        FPSub9=""
                                        ObjectID9=""
                            FPStart8=""
                            FPEnd8=""
                            FPSub8=""
                            ObjectID8=""
                        FPStart7=""
                        FPEnd7=""
                        FPSub7=""
                        ObjectID7=""
                        FPStart6=""
                        FPEnd6=""
                        FPSub6=""
                        ObjectID6=""
                        FPStart5=""
                        FPEnd5=""
                        FPSub5=""
                        ObjectID5=""
                        FPStart4=""
                        FPEnd4=""
                        FPSub4=""
                        ObjectID4=""
                        FPStart3=""
                        FPEnd3=""
                        FPSub3=""
                        ObjectID3=""
                        FPStart2=""
                        FPEnd2=""
                        FPSub2=""
                        ObjectID2=""
                        FPSub1=""
                        FPStart1=""
                        FPEnd1=""
                        ObjectID1=""
                        FPSub0=len(frameNumList[0])
                        FPStart0=frameNumList[0][0]
                        FPEnd0=frameNumList[0][-1]
                        ObjectID0=0
                        TotalDectection=FPSub0
                    
                                  
                   
                    if len(frameNumList1)!=0 and len(frameNumList0)!=0 and len(frameNumList2)!=0:
                        
                        FPStart2=frameNumList2[0]
                        FPEnd2=frameNumList2[-1]
                        FPSub2=len(frameNumList2)
                        ObjectID2=2
                        FPStart1=frameNumList1[0]
                        FPEnd1=frameNumList1[-1]
                        FPSub1=len(frameNumList1)
                        ObjectID1=1
                        FPStart0=frameNumList0[0]
                        FPEnd0=frameNumList0[-1]
                        FPSub0=len(frameNumList0)
                        ObjectID0=0
                        TotalDetection=FPSub1+FPSub0+FPSub2
                        
                    elif len(frameNumList1)!=0 and len(frameNumList0)!=0 and len(frameNumList2)==0:
                        FPStart1=frameNumList1[0]
                        FPEnd1=frameNumList1[-1]
                        FPSub1=len(frameNumList1)
                        ObjectID1=1
                        FPStart0=frameNumList0[0]
                        FPEnd0=frameNumList0[-1]
                        FPSub0=len(frameNumList0)
                        ObjectID0=0
                        FPSub2=""
                        FPStart2=""
                        FPEnd2=""
                        ObjectID2=""
                        TotalDectection=FPSub1+FPSub0
                        
                    elif len(frameNumList1)!=0 and len(frameNumList0)==0 and len(frameNumList2)!=0:
                        FPStart1=frameNumList1[0]
                        FPEnd1=frameNumList1[-1]
                        FPSub1=len(frameNumList1)
                        ObjectID1=1
                        FPStart2=frameNumList2[0]
                        FPEnd2=frameNumList2[-1]
                        FPSub2=len(frameNumList2)
                        ObjectID2=2
                        FPSub0=""
                        FPStart0=""
                        FPEnd0=""
                        ObjectID0=""
                        TotalDetection=FPSub1+FPSub2
                        
                    elif len(frameNumList1)!=0 and len(frameNumList0)==0 and len(frameNumList2)==0:
                        FPStart1=frameNumList1[0]
                        FPEnd1=frameNumList1[-1]
                        FPSub1=len(frameNumList1)
                        ObjectID1=1
                        FPStart2=""
                        FPEnd2=""
                        FPSub2=""
                        ObjectID2=""
                        FPSub0=""
                        FPStart0=""
                        FPEnd0=""
                        ObjectID0=""
                        TotalDetection=FPSub1

                    elif len(frameNumList1)==0 and len(frameNumList0)!=0 and len(frameNumList2)!=0:
                        FPSub1=""
                        FPStart1=""
                        FPEnd1=""
                        ObjectID1=""
                        FPStart2=frameNumList2[0]
                        FPEnd2=frameNumList2[-1]
                        FPSub2=len(frameNumList2)
                        ObjectID2=2
                        FPStart0=frameNumList0[0]
                        FPEnd0=frameNumList0[-1]
                        FPSub0=len(frameNumList0)
                        ObjectID0=0
                        TotalDetection=FPSub0+FPSub2

                    elif len(frameNumList1)==0 and len(frameNumList0)!=0 and len(frameNumList2)==0:
                        FPSub1=""
                        FPStart1=""
                        FPEnd1=""
                        ObjectID1=""
                        FPStart2=""
                        FPEnd2=""
                        FPSub2=""
                        ObjectID2=""
                        FPStart0=frameNumList0[0]
                        FPEnd0=frameNumList0[-1]
                        FPSub0=len(frameNumList0)
                        ObjectID0=0
                        TotalDetection=FPSub0

                    elif len(frameNumList1)==0 and len(frameNumList0)==0 and len(frameNumList2)!=0:
                        FPSub1=""
                        FPStart1=""
                        FPEnd1=""
                        ObjectID1=""
                        FPStart2=frameNumList2[0]
                        FPEnd2=frameNumList2[-1]
                        FPSub2=len(frameNumList2)
                        ObjectID2=2
                        FPSub0=""
                        FPStart0=""
                        FPEnd0=""
                        ObjectID0=""
                        TotalDetection=FPSub2
                    else:
                        FPSub1=""
                        FPStart1=""
                        FPEnd1=""
                        ObjectID1=""
                        FPSub0=""
                        FPStart0=""
                        FPEnd0=""
                        ObjectID0=""
                        FPStart2=""
                        FPEnd2=""
                        FPSub2=""
                        ObjectID2=""
                        TotalDectection=""
'''
'''
                        elif len(newlist)==31 and newlist[1]=="":
                            flag=2
                            #(newlist[1]=="0")
                            frameNumList1.append(int(newlist[0]))
                        elif len(newlist)==31 and newlist[1]=="0":
                            flag=2
                            #(newlist[1]=="0")
                            frameNumList1.append(int(newlist[0]))
                            frameNumList0.append(int(newlist[0]))
                        elif len(newlist)==46 and newlist[1]=="0" and newlist[16]=="1":
                            frameNumList0.append(int(newlist[0]))
                            frameNumList1.append(int(newlist[0]))
                            frameNumList2.append(int(newlist[0]))
                        elif len(newlist)==46 and newlist[1]=="0" and newlist[16]!="1":
                            frameNumList0.append(int(newlist[0]))
                            #frameNumList1.append(int(newlist[0]))
                            frameNumList2.append(int(newlist[0]))
                        elif len(newlist)==46 and newlist[1]!="0" and newlist[16]=="1":
                            #frameNumList0.append(int(newlist[0]))
                            frameNumList1.append(int(newlist[0]))
                            frameNumList2.append(int(newlist[0]))
                        elif len(newlist)==46 and newlist[1]!="0" and newlist[16]!="1":
                            #frameNumList0.append(int(newlist[0]))
                            #frameNumList1.append(int(newlist[0]))
                            frameNumList2.append(int(newlist[0]))
'''
'''
                #这部分是阴差阳错对的 if永远不会进入因为长度永远是10， 一开始赋值totaldetection让空file数就是0， else的forloop会一直跑10次
                if len(frameNumList)==0:
                    
                    for w in range(10):
                        
                        FPStart[w]=""
                        FPEnd[w]=""
                        FPSub[w]=""
                        ObjectID[w]=""
                        TotalDetection=""
                else:
                    
                    TotalDetection=0
                    for p in range(len(frameNumList)):
                        #print (p)
                        if len(frameNumList[p])==0:
                            FPSub[p]=""
                            FPStart[p]=""
                            FPEnd[p]=""
                            ObjectID[p]="" 
                            #print("FPSUB IS: " +str(FPSub[p]))
                        #print(TotalDetection)
                        else:
                            FPSub[p]=len(frameNumList[p])
                            FPStart[p]=frameNumList[p][0]
                            FPEnd[p]=frameNumList[p][-1]
                            ObjectID[p]=p
                            #print("OBJ ID IS: " + str(ObjectID[p]))
                            TotalDetection=TotalDetection+FPSub[p]
                    for z in range(len(frameNumList),10):
                        FPSub[z]=""
                        FPStart[z]=""
                        FPEnd[z]=""
                        ObjectID[z]=""
'''                        

                    
