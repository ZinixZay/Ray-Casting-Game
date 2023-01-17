import json
from paths import DATA_PATH


class DataService:
    def __init__(self, path: str = f"{DATA_PATH}data.json"):
        self.data = {}
        self.path = path

    def save_data(self, head: str, body) -> str:
        self.update_data()
        self.data[head] = body
        dumped_data = json.dumps(self.data)
        with open(self.path, 'w') as f:
            f.write(dumped_data)

    def update_data(self):
        with open(self.path) as f:
            self.data = json.load(f)

    def get_data(self, head: str):
        self.update_data()
        if head in self.data.keys():
            return self.data[head]

    def get_all_data(self):
        self.update_data()
        return self.data

    def clear_data(self):
        self.data = {}
        dumped_data = json.dumps(self.data)
        with open(self.path, 'w') as f:
            f.write(dumped_data)
