import pandas as pd

pd.set_option('display.max_columns', None) # Prevent columns from being hidden
pd.set_option('display.width', 1000)        # Give the text output a wider area before it wraps

csv=pd.read_csv('data/c-test-ds.csv')

print(csv.head())