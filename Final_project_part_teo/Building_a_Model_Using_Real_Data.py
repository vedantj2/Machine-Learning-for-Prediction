"""
Name: Vedant Jain
Date: 26/11/2020 (DD/MM/YYYY)
Project: Machine Learning for Prediction
Part 2: Building a Model Using Real Data
description: This is the second part of my final CMPT120 Project
"""
# ----------------------------------STEP 1-------------------------------------------
from sklearn.linear_model import LinearRegression
from turtle import Screen, Turtle

file = open("SeoulBikeData.csv")  # Opening the dataset

headLineAsString = file.readline()
headLineAsList = headLineAsString.strip().split(",")  # Making a list of the headers in the file
print(headLineAsList)

outputList = []  # This is the main output list
inputListAsString = []  # this is a lit of all the input

for i in file:  # For loop to make all the elements in the file into a list
    thisList = i.strip().split(",")
    outputList.append(float(thisList[1]))  # appending all elements in index 1 in output list
    inputListAsString.append(thisList[2:11])  # appending all elements in a range of index.

inputList = ([list(map(float, i)) for i in inputListAsString])  # Making a input string list to input float list

# ----------------------------------STEP 2-------------------------------------------

eightyPercentOut = int(len(outputList) * (80 / 100))  # calculating 80% of the output list
eightyPercentIn = int(len(inputList) * (80 / 100))  # calculating 80% of the input list

outputTrainingList = outputList[0:eightyPercentOut]  # Making a training list with 80% of the first element
outputTestList = outputList[eightyPercentOut:]  # creating a Test output list with 20% of remaining elements

inputTrainingList = inputList[0:eightyPercentIn]  # Making a training list with 80% of the first element
inputTestList = inputList[eightyPercentIn:]  # creating a Test input list with 20% of remaining elements

# print(inputTestList[0]) TRACE

# Training the model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=inputTrainingList, y=outputTrainingList)

# using the model with test input
outcome = predictor.predict(X=inputTestList)
coefficient = predictor.coef_

print("Prediction :" + str(outcome))
print("Coefficient:" + str(coefficient))

# ----------------------------------STEP 3-------------------------------------------

# calculating the percentage error for all values
percentageErrorAll = [abs(i - j) / i * 100 if i != 0 else 0 for i, j in zip(outputTestList, outcome)]

percentList = []

for i in percentageErrorAll:  # For loop to remove all the 0's in the list
    if i != 0:
        percentList.append(i)
print("Percentage Error List ==>", percentList)  # TRACE

# Dictionary to store values
percentDict = {
    "<=10%": 0,
    "<=20%": 0,
    "<=30%": 0,
    "<=40%": 0,
    "<=50%": 0,
    "<=60%": 0,
    "<=70%": 0,
    "<=80%": 0,
    "<=90%": 0,
    "<=100%": 0,
    ">=100%": 0
}

#  Checking elements in percent list and classifying them
for i in percentList:
    if i <= 10.0:
        percentDict["<=10%"] += 1
    elif i <= 20.0:
        percentDict["<=20%"] += 1
    elif i <= 30.0:
        percentDict["<=30%"] += 1
    elif i <= 40.0:
        percentDict["<=40%"] += 1
    elif i <= 50.0:
        percentDict["<=50%"] += 1
    elif i <= 60.0:
        percentDict["<=60%"] += 1
    elif i <= 70.0:
        percentDict["<=70%"] += 1
    elif i <= 80.0:
        percentDict["<=80%"] += 1
    elif i <= 90.0:
        percentDict["<=90%"] += 1
    elif i <= 100.0:
        percentDict["<=100%"] += 1
    else:
        percentDict[">=100%"] += 1

# ----------------------------------STEP 4-------------------------------------------

fontHeight = 10  # Font size
fontType = ('Arial', fontHeight, 'normal')
border = 40  # border spacing


def draw_histogram(t, datum):
    label, height = datum

    t.left(90)

    t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(20)
    if height > fontHeight:
        t.write(height, align="center", font=fontType)
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.end_fill()

    t.left(90)

    t.backward(40)
    t.forward(20)
    t.write(label, align="center", font=fontType)
    t.forward(20)


maxHeight = max(percentDict.values())  # getting the max value in the dictionary
numBars = len(percentDict)  # getting the length of the dictionary

screen = Screen()
screen.setworldcoordinates(-border, -border, 40 * numBars + border, maxHeight + border)  # making a screen

turtle = Turtle()
turtle.speed(10)
turtle.fillcolor('#C4FF33')
turtle.pensize(3)

# calling the function for each element in the dictionary
for i in percentDict.items():
    draw_histogram(turtle, i)

turtle.penup()

turtle.goto(130, 270)

turtle.write("Percentage Error Histogram", font=('Arial', 20, "normal"))  # writing the title

turtle.hideturtle()
screen.exitonclick()  # Program ends when clicked in the turtle screen
