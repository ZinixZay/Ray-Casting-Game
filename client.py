import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
import threading


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("screens/menu.ui", self)

        self.create_but.clicked.connect(self.create_lobby)
        self.connect_but.clicked.connect(self.connect_lobby)

    @staticmethod
    def create_lobby():
        menu.hide()
        lobby.show()
        lobby.host_lobby()

    def connect_lobby(self):
        name, done1 = QInputDialog.getText(self, 'Connect lobby', 'Enter host ip adress:')


class LobbyScreen(QMainWindow):
    def __init__(self):
        super(LobbyScreen, self).__init__()
        loadUi("screens/lobby.ui", self)

        self.ip_line.setEnabled(False)
        self.players_text.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    menu = MainScreen()
    lobby = LobbyScreen()

    menu.show()
    sys.exit(app.exec())
