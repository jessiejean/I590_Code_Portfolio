#Get basic information of dataset including: count, mean, std, min, 25%, 50%, 75%, max
df.describe()

#Group values together and show size or description of each group
df.groupby(by =[‘class’, ‘doctor_name’]).size()
df.groupby(by =[‘class’, ‘doctor_name’]).describe()

#Get type and other info of a df
df.info()

#Deal with missing values - sum the total of missign values
df.isna().sum()

#Find number of unique values in each column
df.nunique()




#Source: https://towardsdatascience.com/data-wrangling-with-pandas-5b0be151df4e
#Source: https://www.earthdatascience.org/courses/earth-analytics-bootcamp/data-wrangling/data-wrangling-pandas/
