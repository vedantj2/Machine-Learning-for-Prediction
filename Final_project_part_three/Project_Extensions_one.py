"""
Name: Vedant Jain
Date: 26/11/2020 (DD/MM/YYYY)
Project: Machine Learning for Prediction
Part 3: Project Extension 1
description: This is the third part of my final CMPT120 Project
"""
# ----------------------------------STEP 1-------------------------------------------
from sklearn.linear_model import LinearRegression
from turtle import Screen, Turtle
import time

file = open("parkinsons_updrs.data")  # opening the data set

headLineAsString = file.readline()
headLineAsList = headLineAsString.strip().split(",")  # Making a list of the headers in the file
print("Header ==>", headLineAsList)  # TRACE

outputListAsString = []  # This is the output list as string
inputListAsString = []  # This it the input list as string

for i in file:  # For loop to make all the elements in the file into a list
    thisList = i.strip().split(",")
    outputListAsString.append(thisList[4:6])  # appending all elements in index 4 and 5 in output list
    inputListAsString.append(thisList[6:])  # appending all elements in a range of index

inputList = ([list(map(float, i)) for i in inputListAsString])  # converting the strings to float
outputList = ([list(map(float, i)) for i in outputListAsString])  # converting the strings to float

# ----------------------------------STEP 2-------------------------------------------

eightyPercentOut = int(len(outputList)*(80/100))  # calculating 80% of the output list
eightyPercentIn = int(len(inputList)*(80/100))  # calculating 80% of the input list

outputTrainingList = outputList[0:eightyPercentOut]  # Making a training output list with 80% of the first element
outputTestList = outputList[eightyPercentOut:]  # creating a Test output list with 20% of remaining elements

inputTrainingList = inputList[0:eightyPercentIn]  # Making a training input list with 80% of the first element
inputTestList = inputList[eightyPercentIn:]  # creating a Test input list with 20% of remaining elements

# Training the model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=inputTrainingList, y=outputTrainingList)

# using the model with test input
outcome = predictor.predict(X=inputTestList)
coefficient = predictor.coef_


print("Prediction :" + str(outcome))
print("Output Test List ==>", outputTestList)  # TRACE

motor_UPDRS = [i[0] for i in outcome]  # there are 2 different outputs predicted
total_UPDRS = [i[1] for i in outcome]  # there are 2 different outputs predicted

# print(motor_UPDRS)  # TRACE
# print(total_UPDRS)  # TRACE

motor_UPDRS_test = [i[0] for i in outputTestList]  # test list
total_UPDRS_test = [i[1] for i in outputTestList]  # test list 2

# print(motor_UPDRS_test)  # TRACE
# print(total_UPDRS_test)  # TRACE

# ----------------------------------STEP 3-------------------------------------------

# calculating percentage error
percentageErrorAllOne = [abs(i-j)/i*100 if i != 0 else 0 for i, j in zip(motor_UPDRS_test, motor_UPDRS)]
percentageErrorAllTwo = [abs(i-j)/i*100 if i != 0 else 0 for i, j in zip(total_UPDRS_test, total_UPDRS)]

percentListOne = []
percentListTwo = []

for i in percentageErrorAllOne:  # For loop to remove all the 0's in the list
    if i != 0:
        percentListOne.append(i)

for i in percentageErrorAllTwo:  # For loop to remove all the 0's in the list
    if i != 0:
        percentListTwo.append(i)

# Dictionary to store values
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

#  Checking elements in percent list and classifying them
for i in percentListOne:
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

# Dictionary to store values
percentDictTwo = {
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

#  Checking elements in percent list and classifying them
for i in percentListTwo:
    if i <= 10.0:
        percentDictTwo["10%"] += 1
    elif i <= 20.0:
        percentDictTwo["20%"] += 1
    elif i <= 30.0:
        percentDictTwo["30%"] += 1
    elif i <= 40.0:
        percentDictTwo["40%"] += 1
    elif i <= 50.0:
        percentDictTwo["50%"] += 1
    elif i <= 60.0:
        percentDictTwo["60%"] += 1
    elif i <= 70.0:
        percentDictTwo["70%"] += 1
    elif i <= 80.0:
        percentDictTwo["80%"] += 1
    elif i <= 90.0:
        percentDictTwo["90%"] += 1
    elif i <= 100.0:
        percentDictTwo["100%"] += 1
    else:
        percentDictTwo["+100%"] += 1

# ----------------------------------STEP 4-------------------------------------------

fontHeight = 10  # Font size
fontStyle = ('Arial', fontHeight, 'normal')
border = 40  # border spacing


def draw_histogram(t, datum):
    label, height = datum

    t.left(90)

    t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(20)
    if height > fontHeight:
        t.write(height, align="center", font=fontStyle)
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.end_fill()

    t.left(90)

    t.backward(40)
    t.forward(20)
    t.write(label, align="center", font=fontStyle)
    t.forward(20)


maxHeight = max(percentDict.values())  # getting the max value in the dictionary
numBars = len(percentDict)

screen = Screen()
screen.setworldcoordinates(-border, -border, 40 * numBars + border, maxHeight + border)

turtle = Turtle()
turtle.speed(8)
turtle.fillcolor('#02F6B0')
turtle.pensize(3)

turtle.hideturtle()

# calling the function for each element in the dictionary
for i in percentDict.items():
    draw_histogram(turtle, i)

turtle.penup()

turtle.goto(80, 270)
turtle.write("Percentage Error Histogram 1 (motor_UPDRS)", font=('Arial', 20, "normal"))

time.sleep(5)  # wait 5 seconds before clearing and drawing the second graph.

turtle.clear()

turtle.goto(0, 0)
turtle.pendown()

turtle.fillcolor('#FBFF00')

# calling the function for each element in the dictionary of second output
for i in percentDictTwo.items():
    draw_histogram(turtle, i)

turtle.penup()

turtle.goto(80, 270)
turtle.write("Percentage Error Histogram 2(total_UPDRS)", font=('Arial', 20, "normal"))

screen.exitonclick()
