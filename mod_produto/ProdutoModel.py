import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer, BLOB

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(CHAR(10), nullable=True)
    foto = Column(BLOB, nullable=True)
    valor_unitario = Column(Integer, nullable=False)


    def __init__(self, id_cliente, nome, descricao, foto, valor_unitario):
        self.id_cliente = id_cliente
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario
