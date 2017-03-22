# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:49:36 2017

@author: tiwarir
"""
import numpy as np
import sqlite3
import os

os.getcwd()
os.chdir(os.path.join(os.getcwd(), "Documents", "Python Scripts", "recommender"))
os.getcwd()
#########################################################################################
## creating fictitious data for feeding into the data table
###########################################################################################
gender_choice = ["M", "F"]
age_choice = np.arange(10,65)
income_choice = np.arange(0,5)
first_name_choice = ["Mike", "George", "Philip", "Mark", "David", "Malcom", "Tom", "John", "Anold", "Kate", "Tom"]
last_name_choice = ["Pitt", "Clooney", "Depp", "Pacino", "Spacey", "Crowe", "Cruise", "Hanks", "Willis", "Smith"]
address_choice = ["Bedok", "Geylang", "Queenstown", "Kallang", "Bukit Merah", \
                 "Pasir Panjang", "Little India", "Boon Keng", "Buona Vista"]


np.random.seed(10)
gender =  np.random.choice(gender_choice, size = 15, replace = True)
age = np.random.choice(age_choice, size = 15, replace = True)
income= np.random.choice(income_choice, size = 15, replace = True)
first_name = np.random.choice(first_name_choice, size = 15, replace = True)
last_name = np.random.choice(last_name_choice, size = 15, replace = True)
address = np.random.choice(address_choice, size = 15, replace = True)
user_id = np.arange(15)

user_data = zip(user_id, first_name, age, gender, income, address)
user_data[1]
##############################################################################################
# Creating database connection, and adding records to database
############################################################################################## 
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()
 
# create a table
cursor.execute("""CREATE TABLE user_profile
                  (user_id INT, name text, dob INT, 
                   gender text, income_group INT,
                   address text) 
               """)
                  

# insert some data
cursor.execute("INSERT INTO user_profile VALUES (1, 'Anold', 10, 'F', 4, 'Little India')")
cursor.execute("INSERT INTO user_profile VALUES (?, ?, ?, ?, ?, ?)", (2, 'Kate', 52, 'M', 1, 'Geylang'))
cursor.execute("INSERT INTO user_profile VALUES (?, ?, ?, ?, ?, ?)", user_data[3])
cursor.executemany("INSERT INTO user_profile VALUES (?,?,?,?,?,?)", user_data[4:])

conn.commit()
conn.close()

###################################################################################################################### 
# sql query
#################################################################################################

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = "SELECT * FROM user_profile WHERE user_id=1"
cursor.execute(sql)
print cursor.fetchall()
conn.close()

#####################################################################################
# updating the record based on some condition
#####################################################################################
##Example 1
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = """UPDATE user_profile
         SET name = 'Arnold'
         WHERE name == 'Anold'"""
cursor.execute(sql)
conn.commit()
conn.close()

##Example 2
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
sql = """UPDATE user_profile
         SET name = 'Tiger'
         WHERE user_id == 14"""
cursor.execute(sql)
conn.commit()
conn.close()

##Example3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
newaddress = 'Bukit Panjang'
user_id = 7
sql = """UPDATE user_profile SET address = ? WHERE user_id == ?"""
cursor.execute(sql, (newaddress, user_id))
conn.commit()
conn.close()


###############################################################################
# deleting record
###############################################################################
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
delete_userid = 2
sql = """DELETE FROM user_profile WHERE user_id == ?"""
cursor.execute(sql, (delete_userid,))  # the comma at the end of the delete_userid
                                       # is required otherwise it will not work 
conn.commit()
conn.close() 














