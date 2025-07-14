import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import os

path = kagglehub.dataset_download("gokulrajkmv/unemployment-in-india")
print("Dataset downloaded to:", path)
csv_file = os.path.join(path, "Unemployment in India.csv")
df = pd.read_csv(csv_file)

df.columns = df.columns.str.strip()
print("Columns in dataset:", df.columns.tolist())

df['Date'] = pd.to_datetime(df['Date'], format=' %d-%m-%Y')
df = df.sort_values(by='Date').dropna()
sns.set(style="whitegrid")

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')
plt.title("Overall Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14,7))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region', legend=False)
plt.title("Unemployment Rate Trend by Region")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Area')
plt.title("Unemployment Rate by Area Type (Rural vs Urban)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
