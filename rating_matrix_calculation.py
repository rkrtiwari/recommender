# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:20:16 2017

@author: ravitiwari
"""

import os
import sqlite3
import pandas as pd

###########################################################################
# Setting working directory
###########################################################################
os.getcwd()
os.path.join("Documents", "Python Scripts", "recommender")
os.chdir(os.path.join("Documents", "Python Scripts", "recommender"))
os.getcwd()

##########################################################################
# importing sql data (both rating and impression) into pandas data frame
##########################################################################
conn = sqlite3.connect("mydatabase.db") 
sql1 = "SELECT * FROM coupon_redemption"
df1 = pd.read_sql_query(sql1, conn)
sql2 = "SELECT * FROM coupon_impression"
df2 = pd.read_sql_query(sql2, conn)
conn.close()

df1['rating'] = pd.Series(1, index=df1.index)
df2['rating'] = pd.Series(0.7, index=df2.index)
df = df1.append(df2)

df.drop_duplicates(subset = ["user_id", "coupon_id"], inplace = True)
rating_matrix = df.pivot(index = "user_id", columns = "coupon_id", values = "rating")
rating_matrix


##############################################################################
# updating rating matrix when a user redeems a coupon
##############################################################################
user_id = 14
coupon_id = 14

rating_matrix.loc[user_id, coupon_id] = 1

#############################################################################
# Updating rating matrix when a user views a coupon
#############################################################################
user_id = 14
coupon_id = 13

if (rating_matrix.loc[user_id, coupon_id] != 1):
    rating_matrix.loc[user_id, coupon_id] = 0.7


