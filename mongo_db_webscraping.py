# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:21:30 2023

@author: Marcin
"""

import pymongo

# Połącz się z loclahost
mongo_db = pymongo.MongoClient("mongodb://localhost:27017/")

# Podajmy nazwę nowej bazy
db_name = 'test_new_db'

# Wyswietlny wszystkie istniejace bazy danych - jezli istnieje taka, to usun
for db_n in mongo_db.list_database_names():
    print(db_n)
    # Jesli taka baza istnieje, to usun
    if db_n == db_name:
        mongo_db.drop_database(db_name)
        print(db_name + ' dropped')
        
# Uwtorzmy nowa baze
new_db = mongo_db[db_name]

# Przygotowanie danych
from sklearn.datasets import load_iris
import numpy as np
import pandas as pd

iris = load_iris()
data_iris = pd.DataFrame(data = np.c_[iris['data'], iris['target']], columns = iris['feature_names'] + ['target'])

data_x = data_iris.drop(columns = ['target'])
data_y = data_iris['target']

# Dodajemy dane do poszczegolnych kolekcji
new_db['iris_x'].insert_many(data_x.to_dict('records'))
new_db['iris_y'].insert_many(data_y.to_frame().to_dict('records'))

###########
# Wczytanie danych z bazy
import pandas as pd
import numpy as np
import pymongo

# Połącz się z loclahost
mongo_db = pymongo.MongoClient("mongodb://localhost:27017/")

# Połącz się z bazą danych
loaded_db = mongo_db['test_new_db']

# Pobierzmy dane (np. do uczenia maszynowgo)
x_loaded = loaded_db['iris_x']
y_loaded = loaded_db['iris_y']

X = []
Y = []

for x in x_loaded.find():
    X.append(x)

for y in y_loaded.find():
    Y.append(y)

# Tworzymy ramkę danych
data = pd.DataFrame(X).drop(columns=['_id'])
data['target'] = pd.DataFrame(Y).drop(columns=['_id'])

# Operacje na danych... (aktualizacja - update)

# WEBSCRAPPING
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

# Ustawienia przeglądarki
caps = DesiredCapabilities().CHROME
# Czeka na załadowanie dokumentu
caps["pageLoadStrategy"] = "eager"
browser = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps)

browser.get('https://www.onet.pl/')

time.sleep(3)

browser.find_element(By.XPATH, "/html/body/div[7]/div[1]/div[2]/div/div[6]/button[2]").click()

time.sleep(3)

# Pobieramy content
page_content = browser.page_source

# Konwertuj do bs (beautiful soup)
soup = bs(page_content)
browser.close()