import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"D:\ProdigyInfoTech\PRODIGY_DS_01\Gender_Classification_Dataset.csv")

# Preview data
print("Sample Data:\n", df.head())


# Gender distribution (bar chart)
sns.set(style="whitegrid")
sns.countplot(x='gender', data=df, palette='Set2')
plt.title("Gender Distribution in the Sample Population")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("gender_distribution.png")
plt.show()


# Age distribution (histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue')
plt.title("Age Distribution in the Sample Population")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.show()


