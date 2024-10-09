import sys
from PySide6.QtCore import Qt,QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QDialog,QVBoxLayout,QWidgetAction
from ui_functions import consulta_cnpj
from database import Database
from ui.MainLogin import Ui_Login
from ui.MainWindow import Ui_MainWindow
from ui.CadEmpresa import Ui_CadEmpresa
from ui.CadFornecedor import Ui_CadFornecedor
from ui.dialogMensagem import Ui_InfMensagem


from ConfigApp import __version__

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

        self.label_version.setText(QCoreApplication.translate("AppLogin", __version__, None))

        self.bnt_entrar.clicked.connect(self.open_system)



    def open_system(self):
        if self.text_password.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()    


class CadastroEmpresa(QDialog,Ui_CadEmpresa):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro da Empresa - My Finance {__version__}")
        self.setupUi(self)
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
            self.check_optante,
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



        
        # Pega apenas os valores preenchidos para 'text_ramo'
        
        
        
        # # Se você quiser pegar valores de várias chaves e filtrá-los, pode usar:
        # chaves = ['text_cnpj', 'Dt_abertura', 'text_ramo', 'text_nome_fantasia']  # Adicione outras chaves conforme necessário
        # valores_extraidos = {chave: [d.get(chave) for d in valores if d.get(chave)] for chave in chaves}
        
        # print("Valores de 'text_ramo' preenchidos:", ramo_values)
        # print("Valores extraídos (preenchidos):", valores_extraidos)

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
        
class CadastroFornecedor(QDialog,Ui_CadFornecedor):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle(f"Cadastro de Fornecedor - My Finance {__version__}")
        self.setupUi(self)
        self.text_cnpj.editingFinished.connect(lambda c=True:self.on_cnpj_changed())
        self.text_cnpj.returnPressed.connect(lambda c=True:self.on_cnpj_changed())
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
            self.check_optante,
            self.check_p_whats,
            self.radio_fisica,
            self.radio_juridirica
        ]

        self.bnt_alterar.clicked.connect( self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancela)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_incluir)
        self.bnt_salvar.clicked.connect(self.callback_bnt_save)

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
            insert_fornecedor = Database.insert_table_fornecedor(
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

            

            if insert_fornecedor[0] == True:
                self.verify_field()
                self.lcd_id.setProperty(u"intValue", insert_fornecedor[1])
                self.bnt_salvar.setEnabled(False)
                self.bnt_alterar.setEnabled(True)
                self.bnt_adicionar.setEnabled(True)
                infmensagem = InfMensagem(mensagem=f"Empresa Adicionada com sucesso\n empresa código {insert_fornecedor[1]}")
                infmensagem.exec()

            else:
                infmensagem = InfMensagem(mensagem=f"Erro ao Gravar empresa\n {insert_fornecedor[1]}")
                infmensagem.exec()

        else:
            update_fornecedor = Database.update_table_fornecedor(
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

            

            if update_fornecedor[0] == True:
                self.verify_field()
                self.lcd_id.setProperty(u"intValue", update_fornecedor[1])
                self.bnt_salvar.setEnabled(False)
                self.bnt_alterar.setEnabled(True)
                self.bnt_adicionar.setEnabled(True)
                infmensagem = InfMensagem(mensagem=f"Empresa Adicionada com sucesso\n empresa código {update_fornecedor[1]}")
                infmensagem.exec()

            else:
                infmensagem = InfMensagem(mensagem=f"Erro ao Gravar empresa\n {update_fornecedor[1]}")
                infmensagem.exec()



        
        # Pega apenas os valores preenchidos para 'text_ramo'
        
        
        
        # # Se você quiser pegar valores de várias chaves e filtrá-los, pode usar:
        # chaves = ['text_cnpj', 'Dt_abertura', 'text_ramo', 'text_nome_fantasia']  # Adicione outras chaves conforme necessário
        # valores_extraidos = {chave: [d.get(chave) for d in valores if d.get(chave)] for chave in chaves}
        
        # print("Valores de 'text_ramo' preenchidos:", ramo_values)
        # print("Valores extraídos (preenchidos):", valores_extraidos)

    def populate_field(self):
        info = Database.get_table_fornecedor()

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

    def populate_field_consulta(self,nome:str, fantasia:str,abertura:str,natureza:str, logradouro:str, numero:str,complemento:str, municipio:str, bairro:str, uf:str, cep:str, email:str,telefone):
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
        self.text_cep.setText(cep.strip())
        self.text_email.insert(email.strip())
        


    def on_cnpj_changed(self,c=False):
        if c == False:
            id = self.lcd_id.value()
            if id == 0:
                if self.radio_juridirica.isChecked():
                    if len(self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/','')) == 14:
                        contulta = consulta_cnpj(self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/',''))
                    else:
                        infmensagem = InfMensagem(mensagem=f"Quantidade de Caracteres invalida\n cnpj:{self.text_cnpj.text().strip().replace('-','').replace('.','').replace('/','')}").exec()
                        return
                else:
                    infmensagem = InfMensagem(mensagem=f"Para Consulta de Cnpj, teve ser marcado como juridico ").exec()
                                            
    
        pass
 
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"My Finance {__version__}")

        
        self.actionEmpresa.triggered.connect(lambda: CadastroEmpresa().exec())
        self.actionFornecedor.triggered.connect(lambda: CadastroFornecedor().exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainLogin()
    window = AppLogin()
    window.text_password.insert(str(123))
    window.show()
    sys.exit(app.exec())
