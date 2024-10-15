from model import Empresa,Fornecedor,SysConfig,Usuario,Entregas, CONN, Base,engine,session
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
            for index,i in enumerate(q):
                lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])              
                # lista.append([index + ' - ' +  i.id,index + ' - ' +  i.razao_social,index + ' - ' +  i.nome_fantasia,index + ' - ' +  i.cnpj_cpf,index + ' - ' +  i.pf_pj,index + ' - ' +  i.data_abertura,index + ' - ' +  i.IE,index + ' - ' +  i.IM,index + ' - ' +  i.contribuinte,index + ' - ' +  i.simples,index + ' - ' +  i.ramo_ativ,index + ' - ' +  i.end_rua,index + ' - ' +  i.end_numero,index + ' - ' +  i.end_bairro,index + ' - ' +  i.end_complemento,index + ' - ' +  i.end_cep,index + ' - ' +  i.end_cidade,index + ' - ' +  i.end_uf,index + ' - ' +  i.celular,index + ' - ' +  i.p_whats,index + ' - ' +  i.telefone,index + ' - ' +  i.email,index + ' - ' +  i.obs])              
            

            return lista

    def insert_table_fornecedor(cnpj:str,razao:str ,nome_fantasia:str=None,ativo:str='S',pj:str='J',
                             dt_abertura = datetime.now(),IE:str='',IM:str ='',contribuinte:str = 'N',simples:str = 'N',ramo:str='',rua:str='',numero:int=0,
                             bairro:str='',complemento:str='',cep:str='',cidade:str='',uf:str='',celular:str='',whats:str='N',telefone:str='',
                             email:str = '',obs:str=''):
        try:
            new_for = Fornecedor(
                razao_social = razao,
                nome_fantasia = nome_fantasia,
                ativo=ativo,
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

    def update_table_fornecedor(id :int,cnpj: str, razao: str, nome_fantasia: str = None,ativo:str = 'S', pj: str = 'J',
                         dt_abertura = datetime.now(), IE: str = '', IM: str = '', 
                         contribuinte: str = 'N', simples: str = 'N', ramo: str = '', 
                         rua: str = '', numero: int = 0, bairro: str = '', 
                         complemento: str = '', cep: str = '', cidade: str = '', 
                         uf: str = '', celular: str = '', whats: str = 'N', 
                         telefone: str = '', email: str = '', obs: str = ''):
        try:
            # Busca o registro existente pelo CNPJ
            fornecedor = session.query(Fornecedor).filter(Fornecedor.id == id).first()

            if fornecedor is None:
                return (False, "Fornecedor não encontrada.")

            # Atualiza os campos do registro existente
            fornecedor.razao_social = razao
            fornecedor.nome_fantasia = nome_fantasia
            fornecedor.ativo = ativo
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

    def get_table_fornecedor(type = None, id:int = None,cnpj:str = None):
       lista = []

       match type:
        case "id":
            query =  session.query(Fornecedor).filter_by(id=id).order_by().all()
            for index, i in enumerate(query):
                lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])
            return lista    
            
        case "list_id":
            query =  session.query(Fornecedor).all()
            for index, i in enumerate(query):
                # lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])
                lista.append(i.id)
            return lista    

        case "cnpj":
            query =  session.query(Fornecedor).filter_by(cnpj_cpf=cnpj).order_by().all()
            for index, i in enumerate(query):
                lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])
            return lista   
               

        case _:
            q = session.query(Fornecedor).all()
            for index,i in enumerate(q):
                lista.append([i.id,i.razao_social,i.nome_fantasia,i.cnpj_cpf,i.pf_pj,i.data_abertura,i.IE,i.IM,i.contribuinte,i.simples,i.ramo_ativ,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs,i.log_inclusao])              
                # lista.append([index + ' - ' +  i.id,index + ' - ' +  i.razao_social,index + ' - ' +  i.nome_fantasia,index + ' - ' +  i.cnpj_cpf,index + ' - ' +  i.pf_pj,index + ' - ' +  i.data_abertura,index + ' - ' +  i.IE,index + ' - ' +  i.IM,index + ' - ' +  i.contribuinte,index + ' - ' +  i.simples,index + ' - ' +  i.ramo_ativ,index + ' - ' +  i.end_rua,index + ' - ' +  i.end_numero,index + ' - ' +  i.end_bairro,index + ' - ' +  i.end_complemento,index + ' - ' +  i.end_cep,index + ' - ' +  i.end_cidade,index + ' - ' +  i.end_uf,index + ' - ' +  i.celular,index + ' - ' +  i.p_whats,index + ' - ' +  i.telefone,index + ' - ' +  i.email,index + ' - ' +  i.obs])              
            return lista

    def delete_table_fornecedor(id=None):
        if isinstance(id, int):
            try:
                obj = session.query(Fornecedor).filter_by(id=id).first()  # Obter a primeira instância
                if obj:
                    session.delete(obj)  # Deletar a instância encontrada
                    session.commit()
                    return True
                else:
                    return False, "Nenhum valor encontrado"
            except ValueError as e:
                return False, e

        elif isinstance(id, list):
            try:
                objs = session.query(Fornecedor).filter(Fornecedor.id.in_(id)).all()  # Obter todas as instâncias
                for obj in objs:
                    session.delete(obj)  # Deletar cada instância encontrada
                session.commit()
                return True
            except ValueError as e:
                return False, e

        else:
            return False, "ID deve ser um inteiro ou uma lista"
 
    def get_table_sys_config():
        query = session.query(SysConfig).filter_by(id=1).all()
        for i in query:
            return i.chart_p    

    def get_table_user(type:None, id:int =  None,usuario: str = None ):
        lista = []

        match type:
            case 'id':
                query = session.query(Usuario).filter_by(id=id).all()
                for i in query: 
                    lista.append([i.id,i.nome,i.cpf,i.user,i.senha,i.ativo,i.reset_senha,i.primeiro_acesso,i.bloqueado,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs])
                return lista
            
            case 'user':
                query = session.query(Usuario).filter_by(user=usuario).all()
                for i in query: 
                    lista.append([i.user,i.senha,i.ativo,i.reset_senha,i.primeiro_acesso,i.bloqueado])
                return lista

            case "list_id":
                query =  session.query(Usuario).all()
                for i in query:
                    lista.append(i.id)
                return lista  

            case _:
                query = session.query(Usuario).all()
                for i in query: 
                    lista.append([i.id,i.nome,i.cpf,i.user,i.senha,i.ativo,i.reset_senha,i.primeiro_acesso,i.bloqueado,i.end_rua,i.end_numero,i.end_bairro,i.end_complemento,i.end_cep,i.end_cidade,i.end_uf,i.celular,i.p_whats,i.telefone,i.email,i.obs])
                return lista    

    def delete_table_user(id=None):
        if isinstance(id, int):
            try:
                obj = session.query(Usuario).filter_by(id=id).first()  # Obter a primeira instância
                if obj:
                    session.delete(obj)  # Deletar a instância encontrada
                    session.commit()
                    return True
                else:
                    return False, "Nenhum valor encontrado"
            except ValueError as e:
                return False, e

        elif isinstance(id, list):
            try:
                objs = session.query(Usuario).filter(Usuario.id.in_(id)).all()  # Obter todas as instâncias
                for obj in objs:
                    session.delete(obj)  # Deletar cada instância encontrada
                session.commit()
                return True
            except ValueError as e:
                return False, e

        else:
            return False, "ID deve ser um inteiro ou uma lista"

    def insert_table_user(id:int = None,type:str = 'insert',nome:str= None ,cpf:str= None,user:str= None,senha:str= None,ativo:str= None,reset_senha:str= None,primeiro_acesso:str= None,bloqueado:str= None
                          ,end_rua:str= None,end_numero:str= None,end_bairro:str= None,end_complemento:str= None,end_cep:str= None,end_cidade:str= None,end_uf:str= None,
                          celular:str= None,p_whats:str= None,telefone:str= None,email:str= None,obs:str= None):
        match type:
            case 'insert':
                try:
                    new_user = Usuario(
                        nome=nome, 
                        cpf=cpf, 
                        user=user,
                        senha=senha, 
                        ativo=ativo, 
                        reset_senha=reset_senha,
                        primeiro_acesso=primeiro_acesso, 
                        bloqueado=bloqueado, 
                        end_rua=end_rua,
                        end_numero=end_numero,
                        end_bairro=end_bairro,
                        end_complemento=end_complemento,
                        end_cep=end_cep,
                        end_cidade=end_cidade,
                        end_uf=end_uf,
                        celular=celular,
                        p_whats=p_whats,
                        telefone=telefone,
                        email=email,
                        obs=obs


                    )
                    session.add(new_user)            
                    session.commit()

                    return(True,new_user.id)
                except ValueError as e:
                    session.rollback()
                    return(False,str(e))    

            case 'update':
                try:
                    User = session.query(Usuario).filter(Usuario.id == id).first()

                    if User is None:
                        return (False, "Usuário  não encontrada.") 
                    
                    User.nome,nome, 
                    User.cpf=cpf, 
                    User.user=user,
                    User.senha=senha, 
                    User.ativo=ativo, 
                    User.reset_senha=reset_senha,
                    User.primeiro_acesso=primeiro_acesso, 
                    User.bloqueado=bloqueado, 
                    User.end_rua=end_rua,
                    User.end_numero=end_numero,
                    User.end_bairro=end_bairro,
                    User.end_complemento=end_complemento,
                    User.end_cep=end_cep,
                    User.end_cidade=end_cidade,
                    User.end_uf=end_uf,
                    User.celular=celular,
                    User.p_whats=p_whats,
                    User.telefone=telefone,
                    User.email=email,
                    User.obs=obs
                    
                    session.commit()
                    return (True, User.id)
            
                except Exception as e:
                    session.rollback()
                    return (False, str(e))  


    # def insert_tabler_entregas(km_inicial, km_final, km__lt, qt_entregas):
    #     try: 
    #         new_entrega = 

if __name__=='__main__':

#  app = Database.get_table_fornecedor(type='id', id=2)
    app = Database.delete_table_fornecedor(1)
    print(app)
