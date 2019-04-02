#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:10:10 2019

@author: haodongwu
"""



from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import numpy as np
file = open("try.txt","r")
data = file.read()
file.close()

allpoints = data.split("\n")
difference_list = []

points_list = list(map(float,allpoints))

group_num = 1

for i in range(0, len(points_list), 30):
    group = points_list[i:i + 30]
    first_ten = group[0:10]
    last_ten = group[20:30]
    last_ten_x_value = np.arange(i+21,i+31)
    
    #generate the list of x-axis of the data
    x_list = np.arange(i+1,i+11)
    df_x = []
    for i in x_list:
        df_x.append([i])
    
    
    df_y = []
    for j in first_ten:
        df_y.append([j])
        
    lm = linear_model.LinearRegression()
    x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size = 0.2, random_state = 4)
    model = lm.fit(x_train,y_train)
    k = lm.coef_
    b = lm.intercept_

    average = sum(last_ten) / len(last_ten)
    
    middle_of_last_ten = last_ten_x_value[4] + 0.5
    print("The average of the last ten value in group%d is %f " %(group_num,average))
    predict = (k*middle_of_last_ten) + b
    print("Predicted Value is %f" %predict)
    difference = average - predict
    print("Difference is %f \n\n" %difference)
    difference_list.append(difference)

    group_num +=1
    
with open ("results.txt","w") as f:
    for item in difference_list:
        f.write("%f\n" % item)
        
    
    
    
    
    
