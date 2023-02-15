"""
Name: Vedant Jain
Date: 26/11/2020 (DD/MM/YYYY)
Project: Machine Learning for Prediction
Part 4: Project Extension 2
description: This is the fourth part of my final CMPT120 Project
"""
# ----------------------------------STEP 1-------------------------------------------
from sklearn.linear_model import LinearRegression
import os.path
from turtle import Screen, Turtle

filename = input("Enter the File Name ==>")  # take input from user for file name

fileInFolder = False  # bool variable for a while loop created

while fileInFolder == False:  # while loop to check if the file in folder
    if os.path.isfile(filename + ".csv"):  # os.path used to check if file in folder
        print("File exist")
        fileInFolder = True
    else:
        filename = input("Please Enter a valid file name ==>")  # loop runs till the file is not found

file = open(filename + ".csv")  # opening the file

# assuming that there is a header
headLineAsString = file.readline()  # if yes then read the header using rad line
headLineAsList = headLineAsString.strip().split(",")
print(headLineAsList)  # TRACE

outputIndexValue = int(input("Enter the index value for output column ==>"))  # user input output index

# user input for index values of the input
inputIndexValue = input("Enter the range index value for input column (Use , between numbers i.e. 2,4) ==>")
inputIndexList = inputIndexValue.strip().split(",")  # creating a list of the index values
# print(inputIndexList)  # TRACE
inputIndex1 = int(inputIndexList[0])  # first index of the input column
inputIndex2 = int(inputIndexList[1]) + 1  # last index of the input column + 1

# print(inputIndex1)  # TRACE
# print(inputIndex2)  # TRACE

outputList = []  # output list for output values
inputListAsString = []  # input list

for i in file:  # for loop to populate the lists
    thisList = i.strip().split(",")
    outputList.append(float(thisList[outputIndexValue]))
    inputListAsString.append(thisList[inputIndex1:inputIndex2])

inputList = ([list(map(float, i)) for i in inputListAsString])  # converting all input list string to float

# print(outputList)  # TRACE
# print(inputList)  # TRACE

# ----------------------------------STEP 2-------------------------------------------

eightyPercentOut = int(len(outputList)*(80/100))  # calculating 80% of output list
eightyPercentIn = int(len(inputList)*(80/100))  # calculating 80% of input list

outputTrainingList = outputList[0:eightyPercentOut]  # creating an output training list
outputTestList = outputList[eightyPercentOut:]  # creating an output test list

inputTrainingList = inputList[0:eightyPercentIn]  # creating an input training list
inputTestList = inputList[eightyPercentIn:]  # creating an input test list

# ----------------------------------STEP 3-------------------------------------------

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=inputTrainingList, y=outputTrainingList)  # training the model

outcome = predictor.predict(X=inputTestList)  # testing the model with test input list

# calculating the percentage error with all values even if 0
allPercentList = [abs(i-j)/i*100 if i != 0 else 0 for i, j in zip(outputTestList, outcome)]

percentList = []

for i in allPercentList:  # list with non 0 values
    if i != 0:
        percentList.append(i)
print(percentList)  # TRACE

# making a dictionary to store percentage error values in different range
percentDict = {
    "10%": 0,
    "20%": 0,
    "30%": 0,
    "40%": 0,
    "50%": 0,
    "60%": 0,
    "70%": 0,
    "80%": 0,
    "90%": 0,
    "100%": 0,
    "+100%": 0
}

# checking the percentage error and adding in the dictionary
for i in percentList:
    if i <= 10.0:
        percentDict["10%"] += 1
    elif i <= 20.0:
        percentDict["20%"] += 1
    elif i <= 30.0:
        percentDict["30%"] += 1
    elif i <= 40.0:
        percentDict["40%"] += 1
    elif i <= 50.0:
        percentDict["50%"] += 1
    elif i <= 60.0:
        percentDict["60%"] += 1
    elif i <= 70.0:
        percentDict["70%"] += 1
    elif i <= 80.0:
        percentDict["80%"] += 1
    elif i <= 90.0:
        percentDict["90%"] += 1
    elif i <= 100.0:
        percentDict["100%"] += 1
    else:
        percentDict["+100%"] += 1


fontHeight = 10
fontType = ('Arial', fontHeight, 'normal')
border = 40

# ----------------------------------STEP 4-------------------------------------------
# function to draw the histogram


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


maxHeight = max(percentDict.values())  # finding the largest value in the dictionary
numBars = len(percentDict)  # length of the dictionary

screen = Screen()
screen.setworldcoordinates(-border, -border, 40 * numBars + border, maxHeight + border)


turtle = Turtle()
turtle.speed(10)  # turtle speed
turtle.fillcolor('#C4FF33')  # turtle fill colour
turtle.pensize(3)

for datum in percentDict.items():  # calling the draw histogram function for each item in the dictionary
    draw_histogram(turtle, datum)

turtle.penup()
turtle.goto((40 * numBars + border)/2, maxHeight + 10)

turtle.write("Percentage Error Histogram", font=('Arial', 20, "normal"))  # Writing the title

turtle.hideturtle()
screen.exitonclick()
