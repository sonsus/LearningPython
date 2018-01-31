###끝까지 디버깅 못해서 죄송합니다.   
###가독성을 고려해서 코딩하였고 다음과 같은 문서를 15여분간 작성하였습니다.   
###코드는 작동이 중요한데 죄송합니다 ㅠㅠ


큰 방향
--------------------------------   

####1. pandas dataframe 으로 다 처리 후 --> pd.DataFrame.to_csv()    
    
####2. 스크립트가 길어져서 둘로 나눔    

    (1) WEKA_preExp_preproc.py : __main__ 포함    
    (2) supportings_f.py : 함수 포함    

####3. 2.의 두 스크립트는 같은 폴더에 존재해야하고 데이터 역시 같은 방식으로 ./data/New에 폴더별로 존재 (건드리지 않음)   

####4. supportings_f.py에서 기존에 없던 등장하는 함수   

```python
    def make_delta_col(df, key):
    def make_delta2_col(df, key): delta, **2 컬럼 만드는 함수 
    def filter_df2_intervals_XY(infos, df_unfiltered) : 
        def df_check_n_concat(df_list):
        #세부구간까지 합쳐서 한 실험에서의 통계치를 (그러니까 weka로 가는 파일에서는 한 줄에 해당하는) 뽑아내는 함수.
        #새끼함수는 없는 구간을 잘 걸러서 연결하도록 팜 
    def unfold_df_into_a_row(result_df_list, filter_res_msg):
        #그 통계치를 실제 한 줄로 쭉 펼치고 컬럼 이름도 짓는 함수
```

####5. unfold_df_into_a_row 의 리턴값 즉 FINAL_df_complete / sparse, 혹은 Result_ROW 를 concat으로 한 층 한 층 쌓아서 pd.DataFrame으로 만들고 이걸 csv에 전달하는게 목표. 자세한 형태는 다음과 같음   


    한 줄에 다음과같은 column들이 존재

    >    X: ["stb1", "stb2", "ub", "rs1", "rs2", "108", "rs12", "108_rs12" ]* ['UB', 'd_UB', 'd2_UB', 'TV_new', 'd_TV_new', 'd2_TV_new'] * ['std', '25%', '50%', '75%', 'max'] (9*6*5=270...개 죄ㅗㅇ합니다 ㅜㅠㅜ)    
    >    X: ["108", "rs12", "108_rs12" ]* ['UB', 'd_UB', 'd2_UB', 'TV_new', 'd_TV_new', 'd2_TV_new'] * ['std', '25%', '50%', '75%', 'max']
        (3*6*5 = 150개... 역시 죄송 ㅠ)    

    >    Y: rs456의 max 값의 boolean (>17.5)






주요한 수정 사항
-----------------------------------

####1. workID_toStr: 행정 번호에 따라 세부 행정까지 파악할 수 있게 콘텐츠가 변경됨 (사용함)   

####2. 데이터 중 stb1 후에 꼭 stb2 를 거치지 않았기 때문에 control flow 가 대폭 변경됨
```python   
    filter_res_msg: complete (모든 세부구간이 존재)
                    sparse (큰 구간만 다 존재 108 RS)
                    trash (큰 구간조차 누락 되어 쓸 수 없음)
    Procedure_not_Exist= -1 은 그런 맥락에서 가독성을 위해 사용
```

####3. supportings_f.py", line 119    
    >IndexError: index 0 is out of bounds for axis 0 with size 0    

    (여기까지 잡다가 문서 작성중 08:25AM)



