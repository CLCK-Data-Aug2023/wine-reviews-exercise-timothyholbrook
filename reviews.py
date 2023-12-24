import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

summary_df = df.groupby('country').agg({'points': ['count', 'mean']}).reset_index()
summary_df.columns = ['country', 'count', 'points']

summary_df['points'] = summary_df['points'].round(1)

summary_df.to_csv('data/reviews-per-country.csv', index=False)