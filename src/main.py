import sys
from PySide6.QtCore import Qt,QCoreApplication,QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QDialog,QVBoxLayout,QWidgetAction,QMdiSubWindow
from ui_functions import consulta_cnpj
from func_crypt import decrypt,encrypt
from database import Database
from import_display import *
from ConfigApp import __version__,MODE_DEBUG,SALT_CRYPT

class InfMensagem(QDialog,Ui_InfMensagem):
    def __init__(self,mensagem) -> None:
        super().__init__(parent=None)
        self.setupUi(self)
        self.mensagem= mensagem
        self.lb_inf.setText(QCoreApplication.translate("InfMensagem", self.mensagem, None))

class AppLogin(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(AppLogin,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Login - My Finance {__version__}")
        self.key = Database.get_table_sys_config()




        self.label_version.setText(QCoreApplication.translate("AppLogin", __version__, None))

        self.bnt_entrar.clicked.connect(self.open_system)


    def _get_user(self,usuario):
        user = Database.get_table_user(type='user', usuario=usuario)
        user_db =user[0][0]
        password =decrypt(user[0][1],self.key,SALT_CRYPT)
        ativo = user[0][2]
        reset = user[0][3]
        first_acess =user[0][4]
        locked = user[0][5] 
        return (user_db,password,ativo,reset,first_acess,locked)
        pass

    def open_system(self):
        
        if MODE_DEBUG:
            self.w = MainWindow()
            self.w.showMaximized()
            self.close()  
        else: 
            re_query = self._get_user(self.text_usuario.text().strip())
            if re_query[0] == self.text_usuario.text().strip() and re_query[1] == self.text_password.text().strip():
                if re_query[2] != 'S' or re_query[5] != 'N':
                    infmensagem = InfMensagem(mensagem="Não é possivel acessar com Usuário, verifique o cadastro").exec()
                    return   
                else:
                    self.w = MainWindow()
                    self.w.showMaximized()
                    self.close() 
        # if self.text_password.text() == '123':
        #     self.w = MainWindow()
        #     self.w.show()
        #     self.close()    

class CadatroUsuario(QWidget, Ui_CadUser):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro de Usuário - My Finance {__version__}")
        self.setupUi(self)

        self.bnt_alterar.clicked.connect( self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancela)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_incluir)
        self.bnt_excluir.clicked.connect(self.callback_bnt_delete)
        self.bnt_salvar.clicked.connect(self.callback_bnt_save)
        self.bnt_next.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next"))
        self.bnt_next_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next_full"))
        self.bnt_back_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back_full"))
        self.bnt_back.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back"))
        
        
        self.field_text = [
            self.text_nome,
            self.text_email,
            self.text_phone,
            self.text_cpf, 
            self.text_user, 
            self.text_password, 
            self.dt_nascimento, 
            self.plain_obs,
            self.plain_obs_adicionais,
            self.text_rua,
            self.text_numero,
            self.text_bairro,
            self.text_complementar,
            self.text_cep,
            self.text_cidade,
            self.text_uf,
            self.text_celular
        ]

        self.field_check = [
            self.check_add_cliente, 
            self.check_add_fornecedor, 
            self.check_first_acesso, 
            self.check_bloqueado, 
            self.check_reset_senha, 
            self.check_whats,
            self.check_ativo, 

        ]

        self.verify_field()
    def verify_field(self, read_text:bool = True, enabled_check:bool = False):

        for i in self.field_text:
            if i.isReadOnly() != read_text:
                i.setReadOnly(read_text)

        for e in self.field_check:
            if e.isEnabled() != enabled_check:
                e.setEnabled(enabled_check)

    def clear_field(self):
        for i in self.field_text:
            i.clear()
        pass

    def callback_bnt_cancela(self):
        label_id = self.lcd_id.value()
        if label_id == 0:
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.clear_field()
            self.populate_field()
            self.modal_seq_info(True)
        else:    
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.modal_seq_info(True)


        pass    

    def callback_bnt_alterar(self):
        
        label_id = self.lcd_id.value()
        if label_id != 0:
            self.verify_field(False,True)
            self.text_password.setText('')
            self.bnt_alterar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()
            
        else:
            infmensagem = InfMensagem(mensagem="Nenhuma Empresa Foi selecionada")
            infmensagem.exec()
            if infmensagem.accepted:
                self.verify_field(True,False)

    def modal_seq_info(self, form:bool = False):
        self.bnt_back.setEnabled(form)
        self.bnt_back_full.setEnabled(form)
        self.bnt_next.setEnabled(form)
        self.bnt_next_full.setEnabled(form)    

    def callback_bnt_incluir(self):
        if self.bnt_alterar.isEnabled() == True:
            self.clear_field()
            self.verify_field(False,True)
            self.lcd_id.setProperty(u"intValue", 0)
            self.bnt_alterar.setEnabled(False)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()

    def callback_bnt_delete(self):
        value_id = self.lcd_id.value()
        if value_id != 0:
            delete = Database.delete_table_user(int(value_id))
            if delete:
                infmensagem = InfMensagem(mensagem=f"Fornecedor: {int(value_id)} excluido com sucesso !").exec()
                self.clear_field()
                self.lcd_id.setProperty(u"intValue", 0)
                self.callback_bnt_seq_info(tipo='next')
            else:
                infmensagem = InfMensagem(mensagem=f"Errp ao excluir fornecedor: {value_id} \n Erro: {delete[1]} !").exec()    
            
    def callback_bnt_seq_info(self, tipo):
        value_in_db =  Database.get_table_user("list_id")
        value_id = self.lcd_id.value()
        self.lbl_total.setText(str(len(value_in_db)))

        match tipo:
            case "back":
                if value_id == 0:
                    return
                else:
                    if value_id == 0:
                        for i in value_in_db:
                            self.populate_field(id=i)
                            return
                    else:
                        if len(value_in_db) > 1: 

                            a = value_in_db.index(value_id)
                            a -= 1
                            try:
                                b = value_in_db[a]
                                self.populate_field(id=b)
                            except:
                                return   
            
            case "back_full":
                if value_id == 0:
                    return
                else:
                    self.populate_field(id=min(value_in_db))
            
            case "next":
                if value_id == 0:
                    for i in value_in_db:
                        self.populate_field(id=i)
                        return
                else:
                    if len(value_in_db) > 1: 

                        a = value_in_db.index(value_id)
                        a += 1
                        try:
                            b = value_in_db[a]
                            self.populate_field(id=b)
                        except:
                            return    


            case "next_full":
                if value_id == max(value_in_db):
                    return
                else:
                    self.populate_field(id=max(value_in_db))


        pass


    def callback_bnt_save(self):
        if self.text_nome.text().strip() == '':
            infmensagem = InfMensagem(mensagem="Campo Nome não pode estar vazio").exec()
            return
        
        if self.text_user.text().strip() =='':
            infmensagem = InfMensagem(mensagem="Campo Usuário não pode estar vazio").exec()
            return
        
        if self.text_password.text().strip() =='':
            infmensagem = InfMensagem(mensagem="Campo senha não pode estar vazio").exec()            
            return

        if self.lcd_id.value() == 0:
            try:
                insert_user = Database.insert_table_user(
                    nome=self.text_nome.text().strip(), 
                    cpf=self.text_cpf.text().strip().replace('.','').replace('-','').replace(' ',''), 
                    user=self.text_user.text().strip(),
                    senha=encrypt(self.text_password.text().strip(),Database.get_table_sys_config(),SALT_CRYPT), 
                    ativo='S' if self.check_ativo.isChecked() else 'N', 
                    reset_senha='S' if self.check_reset_senha.isChecked() else 'N',
                    primeiro_acesso='S' if self.check_first_acesso.isChecked() else 'N', 
                    bloqueado='S' if self.check_bloqueado.isChecked() else 'N', 
                    end_rua=self.text_rua.text().strip(),
                    end_numero=self.text_numero.text().strip(),
                    end_bairro=self.text_bairro.text().strip(),
                    end_complemento=self.text_complementar.text().strip(),
                    end_cep=self.text_cep.text().strip(),
                    end_cidade=self.text_cidade.text().strip(),
                    end_uf=self.text_uf.text().strip(),
                    celular=self.text_celular.text().replace('(','').replace(')','').replace('-','').strip(),
                    p_whats='S' if self.check_whats.isChecked() else 'N',
                    telefone=self.text_phone.text().replace('(','').replace(')','').replace('-','').strip(),
                    email=self.text_email.text().strip().lower(),
                    obs=self.plain_obs.toPlainText().strip()
                )
                
                if insert_user[0] == True:
                    self.verify_field()
                    self.lcd_id.setProperty(u"intValue", insert_user[1])
                    self.bnt_salvar.setEnabled(False)
                    self.bnt_alterar.setEnabled(True)
                    self.bnt_adicionar.setEnabled(True)
                    self.bnt_search.setEnabled(True)
                    self.bnt_excluir.setEnabled(True)
                    self.modal_seq_info(True)
                    infmensagem = InfMensagem(mensagem=f"Usuario Adicionada com sucesso\n Usuario código {insert_user[1]}").exec()
            except ValueError as e :
                infmensagem = InfMensagem(mensagem=f"Erro ao Salvar usuário\n Erro: {e}").exec()
        else:
            try:
                update_user = Database.insert_table_user(
                    id=self.lcd_id.value(),
                    type='update',
                    nome=self.text_nome.text().strip(), 
                    cpf=self.text_cpf.text().strip().replace('.','').replace('-','').replace(' ',''), 
                    user=self.text_user.text().strip(),
                    senha=encrypt(self.text_password.text().strip(),Database.get_table_sys_config(),SALT_CRYPT), 
                    ativo='S' if self.check_ativo.isChecked() else 'N', 
                    reset_senha='S' if self.check_reset_senha.isChecked() else 'N',
                    primeiro_acesso='S' if self.check_first_acesso.isChecked() else 'N', 
                    bloqueado='S' if self.check_bloqueado.isChecked() else 'N', 
                    end_rua=self.text_rua.text().strip(),
                    end_numero=self.text_numero.text().strip(),
                    end_bairro=self.text_bairro.text().strip(),
                    end_complemento=self.text_complementar.text().strip(),
                    end_cep=self.text_cep.text().strip(),
                    end_cidade=self.text_cidade.text().strip(),
                    end_uf=self.text_uf.text().strip(),
                    celular=self.text_celular.text().replace('(','').replace(')','').replace('-','').strip(),
                    p_whats='S' if self.check_whats.isChecked() else 'N',
                    telefone=self.text_phone.text().replace('(','').replace(')','').replace('-','').strip(),
                    email=self.text_email.text().strip().lower(),
                    obs=self.plain_obs.toPlainText().strip()
                )
                
                if update_user[0] == True:
                    self.verify_field()
                    self.lcd_id.setProperty(u"intValue", update_user[1])
                    self.bnt_salvar.setEnabled(False)
                    self.bnt_alterar.setEnabled(True)
                    self.bnt_adicionar.setEnabled(True)
                    self.bnt_search.setEnabled(True)
                    self.bnt_excluir.setEnabled(True)
                    self.modal_seq_info(True)
                    infmensagem = InfMensagem(mensagem=f"Usuario Adicionada com sucesso\n Usuario código {update_user[1]}").exec()
            except ValueError as e :
                infmensagem = InfMensagem(mensagem=f"Erro ao Salvar usuário\n Erro: {e}").exec()        
                    
    def populate_field(self, id:int =  None):
        if id == None:
            info = Database.get_table_user()
        else:
            self.clear_field()
            info = Database.get_table_user(type='id',id=id)   
        if len(info) > 0 :
            info = info[0]
            self.lcd_id.setProperty(u"intValue", info[0])
            self.text_nome.setText(info[1])
            self.text_cpf.setText(info[2])
            self.text_user.setText(info[3])
            self.text_password.insert('*****')
            self.text_rua.setText(info[8])
            self.text_numero.setText(info[9])
            self.text_bairro.setText(info[10])
            self.text_complementar.setText(info[11])
            self.text_cep.setText(info[12])
            self.text_cidade.setText(info[13])
            self.text_uf.setText(info[14])
            self.text_celular.setText(info[15])
            self.text_phone.setText(info[17])
            self.text_email.setText(info[18])
            self.plain_obs.insertPlainText(info[19])

            if info[6] == 'S':
                self.check_bloqueado.setChecked(True)
            else:     
                self.check_bloqueado.setChecked(False)

            if info[5] == 'S':
                self.check_first_acesso.setChecked(True)
            else:     
                self.check_first_acesso.setChecked(False)

            if info[4] == 'S':
                self.check_reset_senha.setChecked(True)
            else:     
                self.check_reset_senha.setChecked(False)

            if info[3] == 'S':
                self.check_ativo.setChecked(True)
            else:     
                self.check_ativo.setChecked(False)

class CadastroEmpresa(QDialog,Ui_CadEmpresa):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro da Empresa - My Finance {__version__}")
        self.setupUi(self)
        if MODE_DEBUG == False:
            self.populate_field()

        self.field_text =  [
            self.text_cnpj,
            self.Dt_abertura,
            self.text_razao_social,
            self.text_nome_fantasia,
            self.text_IE,
            self.text_IM,
            self.text_ramo,
            self.text_rua,
            self.text_numero,
            self.text_bairro,
            self.text_complementar,
            self.text_cep,
            self.text_cidade,
            self.text_uf,
            self.text_celular,
            self.text_telefone,
            self.text_email,
            self.plain_text
        ]
        
        self.field_check = [
            self.check_contribuinte,
            self.check_p_whats,
            self.radio_fisica,
            self.radio_juridirica
        ]

        self.bnt_alterar.clicked.connect(self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancela)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_incluir)
        self.bnt_salvar.clicked.connect(self.callback_bnt_save)

    def get_value(self):
        value = []

        for i in self.field_text:
            if i.objectName() != 'plain_text':
                a = {i.objectName():i.text()}
            else:
                a = {i.objectName():i.toPlainText()}    
            value.append(a)

        return value    

    def verify_field(self, read_text:bool = True, enabled_check:bool = False):

        for i in self.field_text:
            if i.isReadOnly() != read_text:
                i.setReadOnly(read_text)

        for e in self.field_check:
            if e.isEnabled() != enabled_check:
                e.setEnabled(enabled_check)

    def clear_field(self):
        for i in self.field_text:
            i.clear()
        pass

    def callback_bnt_alterar(self):
        
        label_id = self.lcd_id.value()
        if label_id != 0:
            self.verify_field(False,True)
            self.bnt_alterar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_adicionar.setEnabled(False)
            
        else:
            infmensagem = InfMensagem(mensagem="Nenhuma Empresa Foi selecionada")
            infmensagem.exec()
            if infmensagem.accepted:
                self.verify_field(True,False)
            
    def callback_bnt_incluir(self):
        if self.bnt_alterar.isEnabled() == True:
            self.clear_field()
            self.verify_field(False,True)
            self.lcd_id.setProperty(u"intValue", 0)
            self.bnt_alterar.setEnabled(False)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)

    def callback_bnt_cancela(self):
        label_id = self.lcd_id.value()
        if label_id == 0:
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.clear_field()
            self.populate_field()
        else:    
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)


        pass

    def callback_bnt_save(self):

        valores = self.get_value()
        value_cnpj = [i.get('text_cnpj') for i in valores if i.get('text_cnpj')]
        value_razao = [i.get('text_razao_social') for i in valores if i.get('text_razao_social')]

        if len(value_cnpj) ==  0:
            infmensagem = InfMensagem(mensagem="Campo Cnpj/cpf não pode estar vazio")
            infmensagem.exec()
            return
        
        if len(value_razao) ==  0:
            infmensagem = InfMensagem(mensagem="Campo Razão social não pode estar vazio")
            infmensagem.exec()
            return

        if self.lcd_id.value() == 0:
            insert_empresa = Database.insert_table_empresa(
                cnpj=self.text_cnpj.text().replace('.','').replace('-','').strip(),
                razao = self.text_razao_social.text().strip().upper() ,
                nome_fantasia=self.text_nome_fantasia.text().strip().upper(),
                pj='J' if self.radio_juridirica.isChecked() else 'F',
                # dt_abertura =self.Dt_abertura.text() ,
                IE =  self.text_IE.text().strip(),
                IM= self.text_IM.text().strip(),
                contribuinte = 'S' if self.check_contribuinte.isChecked() else 'N',
                simples='S' if self.check_optante.isChecked() else 'N',
                ramo= self.text_ramo.text().strip().upper(),
                rua =self.text_rua.text().strip(),
                numero =  self.text_numero.text().strip(),
                bairro = self.text_bairro.text().strip(),
                complemento =  self.text_complementar.text().strip(),
                cep = self.text_cep.text().replace('-','').strip(),
                cidade =  self.text_cidade.text().strip(),
                uf = self.text_uf.text().strip(),
                celular = self.text_celular.text().replace('(','').replace(')','').replace('-','').strip(),
                whats='S' if self.check_p_whats.isChecked() else 'N',
                telefone= self.text_telefone.text().replace('(','').replace(')','').replace('-','').strip(),
                email=self.text_email.text().strip().lower(),
                obs = self.plain_text.toPlainText().strip()
            )

            

            if insert_empresa[0] == True:
                self.verify_field()
                self.lcd_id.setProperty(u"intValue", insert_empresa[1])
                self.bnt_salvar.setEnabled(False)
                self.bnt_alterar.setEnabled(True)
                self.bnt_adicionar.setEnabled(True)
                infmensagem = InfMensagem(mensagem=f"Empresa Adicionada com sucesso\n empresa código {insert_empresa[1]}")
                infmensagem.exec()

            else:
                infmensagem = InfMensagem(mensagem=f"Erro ao Gravar empresa\n {insert_empresa[1]}")
                infmensagem.exec()

        else:
            update_empresa = Database.update_table_empresa(
                id = self.lcd_id.value(),
                cnpj=self.text_cnpj.text().replace('.','').replace('-','').strip(),
                razao = self.text_razao_social.text().strip().upper() ,
                nome_fantasia=self.text_nome_fantasia.text().strip().upper(),
                pj='J' if self.radio_juridirica.isChecked() else 'F',
                # dt_abertura =self.Dt_abertura.text() ,
                IE =  self.text_IE.text().strip(),
                IM= self.text_IM.text().strip(),
                contribuinte = 'S' if self.check_contribuinte.isChecked() else 'N',
                simples='S' if self.check_optante.isChecked() else 'N',
                ramo= self.text_ramo.text().strip().upper(),
                rua =self.text_rua.text().strip(),
                numero =  self.text_numero.text().strip(),
                bairro = self.text_bairro.text().strip(),
                complemento =  self.text_complementar.text().strip(),
                cep = self.text_cep.text().replace('-','').strip(),
                cidade =  self.text_cidade.text().strip(),
                uf = self.text_uf.text().strip(),
                celular = self.text_celular.text().replace('(','').replace(')','').replace('-','').strip(),
                whats='S' if self.check_p_whats.isChecked() else 'N',
                telefone= self.text_telefone.text().replace('(','').replace(')','').replace('-','').strip(),
                email=self.text_email.text().strip().lower(),
                obs = self.plain_text.toPlainText().strip()
            )

            

            if update_empresa[0] == True:
                self.verify_field()
                self.lcd_id.setProperty(u"intValue", update_empresa[1])
                self.bnt_salvar.setEnabled(False)
                self.bnt_alterar.setEnabled(True)
                self.bnt_adicionar.setEnabled(True)
                infmensagem = InfMensagem(mensagem=f"Empresa Adicionada com sucesso\n empresa código {update_empresa[1]}")
                infmensagem.exec()

            else:
                infmensagem = InfMensagem(mensagem=f"Erro ao Gravar empresa\n {update_empresa[1]}")
                infmensagem.exec()

    def populate_field(self):
        info = Database.get_table_empresa()[0]
        self.lcd_id.setProperty(u"intValue", info[0])
        self.text_cnpj.insert(info[3])
        self.text_razao_social.insert(info[1])
        self.text_nome_fantasia.insert(info[2])
        self.text_IE.insert(info[6])
        self.text_IM.insert(info[7])
        self.text_ramo.insert(info[10])
        self.text_rua.insert(info[11])
        self.text_numero.insert(str(info[12]))
        self.text_bairro.insert(info[13])
        self.text_complementar.insert(info[14])
        self.text_cep.insert(info[15])
        self.text_cidade.insert(info[16])
        self.text_uf.insert(info[17])
        # self.text_celular.insert(info[18])
        self.text_telefone.setText(info[20])
        self.text_email.insert(info[21])
        self.plain_text.insertPlainText(info[22])
        self.text_celular.setText(info[18])

        if info[8] == 'S':
            self.check_contribuinte.setChecked(True)
        if info[9] == 'S' :
            self.check_optante.setChecked(True)
        if info[19] == 'S':    
            self.check_p_whats.setChecked(True)
        if info[4] == 'J': 
            self.radio_juridirica.setChecked(True)
        else:       
            self.radio_fisica.setChecked(True)
        
class CadastroFornecedor(QWidget,Ui_CadFornecedor):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro de Fornecedor - My Finance {__version__}")
        self.setupUi(self)
        self.text_cnpj.editingFinished.connect(lambda c=True:self.on_cnpj_changed())


        self.field_text =  [
            self.text_cnpj,
            self.Dt_abertura,
            self.text_razao_social,
            self.text_nome_fantasia,
            self.text_IE,
            self.text_IM,
            self.text_ramo,
            self.text_rua,
            self.text_numero,
            self.text_bairro,
            self.text_complementar,
            self.text_cep,
            self.text_cidade,
            self.text_uf,
            self.text_celular,
            self.text_telefone,
            self.text_email,
            self.plain_text
        ]
        
        self.field_check = [
            self.check_contribuinte,
            self.check_optante,
            self.check_p_whats,
            self.check_ativo,
            self.radio_fisica,
            self.radio_juridirica
        ]

        self.bnt_alterar.clicked.connect( self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancela)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_incluir)
        self.bnt_excluir.clicked.connect(self.callback_bnt_delete)
        self.bnt_salvar.clicked.connect(self.callback_bnt_save)
        self.bnt_consulta_cnpj.clicked.connect(lambda c=True: self.on_cnpj_changed(return_bnt=True))
        self.bnt_next.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next"))
        self.bnt_next_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next_full"))
        self.bnt_back_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back_full"))
        self.bnt_back.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back"))
        

    def get_value(self):
        value = []

        for i in self.field_text:
            if i.objectName() != 'plain_text':
                a = {i.objectName():i.text()}
                # a = dict(i.objectName(),i.text())
            else:
                a = {i.objectName():i.toPlainText()}    
                # a = dict(i.objectName(),i.toPlainText())
            value.append(a)
        
        # for item in value:
        #     for chave, valor in item.items():
        #         print(f"{chave}: {valor}")

        return value    

    def verify_field(self, read_text:bool = True, enabled_check:bool = False):

        for i in self.field_text:
            if i.isReadOnly() != read_text:
                i.setReadOnly(read_text)

        for e in self.field_check:
            if e.isEnabled() != enabled_check:
                e.setEnabled(enabled_check)

    def clear_field(self):
        for i in self.field_text:
            i.clear()
        pass

    def callback_bnt_alterar(self):
        
        label_id = self.lcd_id.value()
        if label_id != 0:
            self.verify_field(False,True)
            self.bnt_alterar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()
            
        else:
            infmensagem = InfMensagem(mensagem="Nenhuma Empresa Foi selecionada")
            infmensagem.exec()
            if infmensagem.accepted:
                self.verify_field(True,False)

    def modal_seq_info(self, form:bool = False):
        self.bnt_back.setEnabled(form)
        self.bnt_back_full.setEnabled(form)
        self.bnt_next.setEnabled(form)
        self.bnt_next_full.setEnabled(form)
    

    def callback_bnt_incluir(self):
        if self.bnt_alterar.isEnabled() == True:
            self.clear_field()
            self.verify_field(False,True)
            self.lcd_id.setProperty(u"intValue", 0)
            self.bnt_alterar.setEnabled(False)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()

    def callback_bnt_cancela(self):
        label_id = self.lcd_id.value()
        if label_id == 0:
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.clear_field()
            self.populate_field()
            self.modal_seq_info(True)
        else:    
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.modal_seq_info(True)


        pass

    def callback_bnt_save(self):

        valores = self.get_value()
        value_cnpj = [i.get('text_cnpj') for i in valores if i.get('text_cnpj')]
        value_razao = [i.get('text_razao_social') for i in valores if i.get('text_razao_social')]

        if len(value_cnpj) ==  0:
            infmensagem = InfMensagem(mensagem="Campo Cnpj/cpf não pode estar vazio")
            infmensagem.exec()
            return
        
        if len(value_razao) ==  0:
            infmensagem = InfMensagem(mensagem="Campo Razão social não pode estar vazio")
            infmensagem.exec()
            return

        if self.lcd_id.value() == 0:
            v =  Database.get_table_fornecedor(type='cnpj', cnpj = (self.text_cnpj.text().replace('.','').replace('-','').strip()))
            if len(v) == 0:
                insert_fornecedor = Database.insert_table_fornecedor(
                    cnpj=self.text_cnpj.text().replace('.','').replace('-','').strip(),
                    razao = self.text_razao_social.text().strip().upper() ,
                    nome_fantasia=self.text_nome_fantasia.text().strip().upper(),
                    ativo='S' if self.check_ativo.isChecked() else 'N',
                    pj='J' if self.radio_juridirica.isChecked() else 'F',
                    # dt_abertura =self.Dt_abertura.text() ,
                    IE =  self.text_IE.text().strip(),
                    IM= self.text_IM.text().strip(),
                    contribuinte = 'S' if self.check_contribuinte.isChecked() else 'N',
                    simples='S' if self.check_optante.isChecked() else 'N',
                    ramo= self.text_ramo.text().strip().upper(),
                    rua =self.text_rua.text().strip(),
                    numero =  self.text_numero.text().strip(),
                    bairro = self.text_bairro.text().strip(),
                    complemento =  self.text_complementar.text().strip(),
                    cep = self.text_cep.text().replace('-','').strip(),
                    cidade =  self.text_cidade.text().strip(),
                    uf = self.text_uf.text().strip(),
                    celular = self.text_celular.text().replace('(','').replace(')','').replace('-','').strip(),
                    whats='S' if self.check_p_whats.isChecked() else 'N',
                    telefone= self.text_telefone.text().replace('(','').replace(')','').replace('-','').strip(),
                    email=self.text_email.text().strip().lower(),
                    obs = self.plain_text.toPlainText().strip()
                )

                

                if insert_fornecedor[0] == True:
                    self.verify_field()
                    self.lcd_id.setProperty(u"intValue", insert_fornecedor[1])
                    self.bnt_salvar.setEnabled(False)
                    self.bnt_alterar.setEnabled(True)
                    self.bnt_adicionar.setEnabled(True)
                    self.bnt_search.setEnabled(True)
                    self.bnt_excluir.setEnabled(True)
                    self.modal_seq_info(True)
                    infmensagem = InfMensagem(mensagem=f"Fornecedor Adicionada com sucesso\n empresa código {insert_fornecedor[1]}")
                    infmensagem.exec()

                else:
                    infmensagem = InfMensagem(mensagem=f"Erro ao Gravar empresa\n {insert_fornecedor[1]}")
                    infmensagem.exec()

            else:
                infmensagem = InfMensagem(mensagem=f"Fornecedor já cadastrado no código: {v[0][0]}").exec()


        else:
            update_fornecedor = Database.update_table_fornecedor(
                id = self.lcd_id.value(),
                cnpj=self.text_cnpj.text().replace('.','').replace('-','').strip(),
                razao = self.text_razao_social.text().strip().upper() ,
                nome_fantasia=self.text_nome_fantasia.text().strip().upper(),
                ativo='S' if self.check_ativo.isChecked() else 'N',
                pj='J' if self.radio_juridirica.isChecked() else 'F',
                # dt_abertura =self.Dt_abertura.text() ,
                IE =  self.text_IE.text().strip(),
                IM= self.text_IM.text().strip(),
                contribuinte = 'S' if self.check_contribuinte.isChecked() else 'N',
                simples='S' if self.check_optante.isChecked() else 'N',
                ramo= self.text_ramo.text().strip().upper(),
                rua =self.text_rua.text().strip(),
                numero =  self.text_numero.text().strip(),
                bairro = self.text_bairro.text().strip(),
                complemento =  self.text_complementar.text().strip(),
                cep = self.text_cep.text().replace('-','').strip(),
                cidade =  self.text_cidade.text().strip(),
                uf = self.text_uf.text().strip(),
                celular = self.text_celular.text().replace('(','').replace(')','').replace('-','').strip(),
                whats='S' if self.check_p_whats.isChecked() else 'N',
                telefone= self.text_telefone.text().replace('(','').replace(')','').replace('-','').strip(),
                email=self.text_email.text().strip().lower(),
                obs = self.plain_text.toPlainText().strip()
            )

            

            if update_fornecedor[0] == True:
                self.verify_field()
                self.lcd_id.setProperty(u"intValue", update_fornecedor[1])
                self.bnt_salvar.setEnabled(False)
                self.bnt_alterar.setEnabled(True)
                self.bnt_adicionar.setEnabled(True)
                self.bnt_search.setEnabled(True)
                self.bnt_excluir.setEnabled(True)
                self.modal_seq_info(True)
                infmensagem = InfMensagem(mensagem=f"Fornecedor Adicionada com sucesso\n empresa código {update_fornecedor[1]}")
                infmensagem.exec()

            else:
                infmensagem = InfMensagem(mensagem=f"Erro ao Gravar Fornecedor\n {update_fornecedor[1]}")
                infmensagem.exec()

    def populate_field(self, id:int =  None):
        if id == None:
            info = Database.get_table_fornecedor()
        else:
            self.clear_field()
            info = Database.get_table_fornecedor(type='id',id=id)   
        if len(info) > 0 :
            info = info[0]
            self.lcd_id.setProperty(u"intValue", info[0])
            self.text_cnpj.insert(info[3])
            self.text_razao_social.insert(info[1])

            self.text_nome_fantasia.insert(info[2])
            self.text_IE.insert(info[6])
            self.text_IM.insert(info[7])
            self.text_ramo.insert(info[10])
            self.text_rua.insert(info[11])
            self.text_numero.insert(str(info[12]))
            self.text_bairro.insert(info[13])
            self.text_complementar.insert(info[14])
            self.text_cep.insert(info[15])
            self.text_cidade.insert(info[16])
            self.text_uf.insert(info[17])
            # self.text_celular.insert(info[18])
            self.text_telefone.setText(info[20])
            self.text_email.insert(info[21])
            self.plain_text.insertPlainText(info[22])
            self.text_celular.setText(info[18])

            if info[8] == 'S':
                self.check_contribuinte.setChecked(True)
            if info[9] == 'S' :
                self.check_optante.setChecked(True)
            if info[19] == 'S':    
                self.check_p_whats.setChecked(True)
            if info[4] == 'J': 
                self.radio_juridirica.setChecked(True)
            else:       
                self.radio_fisica.setChecked(True)

    def populate_field_consulta(self,nome:str, fantasia:str,abertura:str,natureza:str, logradouro:str, numero:str,complemento:str, municipio:str, bairro:str, uf:str, cep:str, email:str,telefone:str):
        self.text_razao_social.insert(nome.strip())
        self.text_nome_fantasia.insert(fantasia.strip())
        # self.Dt_abertura.
        self.text_ramo.insert(natureza.strip())
        self.text_rua.insert(logradouro.strip())
        self.text_numero.setText(numero.strip())
        self.text_complementar.insert(complemento.strip())
        self.text_cidade.insert(municipio.strip())
        self.text_bairro.insert(bairro.strip())
        self.text_uf.insert(uf.strip())
        self.text_cep.setText(cep.strip().replace('-','').replace('.','').replace('/',''))
        self.text_email.insert(email.strip())
        self.text_telefone.setText(telefone.strip().replace('-','').replace('.','').replace('(','').replace(')',''))        

    def callback_bnt_seq_info(self, tipo):
        value_in_db =  Database.get_table_fornecedor("list_id")
        value_id = self.lcd_id.value()
        self.lbl_total.setText(str(len(value_in_db)))
        

        match tipo:
            case "back":
                if value_id == 0:
                    return
                else:
                    if value_id == 0:
                        for i in value_in_db:
                            self.populate_field(id=i)
                            return
                    else:
                        if len(value_in_db) > 1: 

                            a = value_in_db.index(value_id)
                            a -= 1
                            try:
                                b = value_in_db[a]
                                self.populate_field(id=b)
                            except:
                                return   
            
            case "back_full":
                if value_id == 0:
                    return
                else:
                    self.populate_field(id=min(value_in_db))
            
            case "next":
                if value_id == 0:
                    for i in value_in_db:
                        self.populate_field(id=i)
                        return
                else:
                    if len(value_in_db) > 1: 

                        a = value_in_db.index(value_id)
                        a += 1
                        try:
                            b = value_in_db[a]
                            self.populate_field(id=b)
                        except:
                            return    


            case "next_full":
                if value_id == max(value_in_db):
                    return
                else:
                    self.populate_field(id=max(value_in_db))


        pass
    
    def callback_bnt_delete(self):
        value_id = self.lcd_id.value()
        if value_id != 0:
            delete = Database.delete_table_fornecedor(int(value_id))
            if delete:
                infmensagem = InfMensagem(mensagem=f"Fornecedor: {int(value_id)} excluido com sucesso !").exec()
                self.clear_field()
                self.lcd_id.setProperty(u"intValue", 0)
                self.callback_bnt_seq_info(tipo='next')
            else:
                infmensagem = InfMensagem(mensagem=f"Errp ao excluir fornecedor: {value_id} \n Erro: {delete[1]} !").exec()    
            

        pass

    def on_cnpj_changed(self,c=False,return_bnt = False):
        if self.text_cnpj.text().strip():
            id = self.lcd_id.value()
            if id == 0:
                if self.radio_juridirica.isChecked():
                    if len(self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/','')) == 14:
                        cn = self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/','')
                        consulta = consulta_cnpj(self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/',''))
                        self.clear_field()
                        self.text_cnpj.setText(cn)
                        self.populate_field_consulta(
                            nome=consulta[0],
                            fantasia=consulta[1],
                            abertura=consulta[2],
                            natureza=consulta[3],
                            logradouro=consulta[4],
                            numero=consulta[5],
                            complemento=consulta[6],
                            bairro=consulta[7],
                            municipio=consulta[8],
                            uf=consulta[9],
                            cep=consulta[10],
                            email=consulta[11],
                            telefone=consulta[12]

                        )
                        
                    else:
                        infmensagem = InfMensagem(mensagem=f"Quantidade de Caracteres invalida\n cnpj:{self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/','')}").exec()
                        
                        
                        return
                else:
                    if return_bnt:
                        infmensagem = InfMensagem(mensagem=f"Para Consulta de Cnpj, teve ser marcado como juridico ").exec()
        else: 
            if return_bnt ==  True and self.radio_juridirica.isChecked():
                infmensagem = InfMensagem(mensagem=f"O Campo de CNPJ Não pode estar vazio.").exec()

    
        pass

class CadastroRamoAtividade(QWidget,Ui_dialogRamoAtividade):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro de Ramo de Atividade- My Finance {__version__}")
        self.setupUi(self)
        
        self.bnt_alterar.clicked.connect(self.callback_bnt_alterar)
        self.bnt_incluir.clicked.connect(self.callback_bnt_incluir)
        
    
    def callback_bnt_alterar(self):
        lbl = self.lcd_id.value()
        if lbl == 0 :
            self.text_codigo.setReadOnly(False)
            self.plain_descricao.setReadOnly(False)      
            self.bnt_alterar.setEnabled(False)
            self.bnt_incluir.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_pesquisar.setEnabled(False)
        
        
    def callback_bnt_incluir(self):
        self.text_codigo.clear()
        self.plain_descricao.clear()
        self.lcd_id.setProperty(u"intValue", 0)
        self.text_codigo.setReadOnly(False)
        self.plain_descricao.setReadOnly(False) 
        self.bnt_alterar.setEnabled(False)
        self.bnt_incluir.setEnabled(False)
        self.bnt_salvar.setEnabled(True)
        self.bnt_pesquisar.setEnabled(False)          

# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self) -> None:
#         super(MainWindow,self).__init__()
#         self.setupUi(self)
#         self.setWindowTitle(f"My Finance {__version__}")
#         self.rm = CadastroRamoAtividade()
     
#         self.actionEmpresa.triggered.connect(lambda: CadastroEmpresa().exec())
#         self.actionFornecedor.triggered.connect(lambda: CadastroFornecedor().exec())
#         self.actionRamo_Atividade.triggered.connect(lambda: self.mdi_center.addSubWindow(self.rm))
#         # self.actionRamo_Atividade.triggered.connect(lambda: CadastroRamoAtividade().exec())
#         self.actionCadUser.triggered.connect(lambda: CadatroUsuario().exec())

class FrmDashboard(QWidget,Ui_frm_dashboard):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setupUi(self)
        # self.setWindowTitle(f"My Finance {__version__}")

class CadastroEntregas(QDialog,Ui_CadEntregas):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro de Entregas - My Finance {__version__}")
        self.setupUi(self)
        
        self.bnt_salvar.clicked.connect(self.callback_bnt_save)
        
       
    def clear_field(self):
        self.text_km_final.clear()
        self.text_km_inicial.clear()
        self.text_km_media.clear()
        self.text_qt_entregas.clear()
        self.text_vlr_final.clear()
        
    def callback_bnt_save(self):
        if float(self.text_km_inicial.text().strip()) > float(self.text_km_final.text().strip()):
            infmensagem = InfMensagem(mensagem=f"Valor do km Final, não pode ser menor que o km incial").exec()
            return
        
            
        
        new_entregas = Database.insert_table_entregas(
            data = self.dateEdit.text(),
            km_inicial = self.text_km_inicial.text().strip(), 
            km_final = self.text_km_final.text().strip(), 
            km__lt = self.text_km_media.text().strip(),
            qt_entregas = self.text_qt_entregas.text().strip(),
            valor_final =  self.text_vlr_final.text().strip()                
        )
        if new_entregas[0]:
            infmensagem = InfMensagem(mensagem=f"Entrega Adicionada com sucesso\n Entrega código {new_entregas[1]}").exec()
            self.clear_field()
        else: 
            infmensagem = InfMensagem(mensagem=f"Erro ao adicionar Entrega \n erro  {new_entregas[1]}").exec()
                
        


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"My Finance {__version__}")
        # Inicializa o atributo para armazenar a instância do dashboard e do MDI
        self.apply_stylesheet()
        self.dashboard_window = None
        self.dashboard_subwindow = None
        

        # Constrói a instância do widget a ser adicionado ao MDI
        self.actionEmpresa.triggered.connect(lambda: CadastroEmpresa().exec())
        self.actionFornecedor.triggered.connect(lambda: self.open_mdi_center(CadastroFornecedor(),"Cadastro de Fornecedor"))
        self.actionRamo_Atividade.triggered.connect(lambda : self.open_mdi_center(CadastroRamoAtividade(),"Cadastro de Ramo de atividade"))
        self.actionCadUser.triggered.connect(lambda:self.open_mdi_center(CadatroUsuario(),"Cadastro de Usuário") )
        self.bnt_left_dashboard.clicked.connect(self.open_dashboard )
        self.actionLancarDia.triggered.connect(lambda: CadastroEntregas().exec())

    def open_dashboard(self):
        # Se já existe uma instância do dashboard, fecha-a
        if self.dashboard_subwindow:
            self.dashboard_subwindow.close()
        
        # Cria uma nova instância do FrmDashboard
        self.dashboard_window = FrmDashboard()
        self.dashboard_subwindow = QMdiSubWindow()
        self.dashboard_subwindow.setWidget(self.dashboard_window)
        self.dashboard_subwindow.setWindowTitle(f"Dashboard")
        self.mdi_center.addSubWindow(self.dashboard_subwindow)
        
        # Mostra a subjanela maximizada
        self.dashboard_subwindow.showMaximized()
        self.dashboard_subwindow.setAttribute(Qt.WA_DeleteOnClose)  # Garante que a instância seja removida ao fechar

        # Reseta a referência ao fechar
        self.dashboard_subwindow.destroyed.connect(lambda: self.reset_dashboard_references())

    def reset_dashboard_references(self):
        self.dashboard_window = None
        self.dashboard_subwindow = None


    def open_mdi_center(self,widget,title = ''):
        # Cria uma nova instância do widget
        mdi_widget = widget
        # Cria uma subjanela MDI
        sub_window = QMdiSubWindow()
        sub_window.setWidget(mdi_widget)
        sub_window.setWindowTitle(f"{title} - My Finance {__version__} ")
        # Adiciona a subjanela ao MDI
        self.mdi_center.addSubWindow(sub_window)
        # Mostra a subjanela
        sub_window.show()

    def apply_stylesheet(self, stylesheet_path='D:\Desenvolvimento\python\My-Finance-QtDesigner\src\stylesheets.qss'):
        file = QFile(stylesheet_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = file.readAll().data().decode("utf-8")
            app.setStyleSheet(stream)
        file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #window = MainWindow()
    window = AppLogin()
    window.show()
    sys.exit(app.exec())
