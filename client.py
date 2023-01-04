from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow

from server import GameServer
from network import Network

import threading

import sys


class MenuScreen(QMainWindow):
    """
    Main menu screen
    """
    def __init__(self):
        super(MenuScreen, self).__init__()
        loadUi("screens/menu.ui", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dungeon Buster')
        self.setFixedSize(900, 900)
        self.create_but.clicked.connect(self.create_lobby)
        self.connect_but.clicked.connect(self.connect_lobby)

    def create_lobby(self) -> None:
        """
        Find out the most appropriate photo for money amount
        """
        server = GameServer()
        thread1 = threading.Thread(target=server.start_server)
        thread1.start()
        lobby.lobby_ip.setText(f'Данные для входа (адрес):\n{server.server}:{server.port}')
        net = Network(server.server, server.port)
        menu.hide()
        lobby.show()

    def connect_lobby(self) -> None:
        """
        Find out the most appropriate photo for money amount
        """
        print('connect')


class LobbyScreen(QMainWindow):
    """
    Lobby screen
    """
    def __init__(self):
        super(LobbyScreen, self).__init__()
        loadUi("screens/lobby.ui", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dungeon Buster')
        self.setFixedSize(900, 900)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    menu = MenuScreen()
    lobby = LobbyScreen()

    menu.show()
    sys.exit(app.exec())
