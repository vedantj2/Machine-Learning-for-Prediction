"""
Name: Vedant Jain
Date: 26/11/2020 (DD/MM/YYYY)
Project: Machine Learning for Prediction
Part 1: Building our first Machine Learning Model
description: This is the first part of my final CMPT120 Project
"""
import random
from sklearn.linear_model import LinearRegression

mainList = []  # Creating an empty input list
for j in range(0, 100):
    randomList = []  # To create a 2D list
    for k in range(0, 3):  # To populate the random list with 3 elements
        randomNums = random.randint(0, 1000)  # randint used to select a random number between 0-1000
        randomList.append(randomNums)  # Making a list of 3 elements
    mainList.append(randomList)  # appending the list with 3 elements to the Main input list

print("TRACE Main List ==>", mainList)  # Printing the main list to check

totalList = []  # Empty output list

# Calculating the output using the input list
for i in range(0, 100):
    total = 0
    for j in range(0, 3):
        a = mainList[i][j]  # Obtaining the value in the input list
        # Trace print(a, "<== this is a")
        # Trace print(j+1, "<== this is j")
        total = total + (j+1)*a  # calculating the answer
    # Trace print(total)
    totalList.append(total)  # appending to the output list
print("TRACE Answers List ==>", totalList)

# Training the machine learning model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=mainList, y=totalList)

# Using our model for prediction
X_test = [[10, 20, 30]]
outcome = predictor.predict(X=X_test)
coefficient = predictor.coef_

# Printing the result
print("Prediction :" + str(outcome))
print("Coefficient:" + str(coefficient))
