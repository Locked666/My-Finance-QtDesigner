import sys
from PySide6.QtCore import Qt,QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QDialog,QVBoxLayout,QWidgetAction
from database import Database
from ui.MainLogin import Ui_Login
from ui.MainWindow import Ui_MainWindow
from ui.CadEmpresa import Ui_CadEmpresa
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
            self.verify_field(False,True)
            self.bnt_alterar.setEnabled(False)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)


    def callback_bnt_cancela(self):
        self.verify_field()
        self.bnt_alterar.setEnabled(True)
        self.bnt_salvar.setEnabled(False)
        self.bnt_adicionar.setEnabled(True)


        pass
    

    def callback_bnt_save(self):

        valores = self.get_value()
        
        # Pega apenas os valores preenchidos para 'text_ramo'
        ramo_values = [i.get('text_ramo') for i in valores if i.get('text_ramo')][0]
        
        # # Se você quiser pegar valores de várias chaves e filtrá-los, pode usar:
        # chaves = ['text_cnpj', 'Dt_abertura', 'text_ramo', 'text_nome_fantasia']  # Adicione outras chaves conforme necessário
        # valores_extraidos = {chave: [d.get(chave) for d in valores if d.get(chave)] for chave in chaves}
        
        # print("Valores de 'text_ramo' preenchidos:", ramo_values)
        # print("Valores extraídos (preenchidos):", valores_extraidos)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"My Finance {__version__}")

        
        self.actionEmpresa.triggered.connect(lambda: CadastroEmpresa().exec())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainLogin()
    window = AppLogin()
    window.show()
    sys.exit(app.exec())
