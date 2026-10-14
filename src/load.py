from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
import json 
import os
import certifi
from sqlalchemy import create_engine

load_dotenv()

class Load():
    def __init__(self):
        self.mongo_uri = os.getenv('MONGODB_uri')
        self.client = MongoClient(self.mongo_uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

        self.access_neon = os.getenv('DATABASE_URL')
        self.engine = create_engine(self.access_neon)

    def load_json(self,nomes_doc,data): 

        with open(f"{nomes_doc}.json","w",encoding="utf-8") as f:
            
            json.dump(data,f)
           


    def load_mongo(self,data: list[dict], db_name:str, collection_name:str):
        collection = self.client[db_name][collection_name] 
        if data:
            collection.insert_many(data)

        print(f"Dados inseridos com sucesso na coleção '{collection_name}'!")


    def load_neon(self, df, nome_tabela):
        df.to_sql(nome_tabela, self.engine, if_exists="replace",index=False)

        self.engine.dispose()#fechar sessao
        print(f"Dados salvos no Neon com sucesso na tabela'{nome_tabela}'!")



