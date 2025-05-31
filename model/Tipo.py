from sqlalchemy import Column,String,Integer
from conexao import Base

class Tipo(Base):
    __tablename__ = 'tipo'
    codigo = Column(Integer,primary_key=True)
    nome = Column(String(60),nullable=False)

    def __init__(self, c ,n):
        self.set_codigo(c)
        self.set_nome(n)

    
    def get_codigo(self):
        return self.codigo
    
    def get_nome(self):
        return self.nome

    def set_codigo(self, c):
        self.validar_codigo(c)
        self.codigo = c

    def set_nome(self, n):
        self.validar_nome(n)
        self.nome = n    
    

    def validar_codigo(self,c):
        try:
            int(c)
        except (ValueError):
            raise ValueError("O código deve ser um número inteiro válido.")
    
    def validar_nome(self,n):
        if n is None or n.strip() == "":
             raise ValueError("O nome não pode ser nulo")
        
        for char in n:
            if char.isdigit():
                raise ValueError("O nome não deve conter números")
            if not (char.isalpha() or char.isspace()):
                raise ValueError("O nome não deve conter caracteres especiais")
            
    def __str__(self):
        return f"Tipo(codigo={self.codigo}, nome='{self.nome}')"

        
