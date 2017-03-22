# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
import gensim
import sqlite3
import numpy as np
import pandas as pd
import os
from pandas import read_hdf

os.getcwd()
os.listdir(".")
goal_dir = os.path.join("Documents", "Python Scripts")
os.chdir(goal_dir)
os.getcwd()

### module to create pandas matrix, storing pandas matrix into hdfs,
### saving hdfs file, and retrieving those files


hdf = pd.HDFStore('storage.h5')
print(hdf)

df = pd.DataFrame(np.random.rand(5,3), columns=('A','B','C'))
# put the dataset in the storage
hdf.put('d1', df, format='table', data_columns=True)
print hdf['d1'].shape

hdf.append('d1', pd.DataFrame(np.random.rand(5,3), 
           columns=('A','B','C')), 
           format='table', data_columns=True)
hdf.close() # closes the file         


# this query selects the columns A and B
# where the values of A is greather than 0.5
hdf = pd.read_hdf('storage.h5', 'd1',
               where=['A>.5'], columns=['A','B'])


hdf = pd.HDFStore('storage.h5')
hdf.put('tables/t1', pd.DataFrame(np.random.rand(20,5)))
hdf.put('tables/t2', pd.DataFrame(np.random.rand(10,3)))
hdf.put('new_tables/t1', pd.DataFrame(np.random.rand(15,2)))

print hdf
