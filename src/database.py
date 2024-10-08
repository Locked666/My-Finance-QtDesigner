from model import Empresa, CONN, Base,engine,session



class Database():
    def __init__(self) -> None:
        super().__init__()

    def insert_table_empresa(self,cnpj:str,razao:str ,nome_fantasia:str=None,pj:str='j',
                             dt_abertura:str ='',IE:str='',IM:str ='',contribuinte:str = 'N',simples:str = 'N',ramo:str='',rua:str='',numero:int=0,
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


