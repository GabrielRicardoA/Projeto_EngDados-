from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

class Transform():

    def __init__(self) -> None:
        self.mongo_uri = os.getenv("MONGODB_uri")

    def trasnform_to_silver(self):
        client = MongoClient(self.mongo_uri, server_api=ServerApi('1'))
        
        db = client["IBGE"] 
        

        data = db["PNADC"] 

        data.count_documents({})  

        data = list(data.find()) 

        serie = data[0]['resultados'][0]["series"][0]['serie']

        df = pd.DataFrame.from_dict(serie, orient='index',columns=['valor'])

        df.index.name = "periodo"
        df = df.reset_index()


        df['valor'] = df['valor'].replace("...",'0')

        df['valor'] = df['valor'].astype(float)


        df['ano'] = df['periodo'].str[:4]
        df['tri'] = df['periodo'].str[-2:].astype(int)

        df['periodo'] = pd.PeriodIndex(df['ano'] + "Q" + df["tri"].astype(str),freq='Q') 


        df['periodo'] = df['periodo'].dt.to_timestamp() 
        print("dados transformados em silver!")

        return df

