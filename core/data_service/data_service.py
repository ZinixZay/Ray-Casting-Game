import json


class DataService:
    def __init__(self):
        self.data = {}

    def save_data(self, head: str, body: dict) -> str:
        self.update_data()
        if head in self.data.keys():
            return 'error'
        self.data[head] = body
        dumped_data = json.dumps(self.data)
        with open('C:/Users/Daniel/PycharmProjects/projects/Ray-Casting-Game/assets/data/data.json', 'w') as f:
            f.write(dumped_data)
        return 'ok'

    def update_data(self):
        with open('C:/Users/Daniel/PycharmProjects/projects/Ray-Casting-Game/assets/data/data.json') as f:
            self.data = json.load(f)
