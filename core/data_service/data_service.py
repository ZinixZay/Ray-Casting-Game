import json
from paths import DATA_PATH


class DataService:
    """
    Service that lets to save game, save info about the game. anything
    """
    def __init__(self, path: str = f"{DATA_PATH}data.json"):
        """
        self.data - current data connected to class
        :param path: path of json file where data be saved
        """
        self.data = {}
        self.path = path

    def save_data(self, head: str, body) -> None:
        """
        Saves piece of data in json
        :param head: head of the piece
        :param body: body of the piece
        :return:
        """
        self.update_data()
        self.data[head] = body
        dumped_data = json.dumps(self.data)
        with open(self.path, 'w') as f:
            f.write(dumped_data)

    def update_data(self) -> None:
        """
        Updates current data
        :return:
        """
        with open(self.path) as f:
            self.data = json.load(f)

    def get_data(self, head: str):
        """
        Finds piece of data by head
        :param head: head of the piece
        :return: body of the piece
        """
        self.update_data()
        if head in self.data.keys():
            return self.data[head]

    def get_all_data(self) -> dict:
        """
        Takes all data
        :return: all existing data
        """
        self.update_data()
        return self.data

    def clear_data(self):
        """
        Deletes all existing data
        :return:
        """
        self.data = {}
        dumped_data = json.dumps(self.data)
        with open(self.path, 'w') as f:
            f.write(dumped_data)
