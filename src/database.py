from model import Empresa,Fornecedor, CONN, Base,engine,session
from datetime import datetime



class Database():
    def __init__(self) -> None:
        super().__init__()

    def insert_table_empresa(cnpj:str,razao:str ,nome_fantasia:str=None,pj:str='j',
                             dt_abertura = datetime.now(),IE:str='',IM:str ='',contribuinte:str = 'N',simples:str = 'N',ramo:str='',rua:str='',numero:int=0,
                             bairro:str='',complemento:str='',cep:str='',cidade:str='',uf:str='',celular:str='',whats:str='N',telefone:str='',
                             email:str = '',obs:str=''):
        try:
            new_emp = Empresa(
                razao_social = razao,
                nome_fantasia = nome_fantasia,
                cnpj_cpf = cnpj,
                pf_pj = pj,
                data_abertura = dt_abertura,
                IE = IE,
                IM = IM,
                contribuinte = contribuinte,
                simples = simples,
                ramo_ativ = ramo,
                end_rua = rua,
                end_numero = numero,
                end_bairro = bairro,
                end_complemento = complemento,
                end_cep = cep,
                end_cidade = cidade,
                end_uf = uf,
                celular = celular,
                p_whats = whats,
                telefone = telefone,
                email = email,
                obs = obs

            )

            session.add(new_emp)            
            session.commit()

            return(True,new_emp.id)
        except ValueError as e:
            session.rollback()
            return(False,str(e))    

    def update_table_empresa(id :int,cnpj: str, razao: str, nome_fantasia: str = None, pj: str = 'j',
                         dt_abertura = datetime.now(), IE: str = '', IM: str = '', 
                         contribuinte: str = 'N', simples: str = 'N', ramo: str = '', 
                         rua: str = '', numero: int = 0, bairro: str = '', 
                         complemento: str = '', cep: str = '', cidade: str = '', 
                         uf: str = '', celular: str = '', whats: str = 'N', 
                         telefone: str = '', email: str = '', obs: str = ''):
        try:
            # Busca o registro existente pelo CNPJ
            empresa = session.query(Empresa).filter(Empresa.id == id).first()

            if empresa is None:
                return (False, "Empresa não encontrada.")

            # Atualiza os campos do registro existente
            empresa.razao_social = razao
            empresa.nome_fantasia = nome_fantasia
            empresa.pf_pj = pj
            empresa.data_abertura = dt_abertura
            empresa.IE = IE
            empresa.IM = IM
            empresa.contribuinte = contribuinte
            empresa.simples = simples
            empresa.ramo_ativ = ramo
            empresa.end_rua = rua
            empresa.end_numero = numero
            empresa.end_bairro = bairro
            empresa.end_complemento = complemento
            empresa.end_cep = cep
            empresa.end_cidade = cidade
            empresa.end_uf = uf
            empresa.celular = celular
            empresa.p_whats = whats
            empresa.telefone = telefone
            empresa.email = email
            empresa.obs = obs

            # Commit das alterações
            session.commit()
            return (True, empresa.id)
        
        except Exception as e:
            session.rollback()
            return (False, str(e))

    def get_table_empresa(type = None, id:int = None):
       lista = []

       match type:
        case "id":
            return session.query(Empresa).filter_by(id=id).order_by().all()
        
        case _:
            q = session.query(Empresa).all()
            print (q)
            for index,i in enumerate(q):
                lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])              
                # lista.append([index + ' - ' +  i.id,index + ' - ' +  i.razao_social,index + ' - ' +  i.nome_fantasia,index + ' - ' +  i.cnpj_cpf,index + ' - ' +  i.pf_pj,index + ' - ' +  i.data_abertura,index + ' - ' +  i.IE,index + ' - ' +  i.IM,index + ' - ' +  i.contribuinte,index + ' - ' +  i.simples,index + ' - ' +  i.ramo_ativ,index + ' - ' +  i.end_rua,index + ' - ' +  i.end_numero,index + ' - ' +  i.end_bairro,index + ' - ' +  i.end_complemento,index + ' - ' +  i.end_cep,index + ' - ' +  i.end_cidade,index + ' - ' +  i.end_uf,index + ' - ' +  i.celular,index + ' - ' +  i.p_whats,index + ' - ' +  i.telefone,index + ' - ' +  i.email,index + ' - ' +  i.obs])              
            

            return lista

    def insert_table_fornecedor(cnpj:str,razao:str ,nome_fantasia:str=None,pj:str='j',
                             dt_abertura = datetime.now(),IE:str='',IM:str ='',contribuinte:str = 'N',simples:str = 'N',ramo:str='',rua:str='',numero:int=0,
                             bairro:str='',complemento:str='',cep:str='',cidade:str='',uf:str='',celular:str='',whats:str='N',telefone:str='',
                             email:str = '',obs:str=''):
        try:
            new_for = Fornecedor(
                razao_social = razao,
                nome_fantasia = nome_fantasia,
                cnpj_cpf = cnpj,
                pf_pj = pj,
                data_abertura = dt_abertura,
                IE = IE,
                IM = IM,
                contribuinte = contribuinte,
                simples = simples,
                ramo_ativ = ramo,
                end_rua = rua,
                end_numero = numero,
                end_bairro = bairro,
                end_complemento = complemento,
                end_cep = cep,
                end_cidade = cidade,
                end_uf = uf,
                celular = celular,
                p_whats = whats,
                telefone = telefone,
                email = email,
                obs = obs

            )

            session.add(new_for)            
            session.commit()

            return(True,new_for.id)
        except ValueError as e:
            session.rollback()
            return(False,str(e))    

    def update_table_fornecedor(id :int,cnpj: str, razao: str, nome_fantasia: str = None, pj: str = 'j',
                         dt_abertura = datetime.now(), IE: str = '', IM: str = '', 
                         contribuinte: str = 'N', simples: str = 'N', ramo: str = '', 
                         rua: str = '', numero: int = 0, bairro: str = '', 
                         complemento: str = '', cep: str = '', cidade: str = '', 
                         uf: str = '', celular: str = '', whats: str = 'N', 
                         telefone: str = '', email: str = '', obs: str = ''):
        try:
            # Busca o registro existente pelo CNPJ
            fornecedor = session.query(Fornecedor).filter(Empresa.id == id).first()

            if fornecedor is None:
                return (False, "Empresa não encontrada.")

            # Atualiza os campos do registro existente
            fornecedor.razao_social = razao
            fornecedor.nome_fantasia = nome_fantasia
            fornecedor.pf_pj = pj
            fornecedor.data_abertura = dt_abertura
            fornecedor.IE = IE
            fornecedor.IM = IM
            fornecedor.contribuinte = contribuinte
            fornecedor.simples = simples
            fornecedor.ramo_ativ = ramo
            fornecedor.end_rua = rua
            fornecedor.end_numero = numero
            fornecedor.end_bairro = bairro
            fornecedor.end_complemento = complemento
            fornecedor.end_cep = cep
            fornecedor.end_cidade = cidade
            fornecedor.end_uf = uf
            fornecedor.celular = celular
            fornecedor.p_whats = whats
            fornecedor.telefone = telefone
            fornecedor.email = email
            fornecedor.obs = obs

            # Commit das alterações
            session.commit()
            return (True, fornecedor.id)
        
        except Exception as e:
            session.rollback()
            return (False, str(e))

    def get_table_fornecedor(type = None, id:int = None):
       lista = []

       match type:
        case "id":
            return session.query(Fornecedor).filter_by(id=id).order_by().all()
        
        case _:
            q = session.query(Fornecedor).all()
            print (q)
            for index,i in enumerate(q):
                lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])              
                # lista.append([index + ' - ' +  i.id,index + ' - ' +  i.razao_social,index + ' - ' +  i.nome_fantasia,index + ' - ' +  i.cnpj_cpf,index + ' - ' +  i.pf_pj,index + ' - ' +  i.data_abertura,index + ' - ' +  i.IE,index + ' - ' +  i.IM,index + ' - ' +  i.contribuinte,index + ' - ' +  i.simples,index + ' - ' +  i.ramo_ativ,index + ' - ' +  i.end_rua,index + ' - ' +  i.end_numero,index + ' - ' +  i.end_bairro,index + ' - ' +  i.end_complemento,index + ' - ' +  i.end_cep,index + ' - ' +  i.end_cidade,index + ' - ' +  i.end_uf,index + ' - ' +  i.celular,index + ' - ' +  i.p_whats,index + ' - ' +  i.telefone,index + ' - ' +  i.email,index + ' - ' +  i.obs])              
            

            return lista

      
          
if __name__=='__main__':

 app = Database.get_table_empresa()
 print(app)
