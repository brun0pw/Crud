# ORM : SQLAlchemy 
# Banco de dados : SQLite

""" Menu :

        === RH System ===

    1 - Adicionar funcionário
    2- Consultar um funcionário
    3- Atualizar os dados de um funcionário 
    4- Excluir um funcionário 
    5- Listar todos os funcionários
    6- sair do sistema



"""

import os 
from sqlalchemy import create_engine , Column  , String , Integer 
from sqlalchemy.orm import sessionmaker , declarative_base

# Criando meu banco de dados.

RH_SYSTEM = create_engine("sqlite:///banco.db")

Session = sessionmaker(bind=RH_SYSTEM)
session = Session()


Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    # Tabela

    id = Column ("id" , Integer , primary_key=True , autoincrement=True)
    nome = Column("nome" , String)
    email = Column("email " , String)
    senha = Column("senha" , String)

    #  Definindo os atributos de classe.
    def __init__(self , nome:str , email:str , senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando a tabela no banco de dados.
Base.metadata.create_all(bind=RH_SYSTEM)

# Salvamento no banco de dados
os.system("cls || clear")

# Solicitando dados.

print ("Solicitando dados para o funcionario")
inserir_nome = input ("Digite o seu nome: ")
inserir_email = input ("Digite o seu email: ")
inserir_senha = input ("Digite a sua senha: ")


funcionarios = Funcionario("Carlos" , "carlos@gmail.com" , "123")
session.add(funcionarios)
session.commit()

# Listando todos os usuarios do banco de dados.

print("\nExibindo todos os funcionarios do banco de dados")
lista_funcionarios = session.query(Funcionario).all

for funcionario in lista_funcionarios:
    print (f"{funcionario.id} - {funcionarios.nome} - {funcionarios.senha}")

# Delete

print("\nExcluindo um usuário.")
email_funcionario = input ("Informe o email do funcionário para ser excluido:")
funcionario = session.query(Funcionario).filter_by(email = email_funcionario).first()
session.delete(funcionario)
session.commit()
print("Usuário excluido com sucesso.")

# Listando todos os funcionários do banco de dados.
print ("\nExibindo todos os usuários do banco de dados.")
lista_funcionarios = session.query(Funcionario).all()

for funcionario in lista_funcionarios:
    print (f"{funcionario.id} - {funcionario.nome} - {funcionario.senha}")

# Fechando conexão.
session.close()