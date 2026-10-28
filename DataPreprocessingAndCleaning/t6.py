import pandas as pd

csv=pd.read_csv('data/c-test-ds.csv')

# Handle missing values:
# Numerical → median
# Categorical → Unknown

## Identify numerical and categorical columns.
print("\n Missing values before handling all columns:")
print(csv.isnull().sum())

numerical_columns = csv.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = csv.select_dtypes(include=['object']).columns

for col in numerical_columns:
    if csv[col].isnull().sum() > 0:
        median_value = csv[col].median()
        csv[col].fillna(median_value, inplace=True)

for col in categorical_columns:
    if csv[col].isnull().sum() > 0:
        csv[col].fillna("Unknown", inplace=True)

print("\n Missing values after handling all columns:")
print(csv.isnull().sum())

## Test for Remove duplicate rows (if any)
csv.drop_duplicates(inplace=True)

## Rename columns to lowercase and snake_case.
print("\n Columns before renaming:")
print(csv.columns)
print("\n Renaming columns to lowercase and snake_case.")
print(csv.columns.str.lower().str.replace(' ', '_'))

## Fix incorrect data types
csv['Date'] = pd.to_datetime(csv['Date'], errors='coerce')
csv['Ticket'] = pd.to_numeric(csv['Ticket'], errors='coerce')
csv['Age'] = csv['Age'].astype('float32')

print(csv.info())

#### done
