import pandas as pd

# Create a Dataframe from CSV
moma=pd.read_csv("https://raw.githubusercontent.com/valxwz/data-viz/master/gp/MoMA_artworks_cleaned_all_columns.csv")

# Drop via logic: similar to SQL 'WHERE' clause

date_created_new= moma['Date'].astype(str).str[0:4].str[-2:]
moma = moma[int(date_created_new)==False]
moma.to_csv(r'', index = False)