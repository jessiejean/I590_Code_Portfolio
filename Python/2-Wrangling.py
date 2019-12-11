#Get basic information of dataset including: count, mean, std, min, 25%, 50%, 75%, max
df.describe()

#Get type and other info of a df
df.info()

#Deal with missing values - sum the total of missign values
df.isna().sum()

#Find number of unique values in each column
df.nunique()

#Group variables together and show size or description of each group
df.groupby(by =[‘class’, ‘doctor_name’]).size()
df.groupby(by =[‘class’, ‘doctor_name’]).describe()

#Merge two dataframes with both the left and right dataframes using the subject_id key
pd.merge(df_new, df_n, left_on='subject_id', right_on='subject_id')

#Merge with outer join produces the set of all records in Table A and Table B, with matching records 
#from both sides where available. If there is no match, the missing side will contain null.”
pd.merge(df_a, df_b, on='subject_id', how='outer')

#Merge with inner join produces only the set of records that match in both Table A and Table B
pd.merge(df_a, df_b, on='subject_id', how='inner')

#Merge with right join
pd.merge(df_a, df_b, on='subject_id', how='right')

#Concatenate data by combining two datasets together
x = [1, 2, 3]
y = [4, 5, 6]
pd.concat([x, y])


#Source: https://towardsdatascience.com/data-wrangling-with-pandas-5b0be151df4e
#Source: https://www.earthdatascience.org/courses/earth-analytics-bootcamp/data-wrangling/data-wrangling-pandas/
#Source: https://www.tutorialspoint.com/python_data_science/python_data_wrangling.htm
