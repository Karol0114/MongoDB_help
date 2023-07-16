import pandas as pd
from pymongo import MongoClient

# Połączenie z bazą danych MongoDB
client = MongoClient('adres_hosta', port=port)
db = client['nazwa_bazy']
kolekcja = db['nazwa_kolekcji']

# Pobranie wszystkich dokumentów z kolekcji MongoDB
dokumenty = kolekcja.find()

# Konwersja dokumentów do DataFrame w Pandas
df = pd.DataFrame(list(dokumenty))

# Sprawdzenie, czy istnieją brakujące dane w DataFrame
braki_danych = df.isnull().values.any()

if braki_danych:
    print("Istnieją brakujące dane w DataFrame.")
else:
    print("Brak brakujących danych w DataFrame.")