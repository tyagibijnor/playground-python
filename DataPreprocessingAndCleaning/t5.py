import pandas as pd

pd.set_option('display.max_columns', None) # Prevent columns from being hidden
pd.set_option('display.width', 1000)        # Give the text output a wider area before it wraps

csv=pd.read_csv('data/c-test-ds.csv')


print("Dataset shape:", csv.shape)

## column data types.
print("\n Column data types:")
print(csv.dtypes)

## numerical and categorical columns.
numerical_columns = csv.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = csv.select_dtypes(include=['object']).columns

print("\n Numerical columns:", list(numerical_columns))
print("Categorical columns:", list(categorical_columns))

print("\nMissing values per column:")
print(csv.isnull().sum())

## Other echniques
print("\n using describe()")
print(csv.describe())
print(csv.describe(include=['object']))

## using head() and tail()
print(csv.head(5))
print(csv.tail(5))

## change float64 to float32 and display the info
print(csv.info())
print("\n Changed float64 to float32 ")
csv = csv.astype({col: 'float32' for col in numerical_columns if csv[col].dtype == 'float64'})
print(csv.info())


##end