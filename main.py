from src.extract import Extract
from src.load import Load

dados = Extract()
dados = dados.extract_pnadc()

print("Os dados foram extraidos com sucesso!")

carregamento = Load()
carregamento.load_mongo(dados,"IBGE","PNADC")
print("Os dados foram carregados com sucesso!")
