import pandas as pd
print(pd.__version__)

df=pd.read_csv("G:\\MANA MINI PROJECT\DATA SET\\dataset.csv")
print(df)

d=pd.read_csv("G:\\MANA MINI PROJECT\DATA SET\\dataset.csv")
df=pd.DataFrame(d)
print(df)


di={"Name":["abc","def","ghi"],"Eoll_No":[1,2,3],"Perc":[100,90,80]}
df=pd.DataFrame(di)
print(df)



l=[("Name","Roll_No","Perc"),("abc",10,90),("def",20,100),("ghi",30,300)]
df=pd.DataFrame(l)
print(df)

d=pd.read_csv("G:\\MANA MINI PROJECT\DATA SET\\dataset.csv")
df=pd.DataFrame(d)
print(df)

print(df.head())

print(df.head(2))

print(df.head(10))

print(df.tail())

print(df.tail(2))

print(df.tail(10))

# describe about dataset
print(df.describe())

# shape
print(df.shape)

# slicing
print(df[0:10:1])


# indexing column by column

print(df["year"])


print(df["daylight"])

# indexing multiple columns
print(df[["year","holiday"]])

# indexing and slicing
print(df[["year","daylight"]][1:5:1])

# get details of individual record for all records
# for rec in df.iterrows():
#     print(rec)


# get details of individual record for 3 records
for rec in df.head(3).iterrows():
    print(rec)

# LOC [] -- stop index included

# columns are represented as column names


# get only first row
print(df.loc[1])

# get some 5th row
print(df.loc[5])

# get 10th ro
print(df.loc[10])

print(df.loc[10,"year"])

# get year value in 10th row of dataset
print(df.loc[10,["year"]])


# get 10 weekday and holiday column values of 10th row
print(df.loc[10,["weekday","holiday"]])

# from 0 to 5th row including 5
print(df.loc[0:5])

print(df.loc[0:5,"month"])

# rows start to stop but multiple columns
# range for rows but need multiple columns
print(df.loc[0:5,["month","year"]])

# range for both rows and columns
print(df.loc[0:5,"month":"rain"])

# top 3 rows with columns from month to minute
print(df.loc[0:3,"month":"minute"])

# ILOC [] -- stop index excluded
# columns are represented as column numbers

# get only row 1 using ILOC
print(df.iloc[1])

# specified row with specified column

print(df.iloc[1,1])

# one row but multiple columns
# get top 3 rows
print(df.iloc[1,[1,2,3,4,5]])

print(df.iloc[0:3])

# get top three rows but only column with index 1
print(df.iloc[0:3,1])

# get top 3 rows  1-5 columns 6th column excluded
print(df.iloc[0:3,1:6])

# top 3 rows with column 1,2,3 only
# whenever u need multiple columns specify them in list format
print(df.iloc[0:3,[1,2,3]])

# rows start to stop but multiple columns
print(df.iloc[0:3,[1,2,3,4,5]])

print(df.iloc[0:3,1:6])


# get specified rows with all columns

# top 3 rows with all column values
print(df.iloc[[1,2,3]])

# specified rows with specified columns

print(df.iloc[[1,2,3],[1,2,3,4,5]])

# all rows but specified columns

print(df.iloc[:,[1,2,3,4,5]])

# all rows but columns by given range
print(df.iloc[:,1:6])

# all rows and all columns
print(df.iloc[:])

# sort dataset by specific column name

print(df.sort_values("volume"))

print(df.sort_values("day"))

# manipulate the dataframe


# add column to dataframe
df["value"]=df["day"]+df["month"]
print(df)

# print added column in dataframe
print(df["value"])

# value column names of top 3 records
print(df["value"][0:3])

print(df["value"][1000:1003])

print(df.describe())
# drop column

print(df.drop(columns="value"))
print(df.describe())

print(df.drop(columns="value",inplace=True))
print(df.describe())

# check whether data frame is duplicated
print(df.duplicated())

# print dataframe with out dupllicates
print(df.drop_duplicates())

# to drop the duplicates permanently from the dataframe
print(df.drop_duplicates(inplace=True))

print(df)

# handling missing data


# drop unavailable rows in the dataset
print(df.dropna())
print(df)

# drop the rows permanently and updates dataframe also
df.dropna(inplace=True)
print(df)


# fill th rows with the missing values with the given default value
df.fillna(80)

# fill the rain column eith default value as 1 if it has missing data
print(df['rain'].fillna(1))


# filteringdata

# get  traffic data with volume > 1000 vehicles
print(df.loc[df['volume']>1000])


