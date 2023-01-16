import csv
import math
import shutil
import xlwings as xw


def movKpiResults(vidnum,buildname,filename):
    #this function gather information from comparison file generated from kpi
    #run into kpi report
    #Things to be gathered:
        #1)Average distance of TD
        #2)Three columns of data
    #The name of the build still need manual input
    with open (filename, newline = '') as csvfile:
        data= [row for row in csv.reader(csvfile)]
        
        #get TD value
        TD_index=vidnum*5+27
        TD=data[TD_index][7]
        
        #get TP value
        TP_index_1=vidnum*5+17
        TP_1=data[TP_index_1][8]
        
        TP_index_2=vidnum*5+18
        TP_2=data[TP_index_2][8]
        
        TP_index_3=vidnum*5+19
        TP_3=data[TP_index_3][8]
        
        TP_index_4=vidnum*5+20
        TP_4=data[TP_index_4][8]

        TP_index_5=vidnum*5+21
        TP_5=data[TP_index_5][8]
        
        #get FP value
        FP_index_1=vidnum*5+17
        FP_1=data[FP_index_1][9]
        
        FP_index_2=vidnum*5+18
        FP_2=data[FP_index_2][9]
        
        FP_index_3=vidnum*5+19
        FP_3=data[FP_index_3][9]
        
        FP_index_4=vidnum*5+20
        FP_4=data[FP_index_4][9]

        FP_index_5=vidnum*5+21
        FP_5=data[FP_index_5][9]

        #get Accuracy value
        AC_index_1=vidnum*5+17
        AC_1=data[AC_index_1][11]
        
        AC_index_2=vidnum*5+18
        AC_2=data[AC_index_2][11]
        
        AC_index_3=vidnum*5+19
        AC_3=data[AC_index_3][11]
        
        AC_index_4=vidnum*5+20
        AC_4=data[AC_index_4][11]

        AC_index_5=vidnum*5+21
        AC_5=data[AC_index_5][11]
        #print(AC_index_5)
        #print(AC_5)

    wb=xw.Book('KPI_REPORT.xlsx')
    sh=wb.sheets['Sheet1']
    sh.range('C2').value=TD
    sh.range('C3').value=vidnum
    sh.range('C5').value=buildname
    sh.range('C11').value=buildname
    sh.range('C17').value=buildname
    
    sh.range('C6').value=TP_1
    sh.range('C7').value=TP_2
    sh.range('C8').value=TP_3
    sh.range('C9').value=TP_4
    sh.range('C10').value=TP_5
    
    sh.range('C12').value=FP_1
    sh.range('C13').value=FP_2
    sh.range('C14').value=FP_3
    sh.range('C15').value=FP_4
    sh.range('C16').value=FP_5

    sh.range('C18').value=AC_1
    sh.range('C19').value=AC_2
    sh.range('C20').value=AC_3
    sh.range('C21').value=AC_4
    sh.range('C22').value=AC_5
    
        

vidnum = int(input("Please enter number of video: "))
build_name = input("Please enter build name: ")
file_name = input("Please enter file name: ")
movKpiResults(vidnum, build_name, file_name)
