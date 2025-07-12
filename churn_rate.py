# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('data_pelanggan_indosat.csv')

# %%
df.head()

# %%
city_data = df['Kota'].value_counts()

# %%
city_data

# %%
cities = city_data.index.tolist()

# %%
counts = city_data.values.tolist()

# %%
cities

# %%
counts

# %%
sns.pairplot(df)

# %%
