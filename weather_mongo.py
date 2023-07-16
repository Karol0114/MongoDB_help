import pymongo as pm
import interia_weather as iw

def add_data_to_mongodb(link):
    client = pm.MongoClient('mongodb+srv://karolwalczak61:Jakie_Dymyjd132@weathercluster.qua7gug.mongodb.net/', 27017)
    try:
        data = iw.long_term_weather(link)
        city_name = link.split("-")[2].split(",")[0]
        db = client['WeatherCluster']
        collection_name = f'{city_name}_long_term_weather'
        collection = db[collection_name]
        
        collection.insert_one(data)
    except Exception as e:
        print(f'Wystąpił błąd: {e}')
    finally:
        client.close()


#def update_weather_data(link):
    #client = pm.MongoClient('mongodb+srv://karolwalczak61:Jakie_Dymyjd132@weathercluster.qua7gug.mongodb.net/')
    #try:
        #data = iw.long_term_weather(link)
        #city_name = link.split("-")[2].split(",")[0]
        #db = client['WeatherCluster']
        #collection_name = f'{city_name}_long_term_weather'
        #collection = db[collection_name]

        # Kryteria wyszukiwania
        #search_criteria = {"Miasto": city_name}

        # Wyszukanie pierwszego pasującego dokumentu
        #document = collection.find_one(search_criteria)

        #if document:
            #document_id = document["_id"]

            # Nowe dane, które mają zostać zaktualizowane
            #update_data = {"$set": data}

            # Aktualizacja dokumentu na podstawie _id
            #collection.update_one({"_id": document_id}, update_data)
        #else:
            #print(f'Brak dokumentu dla kryteriów wyszukiwania: {search_criteria}')
    #except Exception as e:
        #print(f'Wystąpił błąd: {e}')
    #finally:
        #client.close()


    
#add_data_to_mongodb('https://pogoda.interia.pl/prognoza-dlugoterminowa-krakow,cId,4970')
#update_weather_data('https://pogoda.interia.pl/prognoza-dlugoterminowa-krakow,cId,4970')