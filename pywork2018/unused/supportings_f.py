# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
# imports
import sys
sys.version_info
import pandas as pd
import numpy as np
# preprocessing 
import math

Procedure_Not_Exist= -1

# time diff check --> intervals ( huge diff btw time >1 means new interval starts there)
def split_interval(df) :
    time_diff = df['time diff']
    intervals = list()
    start = 0
    for i in range(len(time_diff)-1) :
        if time_diff[i+1] > 1 :
            end = i+1
            intervals.append(df.iloc[start:end].reset_index(drop=True))
            start = end
    intervals.append(df[start:].reset_index(drop=True))
    for interval in intervals :
        if len(interval) == 0 : 
            print(df['Name'][0], df["csv"][0])
    return intervals

# Dataframe summary
def make_information(intervals, element_list, workID_toStr, drop_list) :
    info = [0] * len(intervals)
    for i, interval in enumerate(intervals) :
        seq = dict()
        # fundamental info in
        seq["index"] = i
        seq["pivot_time"] = list(interval["Col2"])[0]
        seq["Work"] = workID_toStr[list(interval["work_ID"])[0]] 
        seq["Drop"] = False
        work_ID_list = list(interval['work_ID'])
        for id in work_ID_list :
            if id in drop_list :
                seq["Drop"] = True
        # additional info
        for key, value, idx in element_list :
            seq[key] = list(interval[value])[idx]
        info[i] = seq
    return info

# probe Informations (=summary) ordering
def find_info_order(infos) :
    pivot_times = list()
    for info in infos :
        pivot_times.append(info["pivot_time"])
    index = sorted(range(len(pivot_times)), key=lambda k: pivot_times[k])
    return index

# sort Informations (=summary)
def order_information(infos) :
    index = find_info_order(infos)
    infos_new = list()
    for idx in index :
        infos_new.append(infos[idx])
    return infos_new
            
# waste check
def check_waste(df, key) :
    is_waste = True
    if len(df) < 5 : return is_waste # shorter than 5 means it is waste
    value_ref = df[key][0]
    for i in range(1,5) :
        if value_ref != df[key][i] :
            is_waste = False
    return is_waste

def check_nan(df, key) :
    return math.isnan(df[key][0])



def make_delta_col(df, key):
    return df[key].diff().rename("d_"+key)
def make_delta2_col(df, key):
    return df[key].diff().diff().rename("d2_"+key)


def filter_df2_intervals_XY(infos, df_unfiltered) :

    def df_check_n_concat(df_list):
        actual_target=list()
        for df in df_list:
            if type(df) == type(1): continue
            else: actual_target.append(df) # 정수이면 배정받지 못한거임
        
        if len(actual_target)>1:
            return pd.concat(df_list).reset_index(drop=True)
        elif len(actual_target)==1:
            return actual_target[0]
        else: return Procedure_Not_Exist # =-1 정수를 리턴해 결과물에도 다시 적용할 수 있또록 함

    df2_stb1, df2_stb2, df2_ub,\
    df2_rs1, df2_rs2,\
    df2_rs4, df2_rs5, df2_rs6,\
    df2_108, df2_rs12, df2_108_rs12, \
    df2_rs456 = range(12) #임의의 정수로 선언

    for i in range(len(infos)) :
        work_name=infos[i]["Work"]
        df_index=infos[i]["index"]
        target_df=df_unfiltered[df_index]
        #파이썬에는 switch equivalent가 없고 dictionary로 대체 가능한데 좀 못생겼다. lambda가 첨볼때 무서운 것처럼?
        if infos[i]["Stage"] == 2: #infos에는 그대로 stage 2 외에도 남아있으므로
            if work_name=="108stb1":    df2_stb1=target_df
            elif work_name=="108stb2":  df2_stb2=target_df
            elif work_name=="108ub":    df2_ub=target_df
            elif work_name=="RS":
                for rs_lv in [0,1,3,4,5]: #(rs 1 2   4 5 6)
                    rs_lv_mask= (target_df.Col35 == rs_lv)
                    lv_row_start= rs_lv_mask[rs_lv_mask==True].index[0]
                    lv_row_end= rs_lv_mask[rs_lv_mask==True].index[-1]
                    
                    df_rs_part=target_df[(target_df.index>lv_row_start) & (target_df.index<=lv_row_end)] # 이부분이 작동하는지 조금 의문이지만 글쎄...
                    
                    if   rs_lv==0: df2_rs1=df_rs_part
                    elif rs_lv==1: df2_rs2=df_rs_part
                    elif rs_lv==3: df2_rs4=df_rs_part
                    elif rs_lv==4: df2_rs5=df_rs_part
                    elif rs_lv==5: df2_rs6=df_rs_part
    #after for loop on infos finishes,
    #stb1 --> RS 로 가는 경우가 있었다! (stb2 는 왜 안 거쳤나!)
    #덕분에 구간별 세분화는 철회해야할 ㄱ것 같ㄷ다 난..가끔 눙물을ㄹ 흘린ㄷㅏ..** 이럴케 눙ㄴ물흘릴 쑤 있눈 내가 좋타..***
    #아니 세부 구간이 다 존재하는 놈들만 가지고도 csv를 하나 만들어봐야겠다(일단 뭉뚱그린 놈부터?...?)

    df2_108=df_check_n_concat([df2_stb1,df2_stb2,df2_ub])
    df2_rs12=df_check_n_concat([df2_rs1,df2_rs2])
    df2_108_rs12=df_check_n_concat([df2_108, df2_rs12])
    df2_rs456=df_check_n_concat([df2_rs4, df2_rs5, df2_rs6]) 
    
    result_df_list=[df2_stb1, df2_stb2, df2_ub, \
                    df2_rs1, df2_rs2, \
                    df2_108, df2_rs12, df2_108_rs12, \
                    df2_rs456]
    
    
    for stats in ['TV_new', 'UB']:
        for i,res_df in enumerate(result_df_list):
            if type(res_df) == type(Procedure_Not_Exist) : continue
            result_df_list[i].join(make_delta_col(res_df, stats))
            result_df_list[i].join(make_delta2_col(res_df, stats))

    if len(result_df_list)==9:
        filter_res_msg="complete"
    elif len(result_df_list)<9:
        if type(Procedure_Not_Exist) in [type(df2_108), type(df2_rs12), type(df2_rs456)]:
            filter_res_msg="trash"
        else:
            filter_res_msg="sparse"

    if filter_res_msg=="complete": pass # 그대로 result_df_list 전달
    
    elif filter_res_msg=="sparse": # 세부구간 삭제, dataframe 축소
        for i, res_df in enumerate(result_df_list):
            result_df_list= result_df_list[-4:]
            print(result_df_list)
    else: result_df_list=Procedure_Not_Exist # 못 씀, __main__에서 continue로 스킵 

    return result_df_list, filter_res_msg 
    '''
    same as list(df2_stb1, df2_stb2, df2_ub, \
                df2_rs1, df2_rs2, df2_rs3, \
                df2_108, df2_rs12, df_108_rs12, \
                df2_rs456)
    '''
def unfold_df_into_a_row(result_df_list, filter_res_msg):
    if filter_res_msg == "complete":
        Procedure_name=["stb1", "stb2", "ub", "rs1", "rs2", "108", "rs12", "108_rs12" ]
    elif filter_res_msg == "sparse":
        Procedure_name=["108", "rs12", "108_rs12"]

    Xset = result_df_list[:-1] #for feature extraction
    Y_df = result_df_list[-1] #df2_rs456 
    npX = None #actual row value for csv input
    
    # get required columns and rows (it's for transposed ) 
    rowidx, colidx=['UB', 'd_UB', 'd2_UB', 'TV_new', 'd_TV_new', 'd2_TV_new'], \
                    ['std', '25%', '50%', '75%', 'max']
    # get stats of X_df's,
    # and 
    # transpose result X_df's
    for i, X_df in enumerate(Xset):
        try:
            Xset[i]=X_df.describe().T.loc[rowidx[:], colidx]
            if i==0: npX=X_df.values.flatten()
            else   : npX= np.concatenate( (npX, X_df.values.flatten()) )
        except: return -1 
    Yrow=colidx
    Yval=Y_df.describe().loc[Yrow[-1],'TV_new'] > 17.5 #max, 'TV_new'

    result_ROW=np.append(npX, Yval)


    # header for resulting row 
    unfold_header=list()
    for procedure in Procedure_name:
        for rowname in rowidx:
            for colname in colidx:
                unfold_header.append(procedure+rowname+"_"+colname)
    unfold_header.append('Y')

    return pd.DataFrame(result_ROW, columns=unfold_header)