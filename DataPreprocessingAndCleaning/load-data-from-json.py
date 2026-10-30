import pandas as pd

## I have created a json and converted it to
## Datafrome and printing Dataframe.
dataframe = pd.read_json('data/product-data.json')

print(dataframe)