import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui.MainLogin import Ui_Login

class AppLogin(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(AppLogin,self).__init__()
        self.setupUi(self)
        self.usuario = self.text_usuario.text()
        self.senha = self.text_password.text()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainLogin()
    window = AppLogin()
    window.show()
    sys.exit(app.exec_())
