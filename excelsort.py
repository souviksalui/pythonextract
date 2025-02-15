import pandas as pd

df = pd.read_excel("C:\\Users\\USER\\Pictures\\orderReport last 6 months.xlsx")

# print(df.head(5))

df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d-%m-%Y %H:%M:%S")

df = df.sort_values(by='Order Date')

print("CSV sorted successfully!")

output_path = "C:\\Users\\USER\\Pictures\\sorted_file.csv"
df.to_csv(output_path, index=False)


print(f"CSV sorted and saved at {output_path}")