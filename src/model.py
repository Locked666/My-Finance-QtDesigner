from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey, Text, BLOB,Float,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime,date
from pathlib import Path
from ConfigApp import MODE_DEBUG, PATH_DATABASE
import os 

CONN = f"sqlite:///{PATH_DATABASE}"

engine = create_engine(CONN,echo=MODE_DEBUG)
Session =  sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class SysConfig(Base):
    __tablename__='sys_config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chart_p = Column(String, insert_default="wRuN4JL2hp1UrnxSBa4Por3biV_UhPgXQY4qnU0-5ig=")

class Empresa(Base):
    __tablename__='empresa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    cnpj_cpf = Column(String)
    pf_pj = Column(String, comment='Pesso Fiscia : F e pessoa Juridica = J')
    data_abertura = Column(Date)
    IE = Column(String)
    IM = Column(String)
    contribuinte = Column(String, comment='S sim e N não')
    simples = Column(String, comment='S sim e N não')
    ramo_ativ = Column(String, comment='Ramo de atividade')
    end_rua = Column(String)
    end_numero = Column(Integer)
    end_bairro = Column(String)
    end_complemento = Column(String)
    end_cep = Column(String)
    end_cidade = Column(String)
    end_uf = Column(String)
    celular = Column(String)
    p_whats = Column(String, comment="S para sim e N para não")
    telefone = Column(String)
    email = Column(String)
    obs = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 

class Fornecedor(Base):
    __tablename__='fornecedor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    cnpj_cpf = Column(String)
    ativo = Column(String,default='S',comment='S sim e N não')
    pf_pj = Column(String, comment='Pesso Fiscia : F e pessoa Juridica = J')
    data_abertura = Column(Date)
    IE = Column(String)
    IM = Column(String)
    contribuinte = Column(String, comment='S sim e N não')
    simples = Column(String, comment='S sim e N não')
    ramo_ativ = Column(String, comment='Ramo de atividade')
    end_rua = Column(String)
    end_numero = Column(Integer)
    end_bairro = Column(String)
    end_complemento = Column(String)
    end_cep = Column(String)
    end_cidade = Column(String)
    end_uf = Column(String)
    celular = Column(String)
    p_whats = Column(String, comment="S para sim e N para não")
    telefone = Column(String)
    email = Column(String)
    obs = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 

class RamoAtividade(Base):
    __tablename__='ramo_atividade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo=Column(String)
    descricao=Column(String)

class Entregas(Base):
    __tablename__='entregas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String)
    km_inicial=Column(String)
    km_final=Column(String)
    km_lt=Column(String)
    qt_entregas=Column(String)
    valor_final= Column(String)
     
class About(Base):
    __tablename__='about'
    id = Column(Integer, primary_key=True, autoincrement=True)
    razao = Column(String, default = 'Julio Sales') 
    nome_fantasia = Column(String, default = 'Sales Informática')
    cnpj = Column(String, default = '06919904179')
    end_rua = Column(String)
    end_numero = Column(Integer)
    end_bairro = Column(String)
    end_complemento = Column(String)
    end_cep = Column(String)
    end_cidade = Column(String)
    end_uf = Column(String)
    telefone = Column(String)
    email = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 

class Usuario(Base):
    __tablename__='usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    user = Column(String)
    senha = Column(String,)
    ativo = Column(String,default='S',comment='S sim e N não')
    reset_senha = Column(String,default='S',comment='S sim e N não')
    primeiro_acesso = Column(String,default='S',comment='S sim e N não')
    bloqueado = Column(String,default='S',comment='S sim e N não')
    end_rua = Column(String)
    end_numero = Column(Integer)
    end_bairro = Column(String)
    end_complemento = Column(String)
    end_cep = Column(String)
    end_cidade = Column(String)
    end_uf = Column(String)
    celular = Column(String)
    p_whats = Column(String, comment="S para sim e N para não")
    telefone = Column(String)
    email = Column(String)
    obs = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 


class Produtos(Base):
    __tablename__='produtos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)
    nome_reduzido = Column(String)
    tipo_produto = Column(Integer,default=0, comment='0 - Mercadoria para revenda, 1 - Consumo, 2 - MP, 3 - bem movel')
    ativo = Column(String, default='S', comment='S - Sim, N - Não ')
    unidade = Column(String)
    codigo_fab = Column(String)
    qt_unid = Column(String)
    medida = Column(String)
    grupo = Column(Integer)
    sub_grupo = Column(Integer)
    categoria = Column(Integer)
    marca =  Column(Integer)
    grupo_preco = Column(Integer)
    controlado = Column(String,default='N', comment='S - Sim, N - Não ')
    imp_ticket = Column(String,default='N', comment='S - Sim, N - Não ')
    risco = Column(String,default='N', comment='S - Sim, N - Não ')

class ProdutoPreco(Base):
    __tablename__='produto_preco'
    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa = Column(Integer, ForeignKey('empresa.id'), nullable=False, comment='Id da tabela empresa')
    produto = Column(Integer, ForeignKey('produtos.id'),nullable=False, comment='Id da tabela de produtos')
    custo_indireto = Column(Float, default=0.0)
    custo_direto = Column(Float, default=0.0)
    custo_impostos = Column(Float, default=0.0)
    custo_diff = Column(Float, default=0.0)
    margem_direta = Column(Float, default=0.0)
    markup = Column(Float, default=0.0)
    preco = Column(Float, default=0.0)
    preco_sugerido = Column(Float, default=0.0)


if not os.path.exists(PATH_DATABASE):
    Base.metadata.create_all(bind=engine) 
    sys = SysConfig()
    session.add(sys)            
    session.commit()

    about = About()
    session.add(about)
    session.commit()



if __name__=='__main__':
    Base.metadata.create_all(bind=engine)
    pass