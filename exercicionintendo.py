import pandas as pd

df = pd.read_excel("best-selling game consoles.xlsx", sheet_name="consoles")

df['Console Name'] = df['Console Name'].str.replace('NES', 'Nitendinho').str.upper()

print(df['Console Name'].unique())

df['Released Year'] = pd.to_datetime(df['Released Year'], errors='coerce') 
df = df[df['Released Year'].dt.year > 2010]

df.fillna('missing', inplace=True)

df['Discontinuation Year'] = pd.to_datetime(df['Discontinuation Year'], errors='coerce')
df = df[(df['Discontinuation Year'] - df['Released Year']).dt.days < 2 * 365.25]

print(df.info())