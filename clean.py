import pandas as pd
import math
import numpy as np
from pandas.types import dtypes

def clean_age(x):
    if "||" in x:
        mylist = x.split("||")
    else:
        mylist = x.split("|")
    ret = []
    for ele in mylist:
        if "::" in ele:
            tmp = ele.split("::")
        else:
            tmp = ele.split(":")
        ret.append(tmp[1])
    return ret

def male(x):
    count = 0
    for ele in x:
        if ele == "Male":
            count += 1
    return count

def female(x):
    count = 0
    for ele in x:
        if ele == "Female":
            count += 1
    return count

def age_range(x, i, j):
    count = 0
    for ele in x:
        if int(ele) >= i and int(ele) < j:
            count += 1
    return count

raw = pd.read_csv('gun-violence-data_01-2013_03-2018.csv', parse_dates=['date'])
print(raw.size)
raw = raw.dropna()
print(raw.size)
raw['characteristics'] = raw.incident_characteristics.apply(lambda x: x.split("||"))
raw['age_group'] = raw.participant_age_group.apply(lambda x: clean_age(x))
raw['gun_ifstolen'] = raw.gun_stolen.apply(lambda x: clean_age(x))
raw['gun_types'] = raw.gun_type.apply(lambda x: clean_age(x))
raw['type'] = raw.participant_type.apply(lambda x: clean_age(x))
raw['status'] = raw.participant_status.apply(lambda x: clean_age(x))
raw['gender'] = raw.participant_gender.apply(lambda x: clean_age(x))
raw['age'] = raw.participant_age.apply(lambda x: clean_age(x))
raw['male'] = raw.gender.apply(lambda x: male(x))
raw['female'] = raw.gender.apply(lambda x: female(x))
raw['age_below_18'] = raw.age.apply(lambda x: age_range(x,0,18))
raw['age_18_to_30'] = raw.age.apply(lambda x: age_range(x,18,30))
raw['age_30_to_40'] = raw.age.apply(lambda x: age_range(x,30,40))
raw['age_40_to_50'] = raw.age.apply(lambda x: age_range(x,40,50))
raw['age_50_to_60'] = raw.age.apply(lambda x: age_range(x,50,60))
raw['age_above_60'] = raw.age.apply(lambda x: age_range(x,60,150))

res = raw.drop(['incident_characteristics','gun_stolen','gun_type','participant_age_group','participant_type','participant_status','participant_gender','participant_age','participant_relationship','participant_name'], axis=1, errors='ignore')
res.to_csv("clean_data", encoding='utf-8', index=False)
print(res.iloc[0])
