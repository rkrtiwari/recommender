# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:56:23 2017

@author: ravitiwari
"""

import os
import sqlite3
import numpy as np
import pandas as pd
import json

#############################################################################
# Setting up working directory
############################################################################
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
user_id = np.arange(n_users)
user_id = user_id.reshape((-1,1))
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

user_data = np.concatenate((user_id, age, gender, income), axis = 1)

## database operation
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()

# creation of the table, done only once
sql = '''CREATE TABLE user_demographics (
        user_id INT PRIMARY KEY,
        age1 INT, age2 INT, age3 INT, age4 INT, age5 INT,
        male INT, female INT,
        income_low INT, income_medium INT, income_high INT)'''

cursor.execute(sql)

## Inserting records into the table
sql = '''INSERT INTO user_demographics VALUES
         (?,?,?,?,?,?,?,?,?,?,?)'''
         
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

# create the table, used only once
#sql = """CREATE TABLE user_preference (
#         user_id INT PRIMARY KEY,
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


##############################################################################
# reading user information from the database
###############################################################
conn = sqlite3.connect("user_info.db") 
sql1 = "SELECT * FROM user_demographics"
df1 = pd.read_sql_query(sql1, conn)
sql2 = "SELECT * FROM user_preference"
df2 = pd.read_sql_query(sql2, conn)
conn.close()

df = pd.merge(df1, df2, how = 'inner', on = 'user_id')
df.iloc[1,:]


##############################################################################
# updating the table
##############################################################################
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()


sql = '''  SELECT * FROM user_demographics'''
records = cursor.execute(sql)
for record in records:
    print record


sql = '''INSERT OR REPLACE INTO user_demographics VALUES
      (?,?,?,?,?,?,?,?,?,?,?)'''
values = np.array([(5, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1), \
          (6, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1), \
           (7, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1), \
           (8, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1)])

cursor.executemany(sql, values)
conn.commit()
conn.close()






##############################################################################
# Using json data to add/update records in the user_demographics table
###############################################################################
users = []
for uId in np.random.choice(xrange(1, 100), np.random.choice(4)):  # randomly choose 1-4 users
    # generate user profile
    gender = ['M', 'F', '-'][np.random.randint(0, 2)]
    age    = np.random.randint(-1, 6)
    income = np.random.randint(-1, 5)
    prefs  = np.random.randint(2, size=10).tolist()

    profile = {'gender': gender, 'age': age, 'income': income, 'prefs': prefs}
    users.append( {'id': uId, 'profile': profile} )

users_data = {'user': users}

json_data = json.dumps(users_data)

user_data_from_json =  json.loads(json_data)





