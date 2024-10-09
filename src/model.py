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


if not os.path.exists(PATH_DATABASE):
    Base.metadata.create_all(bind=engine) 


if __name__=='__main__':
    Base.metadata.create_all(bind=engine) 
    pass