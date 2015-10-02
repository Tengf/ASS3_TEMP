from pandas import DataFrame, read_csv
import pandas as pd
from numpy import * 
import matplotlib.pyplot as plt

# get data, (file path need editting)
df = pd.read_csv('201501-citibike-tripdata.csv', parse_dates=['starttime'])

df['Dura_Subs'] = df['tripduration'][df['usertype']=='Subscriber']
df['Dura_Cust'] = df['tripduration'][df['usertype']=='Customer']
df.Dura_Subs.describe()
# print df.Dura_Subs.mean(), df.Dura_Cust.mean()
# print 