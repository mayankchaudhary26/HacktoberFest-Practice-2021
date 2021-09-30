from sklearn.linear_model import LinearRegression

import pandas

import numpy

# reading the data from the file 
dataset = pandas.read_csv("data.csv") # you can replace the data from the big data 
Hrs = int(input(("Enter no. of hours you study : ")))
print("data we have :\n",dataset)

y = dataset["marks"]
x = dataset["hrs"]

x = x.values.reshape(-1,1)
model = LinearRegression()
model.fit(x,y)

print("Model predcted marks  : ",model.predict([[Hrs]])[0]) # no of hours will give us the marks 

"""
OUTPUT :

Enter no. of hours you study : 4
data we have :
    hrs  marks
0    2     20
1    3     30
2    7     80
3    9     90
Model predcted marks  :  41.83206106870229

"""
