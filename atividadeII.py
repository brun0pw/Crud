from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
MEU_BANCO = create_engine("///meubanco.db")
Session = sessionmaker(bind= MEU_BANCO)
session= Session()

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "usuarios"
    id_do_funcionario = Column(id, Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    cpf =  Column("cpf", Integer)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)   
    telefone = Column("telefone", String)
    def __init__(self, nome: str,  cpf :Integer, setor : str, funcao : str, salario: Integer, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
    Base.metadata.create_all(bind = MEU_BANCO)

import os

def adicionar_funcionario():
    inserir_nome = input("Digite seu nome: ")
    inserir_cpf = input("Digite seu cpf: ")
    inserir_setor = input("Digite sua setor: ")
    inserir_funcao = input("Digite sua funcao: ")
    inserir_salario = input("Digite seu salario: ")
    inserir_telefone = input("Digite seu telefone: ")
    funcionario = Funcionario(nome= inserir_nome, cpf = inserir_cpf, setor = inserir_setor, funcao= inserir_funcao, salario= inserir_salario, telefone= inserir_telefone)
    session.add(funcionario)
    session.commit()
    lista_trabalhador = session.query(Funcionario).all()
    return funcionario, lista_trabalhador

def consultar_funcionario(funcionario):
    lista_todos_os_funcionarios = []
    lista_todos_os_funcionarios =  session.query(Funcionario).all()
    
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
    cpf_usuario =  input("digite o cpf do funcionario a ser excluido: ")
    for trabalhador in lista_todos_os_funcionarios:
          
    if cpf_usuario ==  in funcionario:
        print(f"")
   
def atualizar_funcionario(funcionario):     

def excluir_todos_os_funcionarios(funcionario):
        print("\n Excluindo um usuario")
        cpf_usuario =  input("digite o cpf do funcionario a ser excluido: ")
        funcionario = session.query(Funcionario).filter_by(cpf = cpf_usuario).first()
        session.delete(funcionario)
        session.commit()
        print("usuario excluido com sucesso! ")   

def listar_todos_os_funcionarios():
    print("\nExibindo todos os funcionários no banco de dados.")
    lista_trabalhador =  session.query(Funcionario).all()
    for usuario in lista_trabalhador:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

while True:
    print("""
        === RH System ===       
    1 - Adicionar funcionário
    2 - Consultar funcionário
    3 - Atualizar funcionário
    4 - Excluir um funcionário
    5 - Listar todos os funcionários
    0 - Sair do funcionário
       
       """)
    escolha = int(input("Digite sua opção: "))
    match escolha:
        case 1: 
         adicionar_funcionario()
        case 2: 
            print()
        case 3:
          print()  
        case 4:
           excluir_todos_os_funcionarios()     
        case 5:
            listar_todos_os_funcionarios()
        case 0 :
            print("Saíndo do funcionário,  laele")
            #Fechando conexão
            session.close()