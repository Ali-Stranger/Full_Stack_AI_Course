import pandas as pd
df=pd.read_csv("D:\Full_Stack_AI\Work\week3\dataset_practice\datasets\Startups in 2021 end.csv",delimiter=",")
print(df)

#print first three rows
print(df.head(3))

# #print last three rows
print(df.tail(3))

# #counting rows and column in data frame
print(df.shape)
print(df["City"])
# #type
print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())


val=df["Valuation"]
country=df["Country"]
print(val)
print(country)

#aceessing single row using loc function
second_row=df.loc[2]
print(second_row)


#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)


second_row4 = df.loc[df['City'] == 'San Francisco']
print("#Conditional selection of rows using .loc")
print(second_row4)

#Selecting a single row using .loc
second_row5 = df.loc[:1,'Select Investors']
print("#Selecting a single column using .loc")
print(second_row5)

#Selecting a slice of rowss using .loc
second_row7 = df.loc[:5,'City':'Select Investors']
print("#Selecting a slice of columns using .loc")
print(second_row7)

#Add a New Row to a Pandas DataFrame
# add a new row
# Copy array from list and add to DataFrame

print(len(df.columns))
df.loc[len(df.index)] = [936,"Bytedance","$140","4/7/2017","China,Beijing","Artificial intelligence","Sequoia Capital China", "SIG Asia Investments", ] 
print("Modified DataFrame - add a new row:")
print(df)

# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)

#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'City': 'City_nameChanged'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'Valuation': 'Valuation_Changed'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)

#Example: Rename Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)



# select the rows where the bed is greater than 3
selected_rows = df.query('Valuation_Changed == \'Valuation_Changed\' or Valuation_Changed == "$140"')

print(selected_rows.to_string())
print(len(selected_rows))



# sort DataFrame by price in ascending order
# sorted_df = df.sort_values(by='longitude')
# print(sorted_df.to_string(index=False))


#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped = df.groupby('Valuation_Changed')['Valuation_Changed'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))

# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)

