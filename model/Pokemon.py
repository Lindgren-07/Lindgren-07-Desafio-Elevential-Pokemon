from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from conexao import Base


class Pokemon(Base):
    __tablename__ = 'pokemon'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String(60), nullable=False)
    codigo_tipo_primario = Column(Integer, ForeignKey('tipo.codigo'), nullable=False)
    codigo_tipo_secundario = Column(Integer, ForeignKey('tipo.codigo'), nullable=True)

    tipo_primario = relationship("Tipo", foreign_keys=[codigo_tipo_primario])
    tipo_secundario = relationship("Tipo", foreign_keys=[codigo_tipo_secundario])

    def __init__(self, c, n, t1, t2=None):
        self.set_codigo(c)
        self.set_nome(n)
        self.set_tipo_primario(t1)
        if t2:
            self.set_tipo_secundario(t2)

    def get_tipo1(self):
        return self.tipo_primario
    
    def get_tipo2(self):
        return self.tipo_secundario
    
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

    def set_tipo_primario(self, t1):
        self.validar_tipo_primario(t1)
        self.codigo_tipo_primario = t1
    
    def set_tipo_secundario(self, t2):
        self.validar_tipo_secundario(t2)
        self.codigo_tipo_secundario = t2
        
        
    

    def validar_codigo(self,c):
        try:
            int(c)
        except (ValueError):
            raise ValueError("O código deve ser um número inteiro válido.")
    
    def validar_nome(self,n):
        if n is None or n.strip() == "":
             raise ValueError("O nome não pode ser nulo")
        
        
            
    def validar_tipo_primario(self,t1):
        try:
            int(t1)
        except (ValueError):
            raise ValueError("O código deve ser um número inteiro válido.")
         
    def validar_tipo_secundario(self,t2):
        try:
            int(t2)
        except (ValueError):
            raise ValueError("O código deve ser um número inteiro válido.")
         
    def __str__(self):
        return f"Pokemon(codigo={self.codigo}, nome='{self.nome}')"