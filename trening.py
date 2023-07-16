import pymongo as pm
import pandas as pd


client = pm.MongoClient('mongodb+srv://karolwalczak61:Jakie_Dymyjd132@wroldpopulationbycountr.dvfaphz.mongodb.net/', 27017)

db = client['sample_weatherdata']
collection = db['data']


data = pd.DataFrame(list(collection.find()))


temperatures_data = data['airTemperature']


available_keys = data['airTemperature'].apply(lambda x: list(x.keys())).explode().unique()
print("Dostępne klucze w kolumnie 'airTemperature':", available_keys)