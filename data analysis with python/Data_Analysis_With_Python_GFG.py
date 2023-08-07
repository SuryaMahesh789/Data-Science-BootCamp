

# Getting Started with Pandas

# Pandas is an open-source library that is built on top of NumPy library. It is a Python package that offers various data structures 
# and operations for manipulating numerical data and time series.
#  It is mainly popular for importing and analyzing data much easier. Pandas is fast and it has high-performance & productivity for users.


# Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index.
# Pandas Series is nothing but a column in an excel sheet.
# Labels need not be unique but must be a hashable type. The object supports both integer and label-based indexing and provides a host of methods for performing operations involving the index.


# Creating a Pandas Series
# In the real world, a Pandas Series will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file.
# Pandas Series can be created from the lists, dictionary, and from a scalar value etc. Series can be created in different ways, here are some ways by which we create a series:

# Creating a series from array: In order to create a series from array, we have to import a numpy module and have to use array() function.


import pandas as pd 
import numpy as np 

data=np.array(['g','e','e','k','s','f','o','r','g','e','e','k','s'])

print(data,"\n")

for i in list(data):
    print(i,end=" ")

print("\n pandas Series (from numpy array):\n")

ser=pd.Series(data)
print(ser,"\n")

print("\n pandas Series (from list):\n")

ser=pd.Series(['g','e','e','k','s','f','o','r','g','e','e','k','s'])
print(ser,"\n")


# Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure,
# i.e., data is aligned in a tabular fashion in rows and columns.
# Pandas DataFrame consists of three principal components, the data, rows, and columns.


# Creating a Pandas DataFrame
# In the real world, a Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file.
# Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc. Dataframe can be created in different ways here are some ways by which we create a dataframe:

# Creating a dataframe using List: DataFrame can be created using a single list or a list of lists.


l = ['Geeks', 'For', 'Geeks', 'is','portal', 'for', 'Geeks']

df=pd.DataFrame(l)
print("DataFrame (From List) :\n",df,"\n")


# Creating DataFrame from dict of ndarray/lists: To create DataFrame from dict of narray/list, all the narray must be of same length.
# If index is passed then the length index should be equal to the length of arrays.
# If no index is passed, then by default, index will be range(n) where n is the array length.


data = {'Name': ['Tom', 'nick', 'krish', 'jack'],'Age': [20, 21, 19, 18]}
df=pd.DataFrame(data)
print("DataFrame (From dictionary) :\n",df,"\n")


# We can delete the Dataframe using the del function

del df


# Dataset Walkthrough

# To access data from the CSV file, we require a function read_csv() that retrieves data in the form of the Dataframe.

# Syntax of read_csv() 
# Syntax: pd.read_csv(filepath_or_buffer, sep=’ ,’ , header=’infer’,  index_col=None, usecols=None, engine=None, skiprows=None, nrows=None) 

 
# Parameters: 

# filepath_or_buffer: It is the location of the file which is to be retrieved using this function. It accepts any string path or URL of the file.
# sep: It stands for separator, default is ‘, ‘ as in CSV(comma separated values).
# header: It accepts int, a list of int, row numbers to use as the column names, and the start of the data. If no names are passed, i.e., header=None, then,
#  it will display the first column as 0, the second as 1, and so on.
# usecols: It is used to retrieve only selected columns from the CSV file.
# nrows: It means a number of rows to be displayed from the dataset.
# index_col: If None, there are no index numbers displayed along with records.  
# skiprows: Skips passed rows in the new data frame.
# Read CSV using Pandas read_csv
# Before using this function, we must import the Pandas library, we will load the CSV file.

import pandas as pd 
import numpy as np 

df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")
print(df,"\n")

#headers to the dataset 
headers = ["symbolizing","normalized-losses","make","fuel-type", "aspiration", "number-of-doors",
"body-style", "drive-wheels","engine-location", "wheel-base", "length","width","height", "curb-weight",
 "engine-type", "num-of-cylinders", "engine-size","fuel-system", "bore","stroke","compression-ratio",
 "horsepower", "peak- rpm","city-mpg", "highway-mpg", "price"]

# adding headers to the dataset 
df.columns=headers

# Pandas DataFrame.columns attribute return the column labels of the given Dataframe.

# Syntax: DataFrame.columns

# Parameter : None

# Returns : column names
print(df.columns,"\n")

# f we want to see the data of a specific column we can store the dataset in a variable and print it enclosing the column name inside the square brackets.
print(df['price'])

#  we want to select multiple columns we need to give double square brackets
print(df[['number-of-doors','price']])

# Mean, median mode

# Mean

# numpy.mean(arr, axis = None) : Compute the arithmetic mean (average) of the given data (array elements) along the specified axis.

# Parameters :
# arr : [array_like]input array.
# axis : [int or tuples of int]axis along which we want to calculate the arithmetic mean. Otherwise, it will consider arr to be flattened(works on all
# the axis). axis = 0 means along the column and axis = 1 means working along the row.
# out : [ndarray, optional]Different array in which we want to place the result. The array must have the same dimensions as expected output.
# dtype : [data-type, optional]Type we desire while computing mean.

# Results : Arithmetic mean of the array (a scalar value if axis is none) or array with mean values along specified axis.


# Weighted Average
# In weighted average, each quantity is assigned a weight, which is multiplied by the quantity to calculate the average. 
# The weight assigned to these quantities can be a priority number or any other entity which describes some importance to the given quantities. 
# All the quantities while calculating the average were equal, but here in calculating the weighted average, the quantities are assigned different weights.
# For given quantities X1, X2, X3, X4, …… Xn. Each associated with weights w1, w2, w3, w4, …… wn

# Weighted Average = ( w1 × X1 + w2 × X2 + w3 × X3 + w4 × X4 +…..+ wn × Xn)/(w1 + w2 + w3 + w4 +…….+ wn)

# or

# W = ∑wi × xi/ ∑wi

# or

# W = Sum of (Product of weights with their respective quantities)/ Sum of all the weights



import pandas as pd 
import numpy as np 

arr=np.array([1,2,3,4,5])

mean=sum(arr)/len(arr)

print(arr,"\n")


print(arr.mean(),"\n")

print(mean,"\n")

print(np.mean(arr),"\n")

arr=np.array([1,2,3,4,7,9])
weight=np.array([1,2,3,4,5,6])

print(arr,"\n")

print(np.average(arr,weights=weight),"\n")

# median 

print(np.median(arr),"\n")

# Mode

# The mode is the number that occurs most often within a set of numbers. This code calculates Mode of a list containing numbers:

arr=np.array([1,2,1,1,3,2,2,2,2,2,6,7,8,8,8,10,4,7,9])

from collections import Counter

count=Counter(arr)

print("Mode: ",count.most_common(1),"\n")


# Standard Deviation and Variance

# Standard Deviation

# What is Standard Deviation?

# Standard deviation is a metric that represents the amount to which various values of a statistical series tend to fluctuate or disperse from its mean or median. It describes how the values are distributed over the data sample and is a measure of the data points’ deviation from the mean. The square root of the variance of a sample, statistical population, random variable, data collection, or probability distribution is its standard deviation.

# Standard Deviation Formula

# The formula for sample standard deviation(s) is as follows:


def standard_deviation(arr):
    mean=arr.mean()
    
    res=0
    for i in arr:
        res+=(i-mean)**2
    res=res/len(arr)
    
    res=res**(0.5)
    return res
    

arr=np.array([1,2,3,4,5])

sd=standard_deviation(arr)
 
print("standard_deviation:- ",sd,"\n")     
        
# Variance

# Variance is defined as a measure of dispersion, a metric used to assess the variability of data around an average value. It is a statistical measurement used to determine the spread of values in a data collection in relation to the average or mean value. Variance is divided into two main categories: population variance and sample variance. The population variance is used to determine how each data point in a particular population fluctuates or is spread out, while the sample variance is used to find the average of the squared deviations from the mean.

# Formula

# The variance for a data set is denoted by the symbol σ2. For population data, its formula is equal to the sum of squared differences of data entries from the mean divided by the number of entries. While for sample data, we divide the numerator value by the difference between the number of entries and unity.

# If the data set is a sample the formula of variance is given by,

# σ2 = ∑ (xi – x̄)2/(n – 1)

# where,

# x̄ is the mean of data set.

# ∑ (xi – x̄)2 is the sum of squares of difference of each observation from mean,

# n is the total number of observations.

# If we have a population data set, the formula is written as,

# σ2 = ∑ (xi – x̄)2/n


print("variance:- ",sd**(2),"\n")

# Data Preprocessing - Removing Null Value Rows

# While making a Data Frame from a csv file, many blank columns are imported as null value into the Data Frame which later creates problems while operating that data frame. Pandas isnull() and notnull() methods are used to check and manage NULL values in a data frame.
 

# Dataframe.isnull()
# Syntax: Pandas.isnull(“DataFrame Name”) or DataFrame.isnull()
# Parameters: Object to check null values for
# Return Type: Dataframe of Boolean values which are True for NaN values 
 

 

# If we add the sum function after the isnull() it will give us the total number of data which are not present or null in our dataset.

# Let us see with the help of an example.


df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data')
print(df.isnull())
print(df.isnull().sum())


# So we can see that our columns are App, Category, Rating etc. So the number which is being displayed after the column names is
#  basically the total number of null values that particular column is containing.
# So we can delete all the rows which are present in our dataframe with the help of dropna() function. Let us see the implementation of that now.


df=df.dropna()
print(df.isnull())
print(df.isnull().sum())


# So no more null values are present in any of the columns.

