import pandas as pd

csv=pd.read_csv('data/c-test-ds.csv')

print(csv.head())

## printing the shape of the data sets
print("\n Shape of csv dataset:", csv.shape)
## printing the column names of the data sets
print("\n Column names of csv dataset:", csv.columns)
## print first 5 rows of the data sets
print("\n First 5 rows of csv dataset:")
print(csv.head())

## Some Other processing techniques discussed in the lectures.
## print the using of info() function to get the summary of the data sets
print('\n\n Some Other processing techniques discussed in the lectures.\n\n')

print("Summary of csv dataset:")
print(csv.info())

## test same for tsv dataset
tsv=pd.read_csv('data/t-test-ds.tsv', sep='\t')
print(tsv.head())
print("\n Shape of tsv dataset:", tsv.shape)
print("\n Column names of tsv dataset:", tsv.columns)
print("First 5 rows of tsv dataset:")
print(tsv.head())
print("\n Summary of tsv dataset:")
print(tsv.info())


## using dtypes() function to get the data types of tsv and csv.
print("\n Data types of tsv dataset:")
print(tsv.dtypes)
print("\n Data types of csv dataset:")
print(csv.dtypes)


##using usecols parameter to read only specific columns from the data sets
tsv_specific_cols=pd.read_csv('data/t-test-ds.tsv', sep='\t', usecols=['text'])
csv_specific_cols=pd.read_csv('data/c-test-ds.csv', usecols=['Name', 'Sex'])

print("\n Specific columns of tsv dataset:")
print(tsv_specific_cols.head())
print("\n Specific columns of csv dataset:")
print(csv_specific_cols.head())

## done