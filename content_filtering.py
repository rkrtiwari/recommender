# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 08:48:42 2017

@author: ravitiwari
"""

import os
import numpy as np
from scipy.spatial import distance


##############################################################################
# Setting up working directory
###############################################################################
os.getcwd()
os.chdir(os.path.join("Documents", "Python Scripts", "recommender"))
os.getcwd()
os.listdir(".")

###############################################################################
# description of the content vectors
# age - 5 levels (0-10, 11-20, 21-35, 36-50, >50)
# gender - 2 levels  (Male, Female)
# income - 3 levels  (Low, High, Medium)
# dining - 5 levels (Chinese, Japanese, Western, Indian, Others)
# fashion - 2 level
# electronics - 2 levels
# groceries - 2 levels
# sports - 2 levels
# sportswear - 2 levels
# travel - 2 levels
# maternity - 2 levels

# For representing the demographics/preference information, I am going to use 
# one hot encoding. According to this approach, a variable that has n (n>=2)
# levels can be considered to consist of n independent components. For example,
# the age variable itself become a vector with 5 independent components,
# namely [age1(0-10), age2(11-20), age3(21-35), age4(36-50), age5(>50)]. Now if 
# a user belongs in the age group of 21-35 then his vector representation will 
# become [0,0,1,0,0]. Only the third component is 1 as it represents age group
# (21-35), rest all are zero to signify that the user does not belong to those 
# categories. 
###############################################################################



##############################################################################
# User content vector generation
#############################################################################
n_users = 300
row_index = np.arange(n_users)

#age = np.zeros(5)
age = np.zeros((n_users, 5))
age_non_zero_col_index = np.random.choice(5,size = n_users, replace = True)
age[row_index, age_non_zero_col_index] = 1

gender = np.zeros((n_users, 2))
gender_non_zero_index = np.random.choice(2,size = n_users, replace = True)
gender[row_index, gender_non_zero_index] = 1

income = np.zeros((n_users, 3))
income_non_zero_index = np.random.choice(3, size = n_users, replace = True)
income[row_index, income_non_zero_index] = 1

dining = np.zeros((n_users, 5))
dining_non_zero_index = np.random.choice(5, size = n_users, replace = True)
dining[row_index, dining_non_zero_index] = 1

fashion = np.random.choice(2, size = n_users, replace = True)
fashion  = fashion[:, None]
electronics = np.random.choice(2, size = n_users, replace = True)
electronics  = electronics[:, None]
groceries = np.random.choice(2, size = n_users, replace = True)
groceries  = groceries[:, None]
sports = np.random.choice(2, size = n_users, replace = True)
sports  = sports[:, None]
sportswear = np.random.choice(2, size = n_users, replace = True)
sportswear = sportswear[:, None]
travel = np.random.choice(2, size = n_users, replace = True)
travel  = travel[:, None]
maternity = np.random.choice(2, size = n_users, replace = True)
maternity = maternity[:, None]

user_content = np.concatenate((age, gender, income, dining, fashion, \
                               electronics, groceries, sports, sportswear, \
                               travel, maternity), axis = 1)


##############################################################################
# Coupon content vector generation
#############################################################################
n_coupons = 5000
row_index = np.arange(n_coupons)

#age = np.zeros(5)
age = np.zeros((n_coupons, 5))
age_non_zero_col_index = np.random.choice(5,size = n_coupons, replace = True)
age[row_index, age_non_zero_col_index] = 1

gender = np.zeros((n_coupons, 2))
gender_non_zero_index = np.random.choice(2,size = n_coupons, replace = True)
gender[row_index, gender_non_zero_index] = 1

income = np.zeros((n_coupons, 3))
income_non_zero_index = np.random.choice(3, size = n_coupons, replace = True)
income[row_index, income_non_zero_index] = 1

dining = np.zeros((n_coupons, 5))
dining_non_zero_index = np.random.choice(5, size = n_coupons, replace = True)
dining[row_index, dining_non_zero_index] = 1

fashion = np.random.choice(2, size = n_coupons, replace = True)
fashion  = fashion[:, None]
electronics = np.random.choice(2, size = n_coupons, replace = True)
electronics  = electronics[:, None]
groceries = np.random.choice(2, size = n_coupons, replace = True)
groceries  = groceries[:, None]
sports = np.random.choice(2, size = n_coupons, replace = True)
sports  = sports[:, None]
sportswear = np.random.choice(2, size = n_coupons, replace = True)
sportswear = sportswear[:, None]
travel = np.random.choice(2, size = n_coupons, replace = True)
travel  = travel[:, None]
maternity = np.random.choice(2, size = n_coupons, replace = True)
maternity = maternity[:, None]

coupon_content = np.concatenate((age, gender, income, dining, fashion, \
                               electronics, groceries, sports, sportswear, \
                               travel, maternity), axis = 1)



#############################################################################
# distance matrix calculation
############################################################################

dist_matrix = distance.cdist(user_content, coupon_content, 'cosine')


############################################################################
# recommendation for a given user
###########################################################################
i = 2 # recommendation for user 2
user_coupon_distance = dist_matrix[i-1,:]
recommendation_order = np.argsort(user_coupon_distance) + 1
recommendation_order[:5]  # top 5 recommendation










