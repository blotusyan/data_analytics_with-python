import csv
import os
import math
import shutil
import os.path
import subprocess
import argparse

def create(dir):
    #source_dir=os.path.dirname(__file__)
    #os.chdir(source_dir)
    #subprocess.call([source_dir +'\\'+'run.bat'])
    INTG=[]
    AWSP=[]
    PD=[]
    All=[]

    fileopen = open("ClearDay.txt","r")
    ClearDay_content=fileopen.readlines()
    fileopen.close()
    fileopen1 = open("ClearNight.txt","r")
    ClearNight_content=fileopen1.readlines()
    fileopen1.close()
    fileopen2 = open("RainDay.txt","r")
    RainDay_content=fileopen2.readlines()
    fileopen2.close()
    fileopen3 = open("RainNight.txt","r")
    RainNight_content=fileopen3.readlines()
    fileopen3.close()
    fileopen4 = open("SnowDay.txt","r")
    SnowDay_content=fileopen4.readlines()
    fileopen4.close()
    fileopen5 = open("SnowNight.txt","r")
    SnowNight_content=fileopen5.readlines()
    fileopen5.close()

    for i in range(len(ClearDay_content)):
        if ClearDay_content[i]!='\x1a':
            string1='dir /B /S /O:N INTG*'+os.path.basename(ClearDay_content[i])[:-5]+'*.csv >> '+dir+'\\clearDay\\ClearDayINTG.txt\n'
            string2='dir /B /S /O:N AWSP*'+os.path.basename(ClearDay_content[i])[:-5]+'*.csv >> '+dir+'\\clearDay\\ClearDayAWSP.txt\n'
            string3='dir /B /S /O:N PD['+os.path.basename(ClearDay_content[i])[:-5]+'*.csv >> '+dir+'\\clearDay\\ClearDayPD.txt\n'
            string4='dir /B /S /O:N INTG*'+os.path.basename(ClearDay_content[i])[:-5]+'*.csv >> '+dir+'\\clearDay\\AllINTG.txt\n'
            string5='dir /B /S /O:N AWSP*'+os.path.basename(ClearDay_content[i])[:-5]+'*.csv >> '+dir+'\\clearDay\\AllAWSP.txt\n'
            string6='dir /B /S /O:N PD['+os.path.basename(ClearDay_content[i])[:-5]+'*.csv >> '+dir+'\\clearDay\\AllPD.txt\n'
            INTG.append(string1)
            AWSP.append(string2)
            PD.append(string3)
            All.append(string4)
            All.append(string5)
            All.append(string6)
    for i in range(len(ClearNight_content)):
        if ClearNight_content[i]!='\x1a':
            string1='dir /B /S /O:N INTG*'+os.path.basename(ClearNight_content[i])[:-5]+'*.csv >> '+dir+'\\clearNight\\ClearNightINTG.txt\n'
            string2='dir /B /S /O:N AWSP*'+os.path.basename(ClearNight_content[i])[:-5]+'*.csv >> '+dir+'\\clearNight\\ClearNightAWSP.txt\n'
            string3='dir /B /S /O:N PD['+os.path.basename(ClearNight_content[i])[:-5]+'*.csv >> '+dir+'\\clearNight\\ClearNightPD.txt\n'
            string4='dir /B /S /O:N INTG*'+os.path.basename(ClearNight_content[i])[:-5]+'*.csv >> '+dir+'\\clearNight\\AllINTG.txt\n'
            string5='dir /B /S /O:N AWSP*'+os.path.basename(ClearNight_content[i])[:-5]+'*.csv >> '+dir+'\\clearNight\\AllAWSP.txt\n'
            string6='dir /B /S /O:N PD['+os.path.basename(ClearNight_content[i])[:-5]+'*.csv >> '+dir+'\\clearNight\\AllPD.txt\n'
            INTG.append(string1)
            AWSP.append(string2)
            PD.append(string3)
            All.append(string4)
            All.append(string5)
            All.append(string6)
    for i in range(len(RainDay_content)):
        if RainDay_content[i]!='\x1a':
            string1='dir /B /S /O:N INTG*'+os.path.basename(RainDay_content[i])[:-5]+'*.csv >> '+dir+'\\rainDay\\RainDayINTG.txt\n'
            string2='dir /B /S /O:N AWSP*'+os.path.basename(RainDay_content[i])[:-5]+'*.csv >> '+dir+'\\rainDay\\RainDayAWSP.txt\n'
            string3='dir /B /S /O:N PD['+os.path.basename(RainDay_content[i])[:-5]+'*.csv >> '+dir+'\\rainDay\\RainDayPD.txt\n'
            string4='dir /B /S /O:N INTG*'+os.path.basename(RainDay_content[i])[:-5]+'*.csv >> '+dir+'\\rainDay\\AllINTG.txt\n'
            string5='dir /B /S /O:N AWSP*'+os.path.basename(RainDay_content[i])[:-5]+'*.csv >> '+dir+'\\rainDay\\AllAWSP.txt\n'
            string6='dir /B /S /O:N PD['+os.path.basename(RainDay_content[i])[:-5]+'*.csv >> '+dir+'\\rainDay\\AllPD.txt\n'
            INTG.append(string1)
            AWSP.append(string2)
            PD.append(string3)
            All.append(string4)
            All.append(string5)
            All.append(string6)
    for i in range(len(RainNight_content)):
        if RainNight_content[i]!='\x1a':
            string1='dir /B /S /O:N INTG*'+os.path.basename(RainNight_content[i])[:-5]+'*.csv >> '+dir+'\\rainNight\\RainNightINTG.txt\n'
            string2='dir /B /S /O:N AWSP*'+os.path.basename(RainNight_content[i])[:-5]+'*.csv >> '+dir+'\\rainNight\\RainNightAWSP.txt\n'
            string3='dir /B /S /O:N PD['+os.path.basename(RainNight_content[i])[:-5]+'*.csv >> '+dir+'\\rainNight\\RainNightPD.txt\n'
            string4='dir /B /S /O:N INTG*'+os.path.basename(RainNight_content[i])[:-5]+'*.csv >> '+dir+'\\rainNight\\AllINTG.txt\n'
            string5='dir /B /S /O:N AWSP*'+os.path.basename(RainNight_content[i])[:-5]+'*.csv >> '+dir+'\\rainNight\\AllAWSP.txt\n'
            string6='dir /B /S /O:N PD['+os.path.basename(RainNight_content[i])[:-5]+'*.csv >> '+dir+'\\rainNight\\AllPD.txt\n'
            INTG.append(string1)
            AWSP.append(string2)
            PD.append(string3)
            All.append(string4)
            All.append(string5)
            All.append(string6)
    for i in range(len(SnowDay_content)):
        if SnowDay_content[i]!='\x1a':
            string1='dir /B /S /O:N INTG*'+os.path.basename(SnowDay_content[i])[:-5]+'*.csv >> '+dir+'\\snowDay\\SnowDayINTG.txt\n'
            string2='dir /B /S /O:N AWSP*'+os.path.basename(SnowDay_content[i])[:-5]+'*.csv >> '+dir+'\\snowDay\\SnowDayAWSP.txt\n'
            string3='dir /B /S /O:N PD['+os.path.basename(SnowDay_content[i])[:-5]+'*.csv >> '+dir+'\\snowDay\\SnowDayPD.txt\n'
            string4='dir /B /S /O:N INTG*'+os.path.basename(SnowDay_content[i])[:-5]+'*.csv >> '+dir+'\\snowDay\\AllINTG.txt\n'
            string5='dir /B /S /O:N AWSP*'+os.path.basename(SnowDay_content[i])[:-5]+'*.csv >> '+dir+'\\snowDay\\AllAWSP.txt\n'
            string6='dir /B /S /O:N PD['+os.path.basename(SnowDay_content[i])[:-5]+'*.csv >> '+dir+'\\snowDay\\AllPD.txt\n'
            INTG.append(string1)
            AWSP.append(string2)
            PD.append(string3)
            All.append(string4)
            All.append(string5)
            All.append(string6)
    for i in range(len(SnowNight_content)):
        if SnowNight_content[i]!='\x1a':
            string1='dir /B /S /O:N INTG*'+os.path.basename(SnowNight_content[i])[:-5]+'*.csv >> '+dir+'\\snowNight\\SnowNightINTG.txt\n'
            string2='dir /B /S /O:N AWSP*'+os.path.basename(SnowNight_content[i])[:-5]+'*.csv >> '+dir+'\\snowNight\\SnowNightAWSP.txt\n'
            string3='dir /B /S /O:N PD['+os.path.basename(SnowNight_content[i])[:-5]+'*.csv >> '+dir+'\\snowNight\\SnowNightPD.txt\n'
            string4='dir /B /S /O:N INTG*'+os.path.basename(SnowNight_content[i])[:-5]+'*.csv >> '+dir+'\\snowNight\\AllINTG.txt\n'
            string5='dir /B /S /O:N AWSP*'+os.path.basename(SnowNight_content[i])[:-5]+'*.csv >> '+dir+'\\snowNight\\AllAWSP.txt\n'
            string6='dir /B /S /O:N PD['+os.path.basename(SnowNight_content[i])[:-5]+'*.csv >> '+dir+'\\snowNight\\AllPD.txt\n'
            INTG.append(string1)
            AWSP.append(string2)
            PD.append(string3)
            All.append(string4)
            All.append(string5)
            All.append(string6)

    outputfile=open("vid2weather.bat","w")
    #outputfile.write('CD /D'+dir+'\n')
    outputfile.write('mkdir '+dir+'\\clearDay'+'\n')
    outputfile.write('mkdir '+dir+'\\clearNight'+'\n')
    outputfile.write('mkdir '+dir+'\\rainDay'+'\n')
    outputfile.write('mkdir '+dir+'\\rainNight'+'\n')
    outputfile.write('mkdir '+dir+'\\snowDay'+'\n')
    outputfile.write('mkdir '+dir+'\\snowNight'+'\n')
    outputfile.write('copy /y ClearDay.txt '+dir+'\\clearDay\\'+'\n')
    outputfile.write('copy /y ClearNight.txt '+dir+'\\clearNight\\'+'\n')
    outputfile.write('copy /y RainDay.txt '+dir+'\\rainDay\\'+'\n')
    outputfile.write('copy /y RainNight.txt '+dir+'\\rainNight\\'+'\n')
    outputfile.write('copy /y SnowDay.txt '+dir+'\\snowDay\\'+'\n')
    outputfile.write('copy /y SnowNight.txt '+dir+'\\snowNight\\'+'\n')
    outputfile.write('CD /D '+dir+'\n')
    for i in range(len(INTG)):
        outputfile.write(INTG[i])
    outputfile.write('\n')
    for i in range(len(AWSP)):
        outputfile.write(AWSP[i])
    outputfile.write('\n')
    for i in range(len(PD)):
        outputfile.write(PD[i])
    outputfile.write('\n')
    for i in range(len(All)):
        outputfile.write(All[i])
    outputfile.write('\n')
    outputfile.close()
    subprocess.call(['vid2weather.bat'])
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="AWS AttrMgr CLI",
                                     usage = '''
                                    Provide 1 arguments:

                                    1. A vidlist .txt file containing
                                    the locations of the videos you 
                                    wish to write attr data into
                                    ''',
                                     description='''
                                    ----------------------------------
                                    CLI for running AttrMgr.exe on 
                                    multiple videos to write AWS data
                                    to AWS_PD_REAR attribute
                                    ----------------------------------
                                    ''',
                                     epilog = "Made by Yan",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     add_help=True)
    parser.add_argument("directory",type=str,help="Enter the path of the source directory",metavar="DIRECTORY")

    arg=parser.parse_args()

    create(arg.directory)
    #create('T:\Xai\work\kpi_20210426\b2_CClassBrRear_2090')