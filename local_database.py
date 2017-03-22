# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:49:36 2017

@author: tiwarir
"""
import numpy as np


## creating the data for feeding into the data table

gender_choice = ["M", "F"]
age_choice = np.arange(10,65)
income_choice = np.arange(0,5)
first_name_choice = ["Mike", "George", "Philip", "Mark", "David", "Malcom", "Tom", "John", "Anold", "Kate", "Tom"]
last_name_choice = ["Pitt", "Clooney", "Depp", "Pacino", "Spacey", "Crowe", "Cruise", "Hanks", "Willis", "Smith"]
address_choice = ["Bedok", "Geylang", "Queenstown", "Kallang", "Bukit Merah", \
                 "Pasir Panjang", "Little India", "Boon Keng", "Buona Vista"]


gender =  np.random.choice(gender_choice, size = 15, replace = True)
age = np.random.choice(age_choice, size = 15, replace = True)
income= np.random.choice(income_choice, size = 15, replace = True)
first_name = np.random.choice(first_name_choice, size = 15, replace = True)
last_name = np.random.choice(last_name_choice, size = 15, replace = True)
address = np.random.choice(address_choice, size = 15, replace = True)
user_id = np.arange(15)

user_data = zip(user_id, first_name, age, gender, income, address)



import sqlite3
 
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()
 
# create a table
cursor.execute("""CREATE TABLE user_profile
                  (user_id INT, name text, dob INT, 
                   gender text, income_group INT,
                   address text) 
               """)
                  

# insert some data
cursor.execute("INSERT INTO user_profile VALUES (%d,%s,%d,%s,%d,%s)", (user_data[1]))
 
# save data to database
conn.commit()

sql = """
UPDATE albums 
SET artist = 'John Doe' 
WHERE artist = 'Andy Hunter'
"""
cursor.execute(sql)
conn.commit()













 
# insert multiple records using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()


                 









import sqlite3
conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print "Records created successfully";
conn.close()


conn = sqlite3.connect('test.db')
conn.close()