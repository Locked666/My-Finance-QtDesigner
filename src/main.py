import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui.MainLogin import Ui_Login
from ui.MainWindow import Ui_MainWindow
from ConfigApp import __version__

class AppLogin(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(AppLogin,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Login - My Finance {__version__}")

        self.bnt_entrar.clicked.connect(self.open_system)


    def open_system(self):
        if self.text_password.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()    



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"My Finance {__version__}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainLogin()
    window = AppLogin()
    window.show()
    sys.exit(app.exec_())
