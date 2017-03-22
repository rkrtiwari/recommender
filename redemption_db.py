# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:56:38 2017

@author: ravitiwari
"""

import os
import numpy as np
import pandas as pd
import sqlite3

os.getcwd()
os.listdir(".")

#########################################################################################
## creating fictitious data for feeding into the data table
###########################################################################################
user_id = np.arange(100)
coupon_id = np.arange(20)

users = np.random.choice(user_id, 1000)
coupons = np.random.choice(coupon_id, 1000)

year = np.random.randint(2015, 2016, 1000)
month = np.random.randint(1, 12, 1000)
day = np.random.randint(1, 28, 1000)

red_data = zip(coupons, users, year, month, day)

##############################################################################################
# Creating database connection, and adding records to database
############################################################################################## 
conn = sqlite3.connect("mydatabase.db") 
cursor = conn.cursor()

#sql = "DROP TABLE coupon_redemption"
#cursor.execute(sql)
 
# create a table
cursor.execute("""CREATE TABLE coupon_redemption
                  (coupon_id INT, user_id INT, 
                    red_year INT, red_month INT,
                    red_day INT) 
               """)
                  

# insert some data
cursor.executemany("INSERT INTO coupon_redemption VALUES (?,?,?,?,?)", red_data)

conn.commit()
conn.close()

###############################################################################
# inserting new data into the database
###############################################################################
conn = sqlite3.connect("mydatabase.db") 
cursor = conn.cursor()

sql = "INSERT INTO coupon_redemption VALUES (?,?,?,?,?)"
cursor.execute(sql, (5, 23, 2016, 1, 1))
conn.commit()
conn.close()

###########################################################################
# QUerying for a value
##########################################################################
conn = sqlite3.connect("mydatabase.db") 
cursor = conn.cursor()

sql = "SELECT * FROM coupon_redemption WHERE red_month = 1 AND red_day = 1"
cursor.execute(sql)
all_row = cursor.fetchall()

for row in all_row:
    print row

conn.close()










