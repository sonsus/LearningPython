https://pandas.pydata.org/pandas-docs/stable/10min.html

# time diff check --> intervals ( huge diff btw time >1 means new interval starts there)
def split_interval(df) :
    time_diff = df['A']
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


def split_interval2(df): # if the last row of the data has large timediff: discarded
    time_diff = df['A']
    intervals = list()
    for i in time_diff.index:
        if time_diff[i] > 1:
            intervals.append(df[df.index< i].reset_index(drop=True))
            df=df[df.index >= i] # to keep a loop working correct, indices need to stay still
    for interval in intervals:
        if len(interval)==0: print(df['Name'][0], df['csv'][0]) # check what file at what dir is gone wrong
    return intervals 








'''
time_diff= df['time diff'].diff() # will return pd.Series which include diff with first elem NaN (intractable)
df.diff()  # will return pd.Dataframe with same size with df filled with diff (delta)

'''