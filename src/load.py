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
        self.mongo_uri = os.getenv('MONGO_URI')
        self.access_neon = os.getenv('DATABASE_URL')
        self.client = MongoClient(self.mongo_uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
        self.engine = create_engine(self.access_neon)

    def load_json(self,nomes_doc,data): #este metodo serve para guardar o json LOCALMENTE onde os parametros passados sao nomes_doc e data-->Os dados que extraimos 

        with open(f"{nomes_doc}.json","w",encoding="utf-8") as f:
            #aqui nos queremos abrir  e escrever por isso o "w" o arquivo json e damos o apelido deste arquivo de f
            
            json.dump(data,f)
            #aqui usamos um metodo da da biblioteca json para salvarmos os dados no arquivo que queremos 
            #json.dumpo(os dados, nome do arquivo)


    def load_mongo(self,data: list[dict], db_name:str, collection_name:str):# vc recebe como parametro do metodo os dados:esperando UMA LISTA DE DICIONARIOS, o nome do db,Nome da collection

        collection = self.client[db_name][collection_name] #aqui vc guarda o CAMINHO da que vc quer pra chegar a collection vc escolhe primeiro a data base pra dps ir pra collection
                                                            #obs os banco NOSQL sao open to fly ent vc pode criar o nome da db da na hora e collection que sera criado
        if data: #so pra ver se data esta vazio
            collection.insert_many(data) #aqui vc diz que colocar dados ate onde esta o caminho e em parenteses os dados que vc quer guardar

        print(f"Dados inseridos com sucesso na coleção '{collection_name}'!")# so falando que deu td cert0

    def load_neon(self, df, nome_tabela):
        df.to_sql(nome_tabela, self.engine, if_exists="replace")

        self.engine.dispose()#fechar sessao
        print(f"Dados salvos no Neon com sucesso na tabela'{nome_tabela}'!")