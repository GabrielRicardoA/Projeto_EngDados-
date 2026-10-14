from src.extract import Extract
from src.transform import Transform
from src.load import Load

dados = Extract()
dados = dados.extract_pnadc() #retorna um df bronze da api cru msm 

print("Os dados foram extraidos com sucesso!")

carregamento = Load()#carrega o df
carregamento.load_mongo(dados,"IBGE","PNADC") #erro aqui neste metodo
print("Os dados foram carregados com sucesso!")

dados = Transform()
dados_silver = dados.trasnform_to_silver() #transforma o msm df em silver

carga = Load()
carga.load_neon(dados_silver,"Tabela_PNADC_silver") #recebe "df" e nome da tabela





