import json


class _IOManager:
    mats_path: str = 'data/MATS.json'

    def load_mats(self) -> dict:
        with open(self.mats_path) as file:
            return json.load(file)

    def save_mats(self, data: dict) -> None:
        current_mats = self.load_mats()
        current_mats.update(data)
        with open(self.mats_path, 'w') as file:
            json.dump(current_mats, file)


sentinel = None


def IOManager() -> _IOManager:
    global sentinel
    if sentinel is None:
        sentinel = _IOManager()
    return sentinel
