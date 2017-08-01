import numpy as np
import pandas as pd
import csv
import os
import sys


class SFC:
    #name age gender church withwho notwithwho
    def __init__(self, chart_row=["n/a", 0, "n/a", "n/a", None, None]):
        self.name=chart_row[0]
        try: self.age=int(chart_row[1]) #handling value error exception for the first line ("int(string)")
        except: return 
        self.gender="m" if chart_row[2]=="남자" else "f" #m for male, f for female
        self.church=chart_row[3]

        \# need to check here whether len(row) will be 6 if the row has nwithwho but withwho
        if len(chart_row)>4 and type(chart_row[4])==type("string"): self.with_list=list(chart_row[4].split(","))
        if len(chart_row)>5 and type(chart_row[5])==type("string"): self.nwith_list=list(chart_row[5].split(","))
        print("constructor is executed for chart_row:%s"%chart_row)

def truncate_tail(chart_row): #chart_row==[name, age, gender, church]
    ch_full=chart_row[-1].rstrip()
    if ch_full[-2:]=="교회": 
        church_prefix=ch_full[:-2] #truncate if church name contains "교회"
        chart_row[-1]=church_prefix
    return chart_row 

#currnet working directory should contain target file: staff.csv
#the script should be run on the same directory as the target file
def currentdir():
    return os.getcwd()+"\\"

def excel_2_csv(xlsx_name):
    data_xls = pd.read_excel(currentdir()+xlsx_name, 'Sheet2', index_col=None)
    csv_name=xlsx_name[:-4]+"csv"
    data_xls.to_csv(csv_name, encoding='utf-8', index=False)
    return csv_name

def csv_2_lists(csv_name):#csv name need to be a string 
    currentdir=os.getcwd()
    with open(currentdir+"\\"+csv_name, 'r', newline="") as csv_f:
        chart=csv.reader(csv_f, delimiter="\t")
        
        sfc_list=[SFC(truncate_tail(row)) for row in chart]
        del sfc_list[0] #removing empty SFC object created 
        
        age_desc_list=sorted(sfc_list, key=lambda sfc: sfc.age, reverse=True)
        return  sfc_list, age_desc_list

