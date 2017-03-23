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
# importing sql data into pandas data frame
##########################################################################
conn = sqlite3.connect("mydatabase.db") 
sql = "SELECT * FROM coupon_redemption"
df = pd.read_sql_query(sql, conn)
df.drop_duplicates(subset = ["coupon_id", "user_id"], inplace = True)
df['rating'] = pd.Series(1, index=df.index)
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

