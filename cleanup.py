from calendar import week
from cmath import inf
from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import datetime as dt
import uuid 
import numpy as np

#1
## load csv into python
df = pd.read_csv('data/School_Learning_Modalities.csv')

#2
## counts the columns and rows
df.shape

#3
## list out the columns names
list(df)

#4/5/6
## column names cleaned and removed all whitespaces or special characters  
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') 
list(df)

#7 convert column to the correct column type
df.dtypes   ## this shows the category of the data type
df['Week'] = pd.to_datetime(df['Week'])

#8 look for duplicated rows and remove them
df.duplicated()
df.drop_duplicates()

#9 assess missingness
df.isnull().sum() ## provides a count of missing values in each column
df.replace(to_replace='', value=np.nan, inplace=True) ## replacing empty cells with NaN with numpy
df.replace(to_replace=' ', value=np.nan, inplace=True) ## replacing cells with whitespace with NaN

#10 New data
list(df)
df['modality_inperson'] = df['Learning_Modality'].apply(lambda x: 'true' if x == 'In Person' else 'false')
print(df['Learning_Modality'],df['modality_inperson'])
