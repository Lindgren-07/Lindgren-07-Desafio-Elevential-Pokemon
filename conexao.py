from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
Base = declarative_base()
from model import Pokemon, Tipo

db_url = 'postgresql://postgres:123@localhost:5432/desafio'
engine = create_engine(db_url)




Session = sessionmaker(bind=engine)
session = Session()

# Teste de conexão
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexão bem-sucedida:", result.scalar())
except Exception as e:
    print("Erro ao conectar ao banco:", e)

Base.metadata.create_all(bind=engine)
