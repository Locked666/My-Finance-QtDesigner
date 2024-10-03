import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from MainWindow import Ui_MainWindow  # Altere o nome conforme necessário
# from MainLogin import Ui_MainLogin
from ui.MainWindow import Ui_MainWindow
from ui.MainLogin import Ui_MainLogin

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class MainLogin(QMainWindow):
    def __init__(self):
        super(MainLogin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainLogin()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
