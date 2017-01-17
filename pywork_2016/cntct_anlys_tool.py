import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('me_contacts.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

iterator =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for no in iterator:
    for i, ele in enumerate(columns[iterator[no-1]]):
        print(i, ele)


#print(no_ele)
'''
if int(no_ele)>=20:
    over20=[]
    over20.append(ele)
elif (no_ele>10) and (no_ele<20):
    btw10n20=[]
    btw10n20.append(ele)
else:
    None
'''
