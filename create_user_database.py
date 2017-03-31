# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:56:23 2017

@author: ravitiwari
"""

import os
import sqlite3
import numpy as np
os.getcwd()
os.chdir(os.path.join("Documents", "Python Scripts", "recommender"))
os.listdir(".")


###############################################################################
# create user demographics database
###############################################################################
n_users = 5

gender_choice = ["M", "F"]
age_choice = np.arange(1,100)
income_choice = np.arange(1,4)


np.random.seed(10)
gender =  np.random.choice(gender_choice, size = n_users, replace = True)
age = np.random.choice(age_choice, size = n_users, replace = True)
income= np.random.choice(income_choice, size = n_users, replace = True)
user_id = np.arange(n_users)

user_data = zip(user_id, age, gender, income)

conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()

# table creation, need to do it only once
#sql = """CREATE TABLE user_profile (
#         user_id INT,
#         gender text,
#         age INT,
#         income INT)"""
#
#cursor.execute(sql)

# populating the table
sql = """INSERT INTO user_profile VALUES 
         (?,?,?,?)"""

cursor.executemany(sql, user_data)
conn.commit()
conn.close()

# querying the table and printing the result
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()
sql = """ SELECT * FROM user_profile"""
records = cursor.execute(sql)
for record in records:
    print(record)
conn.close()


###############################################################################
# create user preference database
###############################################################################

## Creating random data to populate the table
n_users = 5
#np.random.seed(1)  # use this for creating reproducible records
choices = np.arange(2)

chinese = np.random.choice(choices, size = n_users, replace = True)
japanese = np.random.choice(choices, size = n_users, replace = True)
western = np.random.choice(choices, size = n_users, replace = True)
indian = np.random.choice(choices, size = n_users, replace = True)
others = np.random.choice(choices, size = n_users, replace = True)
fashion = np.random.choice(choices, size = n_users, replace = True)
electronics = np.random.choice(choices, size = n_users, replace = True)
grocery = np.random.choice(choices, size = n_users, replace = True)
sports = np.random.choice(choices, size = n_users, replace = True)
sportswear = np.random.choice(choices, size = n_users, replace = True)
travel = np.random.choice(choices, size = n_users, replace = True)
maternity = np.random.choice(choices, size = n_users, replace = True)
user_id = np.arange(n_users)


user_data = zip(user_id, chinese, japanese, western, indian, others, fashion,
                electronics, grocery, sports, sportswear, travel, maternity)

conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()

## create the table, used only once
#sql = """CREATE TABLE user_preference (
#         user_id INT,
#         chinese INT, japanese INT, western INT, indian INT, others INT, 
#         fashion INT,
#         electronics INT,
#         grocery INT,
#         sports INT,
#         sportswear INT,
#         travel INT,
#         maternity INT)"""
#
#cursor.execute(sql)


## insert records in the data base
sql = """INSERT INTO user_preference VALUES 
         (?,?,?,?,?,?,?,?,?,?,?,?,?)"""

cursor.executemany(sql, user_data)
conn.commit()
conn.close()

## querying the database
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()
sql = "SELECT * FROM user_preference"
records = cursor.execute(sql)
for record in records:
    print record
    
conn.close()
















