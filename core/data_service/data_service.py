import json
from paths import DATA_PATH


class DataService:
    def __init__(self):
        self.data = {}

    def save_data(self, head: str, body: dict) -> str:
        self.update_data()
        if head in self.data.keys():
            return 'error'
        self.data[head] = body
        dumped_data = json.dumps(self.data)
        with open(f"{DATA_PATH}data.json", 'w') as f:
            f.write(dumped_data)
        return 'ok'

    def update_data(self):
        with open(f"{DATA_PATH}data.json") as f:
            self.data = json.load(f)

    def get_data(self, head: str):
        self.update_data()
        if head in self.data.keys():
            return self.data[head]
