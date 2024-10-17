#arquivo txt.
#banco de dados
#SQLite
#S-Q-L 
#Linguagem de Consulta Estruturada
# SELECT * FROM CLIENTES
# NOME, SOBRENOME, IDADE
#ORM 
# é uma biblioteca que esconde o sql puro em uma linguagem

import os
from sqlalchemy import create_engine, Column, String, Integer

from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando  conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()



#I/O
#I = Input(Entrada)
#O = output(Saída)

#Criando  campos da tabela

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key =True, autoincrement = True)
    nome= Column("nome", String)
    email = Column("email", String)
    senha= Column("senha", String)
    #definindo atribrutos da classe
    def __init__(self, nome: str, email: str, senha : str):
        self.nome = nome
        self.email = email
        self.senha = senha
#init é imiediatamente quando a classe é chamada ela é automaticamente criada.
#Criando tabela no banco de dados
Base.metadata.create_all(bind = MEU_BANCO)

#Salvar no banco de dados.
os.system("cls || clear")
print("Salvando dados para o usuário.")
inserir_nome = input("digite seu nome: ")
inserir_email = input("digite seu e-mail: ") 
inserir_senha = input("digite sua senha: ")           

usuario = Usuario(nome = inserir_nome, email = inserir_email, senha = inserir_senha)
session.add(usuario)
session.commit()

#listando todos os usuarios no banco de dados
print("\nExibindo todos os usuarios no banco de dados.")
lista_usuario =  session.query(Usuario).all()

for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")
  
  
    
#delete
print("\n Excluindo um usuario")
email_usuario =  input("digite o email do usario a ser excluido: ")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print("usuario excluido com sucesso! ")
#Fechando conexão
session.close()
