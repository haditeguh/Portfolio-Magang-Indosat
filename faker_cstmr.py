import pandas as pd
import numpy as np
from faker import Faker
import random
import matplotlib.pyplot as plt

# Setup
fake = Faker("id_ID")
np.random.seed(42)
Faker.seed(42)

# prefix Indosat
indosat_prefixes = ['0814', '0815', '0816', '0855', '0856', '0857', '0858']

# paket data simulasi
paket_data = ['Freedom Combo', 'Freedom Internet', 'Yellow', 'Unlimited 2GB', 'Unlimited 5GB']

# kota
cities = ['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta', 'Medan', 'Semarang', 'Makassar']

# generate data
n = 200 # jumlah data
data = []
for _ in range(n):
    name = fake.name()
    prefix = random.choice(indosat_prefixes)
    no_hp = prefix + ''.join([str(random.randint(0, 9)) for _ in range(8)])
    city = random.choice(cities)
    paket = random.choice(paket_data)
    tgl_beli = fake.date_between(start_date='-1y', end_date='today')
    durasi_bulan = random.randint(1, 12)
    freq_topup = random.randint(0, 5)
    kuota_per_bulan = random.randint(1, 25) # dalam GB

    data.append([
        name, no_hp, city, paket, tgl_beli, durasi_bulan, freq_topup, kuota_per_bulan 
    ])

# buat dataframe
df = pd.DataFrame(data, columns=[
    'Nama', 'No_HP', 'Kota', 'Paket', 'Tgl_beli', 'Durasi_Bulan', 'Frekuensi_Topup', 'Kuota_Bulan_GB'
])

# simpan ke csv
csv_path = "./data_pelanggan_indosat.csv"
df.to_csv(csv_path, index=False)
