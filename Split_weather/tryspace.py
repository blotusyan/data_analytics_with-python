import csv
import os
import math
import shutil
import os.path
import subprocess

source_dir=os.path.dirname(__file__)
os.chdir(source_dir)
subprocess.call([source_dir +'\\'+'run.bat'])

fileopen1 = open("ClearNight.txt","r")
ClearNight_content=fileopen1.readlines()


print(ClearNight_content)
fileopen1.close()