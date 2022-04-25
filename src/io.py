import json

mats_path: str = "data/MATS.json"


def load_mats() -> dict:
    global mats_path
    with open(mats_path) as file:
        return json.load(file)
