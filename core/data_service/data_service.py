import json


class DataService:
    def __init__(self):
        pass

    def save_data(self, head: str, body: dict):
        with open('C:/Users/Daniel/PycharmProjects/projects/Ray-Casting-Game/assets/data/data.json') as f:
            data = json.load(f)
        data[head] = body
        dumped_data = json.dumps(data)
        with open('C:/Users/Daniel/PycharmProjects/projects/Ray-Casting-Game/assets/data/data.json', 'w') as f:
            f.write(dumped_data)
