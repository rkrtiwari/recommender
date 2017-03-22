# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:09:41 2017

@author: tiwarir
"""

import numpy as np
import pandas as pd
import os

os.getcwd()
os.listdir(".")

rating_matrix = pd.DataFrame(np.random.rand(5,4), columns = ["A", "B","C", "D"],
                             index = ["a", "b", "c", "d", "e"])
rating_matrix.to_csv("rating_matrix.csv")

rating_matrix_2 = pd.read_csv("rating_matrix.csv", header = 0, index_col = 0)
print(rating_matrix_2)

rating_matrix_2.loc["a", "B"] = 20
rating_matrix_2.index
rating_matrix_2.columns

rating_matrix_2.to_csv("rating_matrix.csv")






