
"""

What is the use of pandas?
Pandas is a popular and powerful open-source library in Python for data manipulation and analysis. It offers data structures and functions that simplify working with structured data, such as tables and time series data. Here are some key uses of pandas:


1. **Data Manipulation:** Pandas provides a wide range of tools for data manipulation. You can perform tasks such as filtering, sorting, grouping, merging, and reshaping data, making it easy to clean and transform datasets.


2. **Data Cleaning:** Pandas offers functions to handle missing data, remove duplicates, and perform data imputation. It allows you to identify and handle inconsistent or erroneous data, improving data quality.


3. **Data Analysis:** Pandas provides statistical and analytical functions that facilitate data analysis. You can compute descriptive statistics, aggregate data, apply mathematical operations, and perform calculations on data columns.


4. **Time Series Analysis:** Pandas has robust support for working with time series data. It allows you to handle time-based indexing, resampling, shifting, and rolling window calculations. This makes it convenient for analyzing and modeling time-dependent data.


5. **Data Visualization:** Pandas integrates well with visualization libraries like Matplotlib and Seaborn. It provides functions to generate plots, charts, and graphs to visualize data and gain insights.


6. **Data Input/Output:** Pandas supports reading and writing data in various formats, such as CSV, Excel, SQL databases, JSON, and more. It simplifies data import and export tasks, enabling seamless integration with external data sources.


7. **Integration with Other Libraries:** Pandas seamlessly integrates with other libraries in the scientific Python ecosystem, such as NumPy, Scikit-learn, and TensorFlow. It enhances data analysis workflows by leveraging the capabilities of these libraries.


8. **Data Preprocessing for Machine Learning:** Pandas is commonly used for data preprocessing tasks in machine learning. It helps in preparing data for model training by handling missing values, encoding categorical variables, and scaling numerical features.


Overall, pandas is widely used in data science, research, finance, business analytics, and many other fields where structured data analysis is required. It simplifies data manipulation, enables efficient data exploration, and provides the foundation for data-driven decision making.


"""


"""
What is the use of numpy?

NumPy (Numerical Python) is a fundamental library in Python for scientific computing and data analysis. It provides powerful tools for working with large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. 
Efficient Array Operations: NumPy provides an ndarray object, which is an efficient container for large arrays of homogeneous data. It allows you to perform element-wise operations, array slicing, reshaping, and indexing, making it easier and faster to manipulate and process arrays compared to regular Python lists.

Numerical Computations: NumPy offers a comprehensive set of mathematical functions for array computations. These include basic mathematical operations (e.g., addition, subtraction, multiplication, division), advanced mathematical functions (e.g., trigonometric, exponential, logarithmic functions), linear algebra operations (e.g., matrix multiplication, eigenvalues, solving linear equations), and statistical functions (e.g., mean, median, standard deviation).

Data Representation: NumPy arrays are commonly used to represent and manipulate data in various scientific and numerical applications. They can store numerical data, such as sensor readings, experimental results, or image pixels, in a memory-efficient and computationally efficient manner. NumPy arrays are the foundation for many other libraries in the scientific Python ecosystem.


"""


# //getting started
print("Hello World")

# //importing pandas library using dataset online
import pandas as pd 
url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url,header=None)


# printing whole dataset 
print(df)

# head() by default returns top 5 values of the dataset
print(df.head())

# getting custom number of records from the dataset 
print(df.head(10))

print("The last 10 rows of the dataframe\n")
df.tail(10)

#headers to the dataset 
headers = ["symbolizing","normalized-losses","make","fuel-type", "aspiration", "number-of-doors",
"body-style", "drive-wheels","engine-location", "wheel-base", "length","width","height", "curb-weight",
 "engine-type", "num-of-cylinders", "engine-size","fuel-system", "bore","stroke","compression-ratio",
 "horsepower", "peak- rpm","city-mpg", "highway-mpg", "price"]

# adding headers to the dataset 
df.columns=headers

# path to save the dataset in csv file in local storage 
path="C:/Users/Mahesh/Desktop"

# save dataset in csv format in local storrage c disk 
df.to_csv(path)

# getting all the dtypes of the dataset 
# dataframe.dtypes to check the datatypes 
print(df.dtypes)

# statistical summary of the dataset is obtained from the describe function of dataframe 
# count ,mean,sum,max,min,std,25,median,75 percentiles of the dataset 
print(df.describe())

# full summary statistics of all th columns of the dataset 
# unique,top,frequency,
print(df.describe(include="all"))

# provides concise summary of the dataframe 
print(df.info())


# We can drop missing values along the column "price" as follows:
df=df1.dropna(subset=["price"], axis=0)
df.head(20)


print(df.shape())
# to drop na values 
df.dropna()
print(df.shape())

# subset to check particular column og=f the dataset 
# axis=0 drops the entire row 
# axis=1 drops th entire column 
# inplce remove the records directly in the dataset 
df.dropna(subset=["price"],axis=0,inplace=True)


# df.replace(missing_value,new_value) to replace the missing value with the new value 
# We need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df=df.replace('?',np.NaN)

missing_data=df.isnull()
missing_data.head(5)
# "True" means the value is a missing value while "False" means the value is not a missing value.

# https://labs.cognitiveclass.ai/v2/tools/jupyterlite?ulid=ulid-324a1f0dc9e0efd06c09cfc364dbfead03355a57
# Deal with missing data
# How to deal with missing data?
# Drop data
# a. Drop the whole row
# b. Drop the whole column
# Replace data
# a. Replace it by mean
# b. Replace it by frequency
# c. Replace it based on other functions

# In Pandas, we use:

# .dtype() to check the data type

# .astype() to change the data type


# let`s` see "noramalized-losses" column of the dataset to replace the missing values with the mean value of the column 
# df["particular_coumn"].mean() to obtain mean value of the column 
mean=df["normalized-losses"].mean()

# if u are unable to find the mean , follow the below one 
df["normalized-losses"] = pd.to_numeric(df["normalized-losses"], errors="coerce")
mean = df["normalized-losses"].mean()


# replace NaN values with 0 value of the data column 
df["normalized-losses"].replace(np.nan,0)


# replacing missing values with the mean of the column value in the dataset 
df["normalized-losses"].replace(np.nan,mean)


# data fromatting 
# applying calculations to the entire column of the dataset 
df["city-mpg"]=235/df["city-mpg"]


# rename the column name to new column name 
df.rename(columns={"city-mpg":"city-L/100km"},inplace=True)

# after renaming the column names , to see the column names of the data frame
import pandas as pd

# Assuming your DataFrame is named 'df'
column_names = df.columns
print(column_names)

# tail part of the dataframe only price column 
# returns the tail 5 rows values with the data type it is 
df["price"].tail()


# to know the datatypes of the columns of the data frame 
df.dtypes
print(df.dtypes)


# to convert the data type to some other astype() is used 
df[["price"]] = df[["price"]].astype("float")



# A value is trying to be set on a copy of a slice from a DataFrame," is a common warning in pandas that typically occurs
#  when trying to modify a DataFrame in a chained operation.
# To address this warning, you can use the .loc accessor to explicitly assign
#  values to a DataFrame. Here's an example:

df.loc[:, "price"] = df["price"].astype(float)


# copy the data frame for temporary use to avoid such warnings  and convert the data type to float
df_copy = df.copy()
df_copy["price"] = df_copy["price"].astype(float)
df.dtypes


# normalizing data
# 1) simple feature scaling

df["length"]=df["length"]/df["length"].max()


# 2) min max normalization

df["length"]=(df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())

# 3) z-score normalization 
df["length"]=(df["length"]-df["length"].mean())/(df["length"].std())



"""

What is the maximum value of the feature scaling?
In feature scaling, the maximum value of the scaled feature depends on the specific scaling method being used. Two commonly used scaling methods are Min-Max scaling and Standardization (Z-score scaling).
Min-Max Scaling: In Min-Max scaling, the feature values are transformed to a fixed range, typically between 0 and 1. The maximum value of the scaled feature will be 1.
Standardization (Z-score Scaling): In Standardization, the feature values are transformed to have a mean of 0 and a standard deviation of 1. Unlike Min-Max scaling, Standardization does not have a predefined maximum value since it adjusts the values based on their distribution. The maximum value in the original data may not necessarily correspond to a maximum value in the standardized data.
It's important to note that feature scaling is performed to normalize the range of feature values and does not inherently define a maximum value. The choice of scaling method depends on the specific requirements of the data and the machine learning algorithm being used.


"""


# binning - grouping values into bins 
# converting numerical values into categorical variables
# set of numerical values into a set of bins 
# columns to have a better representation

# Binning
# Why binning?
# Binning is a process of transforming continuous numerical variables into discrete categorical 'bins' for grouped analysis.

bins=np.linspace(min(df["price"]),max(df["price"]),4)
group_names=["Low","Medium","High"]

df["price-binned"]=pd.cut(df["price"],bins,labels=group_names,include_lowest=True)

# try this to binn the price column into price-ninned column into th data frame 
df.loc[:, "price-binned"] = pd.cut(df["price"],bins,labels=group_names,include_lowest=True)

# new column price-binned added into the data frame 
# check using df.columns 

df.columns

# turning categorical values into numerical values 
# python dummies helps to convert it.

# Indicator Variable (or Dummy Variable)
# What is an indicator variable?
# An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.

# Why we use indicator variables?

# We use indicator variables so we can use categorical variables for regression analysis in the later modules.

# Example
# We see the column "fuel-type" has two unique values: "gas" or "diesel". Regression doesn't understand words, only numbers. To use this attribute in regression analysis, we convert "fuel-type" to indicator variables.

# We will use pandas' method 'get_dummies' to assign numerical values to different categories of fuel type.

pd.get_dummies(df['fuel-type'])

# Week-3 explorativbe Data Analysis

df.describe()
df.describe(include="all")

drive_wheels_counts=df["drive-wheels"].value_counts().to_frame()

drive_wheels_counts.rename(columns={'drive-wheels':'value_counts'},inplace=True)
drive_wheels_counts

sns.boxplot(x="drive-wheels",y="price",data=df)

import matplotlib as plt 
x=df["engine-size"]
y=df["price"]

plt.scatter(x,y)

plt.title("Scatterplot of Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")


# Groupby()

df_test=df[['drive-wheels','body-style','price']]
df_grp=df_test.groupby(['drive-wheels','body-style'],as_index=False).mean()
df_grp


df_pivot=df_grp.pivot

non_numeric_prices = df[~df['price'].str.isnumeric()]['price']
print(non_numeric_prices.unique())
df['price'] = df['price'].str.replace(r'[^0-9]', '').astype(float)
df['price'] = df['price'].str.replace(r'[^0-9]', '')



# converting price strings ti numeric float values 
import pandas as pd

# Assuming df['price'] is of type 'str'
# Convert the 'price' column to a numeric type (e.g., float)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Now, you can safely calculate the mean of the 'price' column
price_mean = df['price'].mean()

# Display the mean value
print(price_mean)


# Select the columns 'drive-wheels', 'body-style', and 'price' from the DataFrame
df_test = df[['drive-wheels', 'body-style', 'price']]

# Group the data based on 'drive-wheels' and 'body-style' and calculate the mean of 'price'
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()


# pivot 
df_pivot=df_grp.pivot(index='drive-wheels',columns='body-style')
df_pivot

df.dtypes

df['peak-rpm'].dtypes

df[["engine-size", "price"]].corr()



"""
5. Correlation and Causation
Correlation: a measure of the extent of interdependence between variables.

Causation: the relationship between cause and effect between two variables.

It is important to know the difference between these two. Correlation does not imply causation.
 Determining correlation is much simpler the determining causation as causation may require independent 
 experimentation.

Pearson Correlation

The Pearson Correlation measures the linear dependence between two variables X and Y.

The resulting coefficient is a value between -1 and 1 inclusive, where:

1: Perfect positive linear correlation.
0: No linear correlation, the two variables most likely do not affect each other.
-1: Perfect negative linear correlation.
Pearson Correlation is the default method of the function "corr". Like before, we can calculate the 
Pearson Correlation of the of the 'int64' or 'float64' variables.

"""


"""
Link For Lab Sessions
https://labs.cognitiveclass.ai/v2/tools/jupyterlite?ulid=ulid-002d789a21c7c50d66520997acc642b889321038

"""

import seaborn as sns 
residplot=sns.residplot(df['highway-mpg'],df['price'])
print(residplot)


# 1. Linear Regression and Multiple Linear Regression
# Linear Regression
# One example of a Data Model that we will be using is:

# Simple Linear Regression
# Simple Linear Regression is a method to help us understand the relationship between two variables:

# The predictor/independent variable (X)
# The response/dependent variable (that we want to predict)(Y)
# The result of Linear Regression is a linear function that predicts the response (dependent) variable as a function of the predictor (independent) variable.

# Linear Function

 
# a refers to the intercept of the regression line, in other words: the value of Y when X is 0
# b refers to the slope of the regression line, in other words: the value with which Y changes when X increases by 1 unit1. Linear Regression and Multiple Linear Regression
# Linear Regression
# One example of a Data Model that we will be using is:

# Simple Linear Regression
# Simple Linear Regression is a method to help us understand the relationship between two variables:

# The predictor/independent variable (X)
# The response/dependent variable (that we want to predict)(Y)
# The result of Linear Regression is a linear function that predicts the response (dependent) variable as a function of the predictor (independent) variable.

# Linear Function

 
# a refers to the intercept of the regression line, in other words: the value of Y when X is 0
# b refers to the slope of the regression line, in other words: the value with which Y changes when X increases by 1 unit



# load modules for linear regression

from sklearn.linear_model import LinearRegression

# Create the linear regression object:
lm=LinearRegression()

print(lm)


# For this example, we want to look at how highway-mpg can help us predict car price. 
# Using simple linear regression, we will create a linear function with 
# "highway-mpg" as the predictor variable and the "price" as the response variable.

# x = predictor variable, independent variable,feature,input
# y = response variable, dependent variable, label , output


X = df[['highway-mpg']]
Y = df['price']

lm.fit(X,Y)

# predicted values into Yhat 

Yhat=lm.predict(X)
print(Yhat)
Yhat[0:5]

print(Yhat[0:5])

# as we are currently using simple linear regression , linear mathematical equation 
# with intercept,coefficient

print(lm.intercept_)
print(lm.coef_)


# final estimated linear model 

# Yhat=a+bX 


# <p>What if we want to predict car price using more than one variable?</p>

# <p>If we want to use more variables in our model to predict car price,
# we can use <b>Multiple Linear Regression</b>.
# Multiple Linear Regression is very similar to Simple Linear Regression,
# but this method is used to explain the relationship between one continuous response (dependent) variable and <b>
# two or more</b> predictor (independent) variables.
# Most of the real-world regression models involve multiple predictors.We will illustrate the structure by using four predictor variables, but these results can generalize to any integer:</p>

# From the previous section we know that other good predictors of price could be:

# Horsepower
# Curb-weight
# Engine-size
# Highway-mpg
# Let's develop a model using these variables as the predictor variables.

# multiple independent variables 
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])

print(lm.intercept_)
print(lm.coeff_)


# Regression Plot
# When it comes to simple linear regression, an excellent way to visualize the fit of our model is by using regression plots.

# This plot will show a combination of a scattered data points (a scatterplot), as well as the fitted linear regression line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).

# Let's visualize highway-mpg as potential predictor variable of price:


width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)

# We can see from this plot that price is negatively correlated to highway-mpg since the regression slope is negative.

# One thing to keep in mind when looking at a regression plot is to pay attention to how scattered the data points are around the regression line. This will give you a good indication of the variance of the data and whether a linear model would be the best fit or not. If the data is too far off from the line, this linear model might not be the best model for this data.

# Let's compare this plot to the regression plot of "peak-rpm".


plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

# Comparing the regression plot of "peak-rpm" and "highway-mpg", we see that the points for "highway-mpg" are much closer to the generated line and, on average, decrease. The points for "peak-rpm" have more spread around the predicted line and it is much harder to determine
# if the points are decreasing or increasing as the "peak-rpm" increases.

# Residual Plot
# A good way to visualize the variance of the data is to use a residual plot.

# What is a residual?

# The difference between the observed value (y) and the predicted value (Yhat) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.

# So what is a residual plot?

# A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.

# What do we pay attention to when looking at a residual plot?

# We look at the spread of the residuals:

# - If the points in a residual plot are randomly spread out around the x-axis, then a linear model is appropriate for the data.

# Why is that? Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data.


width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'],y=df['price'])
plt.show()


# What is this plot telling us?

# We can see from this residual plot that the residuals are 
# not randomly spread around the x-axis, leading us to believe that maybe a non-linear model is more appropriate for this data.

# Multiple Linear Regression¶
# How do we visualize a model for Multiple Linear Regression? This gets a bit more complicated because you can't visualize it with regression or residual plot.

# One way to look at the fit of the model is by looking at the distribution plot. We can look at the distribution of the fitted values that result from the model and compare it to the distribution of the actual values.

# First, let's make a prediction:

plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()



# we can easily find the MSE using scikit learn library 

from sklearn.metrics import mean_squared_error 

Y_predict_simple_fit=Yhat
mean_squared_error(df['price'],Y_predict_simple_fit)

mse=mean_squared_error(df['price'],Y_predict_simple_fit)

print(mse)


# R-squared/R^2 

# coefficient of determination
# determines how close the data is to the fitted regression line 

X = df[['highway-mpg']]
Y = df['price']

lm.fit(X,Y)

lm.score(X,Y)

r2score=lm.score(X,Y)

print(r2score)




