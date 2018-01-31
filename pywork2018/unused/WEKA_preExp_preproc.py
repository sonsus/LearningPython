# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
# imports
import sys
sys.version_info
from os import listdir
from os.path import isdir, join
import os
import pandas as pd
import numpy as np
# preprocessing 
from datetime import datetime, timedelta
import math
# weka file
#import arff
import csv
from supportings_f import *
#utf-8 코딩 붙이니까 주석으로 한글도 인정하네 인지용? 권지용? 오지구용?


Procedure_Not_Exist= -1

#workID_toNum
# 0     1       2       3       4       5       6
# stb1  stb1    stb2    ub      stop    RS      stop

if __name__=="__main__":
    ############
    ##READ CSV##
    ############
    
    data_dir = './data/New' # dir for data
    
    date_list = [ "/".join([data_dir, d]) for d in listdir(data_dir)] 
    # make date-wise data list 
    dir_list = list()
    for date in date_list:
        temp = listdir(date)
        for f in temp :
            dir_list.append("/".join([date, f]))
    
    #########
    #preproc#
    #########
    
    FINAL_df_sparse=None # final dataframe to be dumped on a csv will assign here
    FINAL_df_complete=None # final dataframe to be dumped on a csv will assign here

    workID_toStr = {12547 : "AB", 12548 : "AB", 12557 : "AB", 12559 : "AB", 
                    12802 : "MS", 12813 : "MS", 12815 : "MS",
                    13057 : "108stb1", 13058 : "108stb1", 13059 : "108stb2", 13060 : "108ub", 13071 : "stop_108", 
                    13314 : "RS", 13327 : "stop_RS"}
    drop_list = [12557, 12559, 12813, 12815, 13071, 13327]
    workID_toNum = {13057:0, 13058:1, 13059:2, 13060:3, 13071:4, 13314:5, 13327:6}
                    # 0         1       2       3           4       5       6
                    # stb1      stb1    stb2    ub          stop    RS      stop
    element_list = [["Start_time", "Col2", 0],
                    ["End_time", "Col2", -1],
                    ["Stage", "UB Stage", 0],
                    ["Work_ID", "work_ID", 0]
                    ]#Col2: human readable timestmp
    
    max_sec = 0
    no_csv_list = list() #missing csv
    empty_csv_list = list() # empty csv
    waste_list = list() # weird data
    nan_list = list() #nan entry exists
    
    for i, d in enumerate(dir_list):
        # Read a CSV file
        # The line 0 is the header.
        csv_list = [ csv for csv in sorted(os.listdir(d)) if not (csv in ["out_MS.csv, out_AB.csv"] or os.path.isdir("{}/{}".format(d, csv))) ] #?
        csv_empty = False
        if len(csv_list) < 4 : #  MS AB 108 RS = 4 interval data exists
            no_csv_list.append(d)
            continue
        
        intervals = list() 
        for csv in csv_list :
            # dataframe is intstantiated from csv
            df = pd.read_csv("{}/{}".format(d, csv), encoding='cp949', header=0)
            #print(list(df.index)) # int row no 
            #print(list(df.columns)) # column in unicode list 
            #exit("197")
            if len(df) == 0 : # empty csv check
                csv_empty = True
                break
            
            # Add Basic Information
            df['Name'] = d.decode('cp949').encode('utf-8')
            df['csv'] = csv
            df['time'] = df['Col2'].apply(lambda x: pd.to_datetime(str(x), format='%H:%M:%S'))
            
            # Turbin Velocity name encoding prob --> readable form 
            new_columns = df.columns.values
            new_columns[105] = "TV_new"
            df.columns = new_columns
            
            # Split Dataframe
            intervals.extend(split_interval(df)) 
            
        if csv_empty : # empty csv --> quit processing: intervals also reinitialized
            empty_csv_list.append(d)
            continue
        
        new_intervals = list()
        for df in intervals :
            is_waste = check_waste(df, "TV_new")
            if is_waste : waste_list.append(d)
            is_nan = check_nan(df, "TV_new")
            if is_nan : nan_list.append(d)
            if is_waste or is_nan : 
                continue
            new_intervals.append(df)
        intervals = new_intervals
        if len(intervals) == 0 : 
            empty_csv_list.append(d)
            continue
                
        infos = make_information(intervals, element_list, workID_toStr, drop_list)
        infos = order_information(infos)
        #print(infos)

        start_time = intervals[infos[0]["index"]]["time"][0]
         # infos 는 intervals 내의 어떤 부분에 위치하는지 알려준다.
        
        df_unfiltered = list()
        for df in intervals :
            
            #### leave useful columns only 
            # Name: filepath 
            # 'Col2': timestamp
            # 'UB Stage': UB stage. among 3 , we need only 2
            # 'word ID': <<<<label-translated>>>> workID 행정번호 !!라벨!! (0,1,2,3,4)
            # 'Col35': RS stage
            #### important stats TV_new / UB 
            # 'UB': UB
            #  TV_new: turbin velocity (frequency)
            #  time diff: if timediff large --> another interval started
    
            df = df[['Name', 'Col2', 'UB Stage', 'work_ID', 'Col35', 'UB',  "TV_new", 'time diff' ]]
            
            #Only see UB stage2
            df2=df[df['UB Stage']==2]
            
            # Change workID to workID label
            for k in workID_toNum.keys() :
                df2["work_ID"] = df2["work_ID"].replace(k, workID_toNum[k])
            
            # 마지막 drop 발생 이후 지점만 남김
            for i, case in enumerate(drop_list):
                drop_exist = (df2[df2['work_ID'] == case].shape[0] != 0) 
                if drop_exist:
                    drop_index = (df2.work_ID == case)
                    last_drop_index = drop_index[drop_index == True].index[-1] 
                    df2 = df[df.index > last_drop_index]
            
            #행정 별 분할되지 않은(unfiltered)에 집어넣자
            df_unfiltered.append(df2)
    
    
        #드랍은 바로 위에서 다 걸렀으니까 여기선 걸리면 안된다.
        result_df_list, filter_res_msg= filter_df2_intervals_XY(infos, df_unfiltered)
        
        Result_ROW= unfold_df_into_a_row(result_df_list, filter_res_msg)
        if type(Result_ROW) != type(-1):
            if filter_res_msg == "trash": 
                continue
                '''
                i)filter_res_msg == "complete"
                == list(df2_stb1, df2_stb2, df2_ub, \
                            df2_rs1, df2_rs2, df2_rs3, \
                            df2_108, df2_rs12, df_108_rs12, \
                            df2_rs456)
                혹은

                ii)filter_res_msg == "sparse"
                == list(df2_108, df2_rs12, df_108_rs12, df2_rs456)

                혹은 

                iii)filter_res_msg == "trash"
                == -1 (==Procedure_Not_Exist)
                '''
            elif filter_res_msg == "sparse":
                if FINAL_df_sparse==None:
                    FINAL_df_sparse=unfold_df_into_a_row(result_df_list, filter_res_msg) 
                else:
                    FINAL_df_sparse=pd.concat(FINAL_df_sparse, unfold_df_into_a_row(result_df_list, filter_res_msg))
            else: 
                if FINAL_df_complete:
                    FINAL_df_complete=unfold_df_into_a_row(result_df_list, filter_res_msg)
                else:
                    FINAL_df_complete=pd.concat(FINAL_df_complete, unfold_df_into_a_row(result_df_list, filter_res_msg))
                # for loop이 다 돌면 멋진 dataframe 이 나와있을것
                # 이라고 소망...
    
        if (i+1)%100 == 0 :
            print("{}/{}".format(i+1, len(dir_list)))
    
    
    print("ALL DONE")
    print("shape FINAL_df_sparse : ", FINAL_df_sparse.shape )
    print("shape FINAL_df_complete :", FINAL_df_complete.shape)
    print("# of sparse Data : ", len(FINAL_df_sparse))
    print("# of complete Data : ", len(FINAL_df_complete))
    print("# of No CSV : ", len(no_csv_list))
    print("# of empty CSV : ", len(empty_csv_list))
    print("# of waste : ", len(set(waste_list)))
    
    print("\n\n writing on csv")
    FINAL_df_sparse.to_csv("./FINAL_df_sparse.csv", sep='\t', encoding='utf-8')
    FINAL_df_complete.to_csv("./FINAL_df_complete.csv", sep='\t', encoding='utf-8')
    #FINAL_df.to_csv(".\WEKA_preExp_preprocessed.csv", sep=',', encoding='utf-8')
    
