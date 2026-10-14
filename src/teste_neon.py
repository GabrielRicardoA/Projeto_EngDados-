import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

acesso_neon = os.getenv("DATABASE_URL")

engine = create_engine(acesso_neon)

df = pd.DataFrame(
    {
        "periodo": ["2024Q1", "2024Q2"],
        "valor" : [9.5 , 11.2]
    }
)

df.to_sql("teste_neon", engine, if_exists="replace")

print("dados salvos na tabela: 'teste_neon'!  ")

