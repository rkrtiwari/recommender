# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:47:34 2017

@author: ravitiwari
"""

import os
import sqlite3
import numpy as np


os.getcwd()
os.listdir(".")

#########################################################
# Creating fictitous data
##########################################################

users = np.arange(100)
coupons = np.arange(20)

user_id = np.random.choice(users, 1000)
coupon_id = np.random.choice(coupons, 1000)

year = np.random.randint(2015, 2016, 1000)
month = np.random.randint(1,12,1000)
date = np.random.randint(1, 28, 1000)

imp_data = zip(user_id, coupon_id, year, month, date)

##################################################################
# Creating a new table and populating it
##################################################################
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
#sql = """CREATE TABLE coupon_impression (
#        user_id INT,
#        coupon_id INT,
#        imp_year INT,
#        imp_month INT,
#        imp_day INT)"""

#cursor.execute(sql)

sql = "INSERT INTO coupon_impression VALUES (?,?,?,?,?)"          
cursor.executemany(sql, imp_data)
conn.commit()
conn.close()          


########################################################################
# Selecting data from the database
########################################################################
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = "SELECT * FROM coupon_impression"
cursor.execute(sql)
all_row = cursor.fetchall()

for row in all_row:
    print row

conn.close()





