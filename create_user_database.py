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

##############################################################################
# Creating user profile data base encoded as one hot vector
##############################################################################

n_users = 5
row_index = np.arange(n_users)

## creation of some fictitous data
age = np.zeros((n_users, 5))
column_index = np.random.choice(5, size = n_users, replace = True)
age[row_index, column_index] = 1

gender = np.zeros((n_users, 2))
column_index = np.random.choice(2, size = n_users, replace = True)
gender[row_index, column_index] = 1

income = np.zeros((n_users, 3))
column_index = np.random.choice(3, size = n_users, replace = True)
income[row_index, column_index] = 1

user_data = np.concatenate((age, gender, income), axis = 1)

## database operation
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()

# creation of the table, done only once
#sql = '''CREATE TABLE user_demographics (
#        age1 INT, age2 INT, age3 INT, age4 INT, age5 INT,
#        male INT, female INT,
#        income_low INT, income_medium INT, income_high INT)'''
#
#cursor.execute(sql)

## Inserting records into the table
sql = '''INSERT INTO user_demographics VALUES
         (?,?,?,?,?,?,?,?,?,?)'''
         
cursor.executemany(sql, user_data)
conn.commit()
conn.close()

## Fetching records from the table
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()
sql = '''SELECT * FROM user_demographics'''
records = cursor.execute(sql)
for record in records:
    print record





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
###############################################################################















