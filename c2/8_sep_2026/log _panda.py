import pandas as pd
df = pd.read_csv("orders.csv")

df.info()

print("\nRow at index 15:")
print(df.loc[15])

print("\nComplete DataFrame:")
print(df)

print("\nFirst row - word_freq_all:")
print(df.loc[0, "word_freq_all"])

