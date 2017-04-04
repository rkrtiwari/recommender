# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 09:08:01 2017

@author: ravitiwari
"""

###############################################################################
# Importing modules
###############################################################################
import os
import numpy as np
import json
import sqlite3


###############################################################################
# Setting up directory
###############################################################################
os.getcwd()
new_dir = os.path.join("Documents", "Python Scripts", "recommender")
os.chdir(new_dir)
os.getcwd()
os.listdir(".")

###############################################################################
# Creating json files
###############################################################################
new_user = {'user_id': 3,
             'age': 25,
             'gender': 'M',
             'income': 20000}

json_data = json.dumps(new_user)
dict_data = json.loads(json_data)

# json file with multiple user information
users = []  
user_id_max = 100
n_max = 10 
for uId in np.arange(5): 
    gender = np.random.choice(['M', 'F'])
    age    = np.random.randint(0, 100)
    income = np.random.randint(10000, 100000)

    profile = {'id': uId, 'gender': gender, 'age': age, 'income': income}
    users.append(profile)
    

json_data = json.dumps(users)





##############################################################################
# Description of user vector
##############################################################################
# no_features = 12  # Below is the explanation of all features
# age - 5 levels {0:(1-10), 1:(11-20), 2:(21-35), 3:(35-50), 4:(>50)}
# gender - 2 levels - (M->0, F->1)
# income_level - 6 levels ()
# discount - 6 levels (0->10%, 1->20%, 2->30%, 3->40%, 4->50%, 5-> >50%) 
# NEED TO CONVERT OTHER TYPES OF DISCOUNTS TO % TERM)
# dining, - 5 levels (0->chinese, 1->japanese, 2->western, 3->indian, 4->others) 
# fashion, electronics, grocery, sport, sportswear, travel, maternity - 
# ALL THESE 2 levels (0,1)


###############################################################################
# functions to update demographics 
###############################################################################
def update_age(age, value):
    if(value < 11):
        age[0] = 1
    elif(value < 21):
        age[1] = 1
    elif(value < 36):
        age[2] = 1
    elif(value < 51):
        age[3] = 1
    else:
        age[4] = 1


def update_gender(gender, value):
    if (value == 'M'):
        gender[0] = 1
    else:
        gender[1] = 1

def update_income(income, value):
    if (value < 20000):
        income[0] = 1
    elif (value < 80000):
        income[1] = 1
    else:
        income[2] = 1
        
###############################################################################
# update the values
###############################################################################
# Initialize the user vector
age = np.zeros(5)
gender = np.zeros(2)
income = np.zeros(3)

user_id = np.array([dict_data['user_id']])
update_age(age, dict_data['age'])
update_gender(gender, dict_data['gender'])
update_income(income, dict_data['income'])

user_vect = np.concatenate((user_id, age, gender, income))


###############################################################################
# update the values when there are multiple users
###############################################################################
user_data_from_json =  json.loads(json_data)

n_users = len(user_data_from_json)

for user in user_data_from_json:
    print user['id']
    print user['income']
    
age_matrix = np.zeros((n_users, 5))
gender_matrix = np.zeros((n_users, 2))
income_matrix = np.zeros((n_users, 3))

gender_values = [user['gender'] for user in user_data_from_json]
age_values = [user['age'] for user in user_data_from_json]
income_values = [user['income'] for user in user_data_from_json]
ids = [user['id'] for user in user_data_from_json]
ids = np.array(ids)
ids.shape = (-1,1)

for i in xrange(n_users):
    update_age(age_matrix[i], age_values[i])
    update_gender(gender_matrix[i], gender_values[i])
    update_income(income_matrix[i], income_values[i])
    
users_matrix = np.concatenate((ids, age_matrix, gender_matrix, income_matrix),
                              axis = 1)

###############################################################################
# Updating the database upon getting new information
###############################################################################
conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()


sql = '''  SELECT * FROM user_demographics'''
records = cursor.execute(sql)
for record in records:
    print record


sql = '''INSERT OR REPLACE INTO user_demographics VALUES
      (?,?,?,?,?,?,?,?,?,?,?)'''

cursor.executemany(sql, users_matrix)
conn.commit()
conn.close()






