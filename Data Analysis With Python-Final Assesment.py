# Data Analysis with Python
# House Sales in King County, USA
# This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.
#
# id : A notation for a house
#
# date: Date house was sold
#
# price: Price is prediction target
#
# bedrooms: Number of bedrooms
#
# bathrooms: Number of bathrooms
#
# sqft_living: Square footage of the home
#
# sqft_lot: Square footage of the lot
#
# floors :Total floors (levels) in house
#
# waterfront :House which has a view to a waterfront
#
# view: Has been viewed
#
# condition :How good the condition is overall
#
# grade: overall grade given to the housing unit, based on King County grading system
#
# sqft_above : Square footage of house apart from basement
#
# sqft_basement: Square footage of the basement
#
# yr_built : Built Year
#
# yr_renovated : Year when house was renovated
#
# zipcode: Zip code
#
# lat: Latitude coordinate
#
# long: Longitude coordinate
#
# sqft_living15 : Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area
#
# sqft_lot15 : LotSize area in 2015(implies-- some renovations)
#
# You will require the following libraries:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
# %matplotlib inline

# Module 1: Importing Data Sets
# Load the csv:
file_name='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/kc_house_data_NaN.csv'
df=pd.read_csv(file_name)
# We use the method head to display the first 5 columns of the dataframe.
print(df.head())

# Question 1 # Display the data types of each column using the attribute dtype, then take a screenshot and submit it, include your code in the image.

print(df.dtypes)

print(df.describe())

# Module 2: Data Wrangling
# Question 2
# Drop the columns "id" and "Unnamed: 0" from axis 1 using the method drop(), then use the method describe() to obtain a statistical summary of the data.
#

df.drop("id", axis = 1, inplace = True)
df.drop("Unnamed: 0", axis = 1, inplace = True)

print(df.describe())

# We can see we have missing values for the columns  bedrooms and  bathrooms

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())


# number of NaN values for the column bedrooms : 13
# number of NaN values for the column bathrooms : 10
# We can replace the missing values of the column 'bedrooms' with the mean of the column 'bedrooms'  using the method replace().
# Don't forget to set the inplace parameter to True


mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)

# We also replace the missing values of the column 'bathrooms' with the mean of the column 'bathrooms'  using the method replace().
# Don't forget to set the  inplace  parameter top  True

mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull())

# number of NaN values for the column bedrooms : 0
# number of NaN values for the column bathrooms : 0

# Module 3: Exploratory Data Analysis
# Question 3
# Use the method value_counts to count the number of houses with unique floor values, use the method .to_frame() to convert it to a dataframe.

print(df['floors'].value_counts().to_frame())

# Question 4
# Use the function boxplot in the seaborn library to determine whether houses with a waterfront view or without a waterfront view have more price outliers.

print(sns.boxplot(x="waterfront", y="price", data=df))

# Question 5
# Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price.

print(sns.regplot(x="sqft_above", y="price", data=df, ci = None))

# We can use the Pandas method corr() to find the feature other than price that is most correlated with price.

print(df.corr()['price'].sort_values())

# Module 4: Model Development
# We can Fit a linear regression model using the longitude feature 'long' and caculate the R^2.

X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

print(lm.score(X, Y))


# Question 6
# Fit a linear regression model to predict the 'price' using the feature 'sqft_living' then calculate the R^2. Take a screenshot of your code and the value of the R^2.

X1 = df[['sqft_living']]
Y1 = df['price']
lm = LinearRegression()
lm
lm.fit(X1,Y1)
lm.score(X1, Y1)
print(lm.score(X1, Y1))

# Question 7
# Fit a linear regression model to predict the 'price' using the list of features:

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
# Then calculate the R^2. Take a screenshot of your code.

X2 = df[features]
Y2 = df['price']
lm.fit(X2,Y2)
lm.score(X2,Y2)
print(lm.score(X2,Y2))

# This will help with Question 8
# Create a list of tuples, the first element in the tuple contains the name of the estimator:

# 'scale'
#
# 'polynomial'
#
# 'model'

# The second element in the tuple contains the model constructor

StandardScaler()

PolynomialFeatures(include_bias=False)

LinearRegression()

Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]

#
# Question 8
# Use the list to create a pipeline object to predict the 'price', fit the object using the features in the list features, and calculate the R^2.

pipe=Pipeline(Input)
print(pipe)
X = df[features]
Y = df['price']
pipe.fit(X,Y)
print(pipe.score(X,Y))

# Module 5: Model Evaluation and Refinement
# Import the necessary modules:

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
print("done")
# done
# We will split the data into training and testing sets:

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])
# number of test samples: 3242
# number of training samples: 18371
# Question 9
# Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data.

from sklearn.linear_model import Ridge
RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train, y_train)
RidgeModel.score(x_test, y_test)
0.6478759163939122

# Question 10
# Perform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided. Take a screenshot of your code and the R^2.

pr = PolynomialFeatures(degree = 2)
x_train_pr = pr.fit_transform(x_train[features])
x_test_pr = pr.fit_transform(x_test[features])

RidgeModel1 = Ridge(alpha = 0.1)
RidgeModel1.fit(x_train_pr, y_train)
print(RidgeModel1.score(x_test_pr, y_test))